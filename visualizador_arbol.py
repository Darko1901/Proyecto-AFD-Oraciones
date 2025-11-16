"""
Visualizador de Árbol Sintáctico
Módulo para generar representaciones gráficas de árboles sintácticos
usando matplotlib y networkx.
"""

import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import FancyBboxPatch
import os
from datetime import datetime


class VisualizadorArbol:
    """
    Clase para generar visualizaciones de árboles sintácticos.
    """
    
    def __init__(self):
        """Inicializa el visualizador."""
        # Configurar matplotlib para no usar GUI interactiva
        plt.ioff()
        
        # Crear carpeta para guardar imágenes si no existe
        self.carpeta_imagenes = "arboles_sintacticos"
        if not os.path.exists(self.carpeta_imagenes):
            os.makedirs(self.carpeta_imagenes)
    
    def generar_arbol(self, doc, oracion: str) -> str:
        """
        Genera una imagen del árbol sintáctico de la oración.
        
        Args:
            doc: Documento procesado por spaCy
            oracion: Texto original de la oración
            
        Returns:
            Ruta del archivo de imagen generado
        """
        # Crear grafo dirigido
        G = nx.DiGraph()
        
        # Diccionario para almacenar información de los nodos
        nodos_info = {}
        
        # Agregar nodos al grafo
        for token in doc:
            nodo_id = token.i
            etiqueta = f"{token.text}\n[{token.pos_}]\n({token.dep_})"
            nodos_info[nodo_id] = {
                'label': etiqueta,
                'pos': token.pos_,
                'dep': token.dep_,
                'text': token.text
            }
            G.add_node(nodo_id, **nodos_info[nodo_id])
        
        # Agregar aristas (dependencias)
        for token in doc:
            if token.head != token:  # Evitar auto-referencias
                G.add_edge(token.head.i, token.i)
        
        # Crear figura
        fig, ax = plt.subplots(1, 1, figsize=(14, 10))
        
        # Calcular posiciones jerárquicas
        try:
            pos = self._calcular_posiciones_jerarquicas(G, doc)
        except:
            # Si falla, usar layout automático
            pos = nx.spring_layout(G, k=2, iterations=50)
        
        # Colores según la categoría gramatical
        colores = {
            'VERB': '#FF6B6B',    # Rojo para verbos
            'NOUN': '#4ECDC4',    # Turquesa para sustantivos
            'PRON': '#95E1D3',    # Verde claro para pronombres
            'ADJ': '#F38181',     # Rosa para adjetivos
            'ADV': '#AA96DA',     # Morado para adverbios
            'ADP': '#FCBAD3',     # Rosa claro para preposiciones
            'DET': '#FFFFD2',     # Amarillo claro para determinantes
            'PROPN': '#A8E6CF',   # Verde para nombres propios
        }
        
        # Asignar colores a los nodos
        node_colors = []
        for nodo_id in G.nodes():
            pos_tag = nodos_info[nodo_id]['pos']
            color = colores.get(pos_tag, '#E0E0E0')  # Gris por defecto
            node_colors.append(color)
        
        # Dibujar aristas
        nx.draw_networkx_edges(
            G, pos, ax=ax,
            edge_color='#666666',
            arrows=True,
            arrowsize=20,
            arrowstyle='->',
            width=2,
            connectionstyle='arc3,rad=0.1'
        )
        
        # Dibujar nodos
        nx.draw_networkx_nodes(
            G, pos, ax=ax,
            node_color=node_colors,
            node_size=3000,
            node_shape='o',
            alpha=0.9,
            edgecolors='#333333',
            linewidths=2
        )
        
        # Dibujar etiquetas
        labels = {nodo_id: info['label'] for nodo_id, info in nodos_info.items()}
        nx.draw_networkx_labels(
            G, pos, labels, ax=ax,
            font_size=9,
            font_weight='bold',
            font_family='sans-serif'
        )
        
        # Configurar título y estilo
        ax.set_title(
            f'Árbol Sintáctico\n"{oracion}"',
            fontsize=16,
            fontweight='bold',
            pad=20
        )
        
        # Agregar leyenda
        self._agregar_leyenda(ax, colores)
        
        # Eliminar ejes
        ax.axis('off')
        
        # Ajustar márgenes
        plt.tight_layout()
        
        # Generar nombre de archivo único
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"arbol_{timestamp}.png"
        ruta_archivo = os.path.join(self.carpeta_imagenes, nombre_archivo)
        
        # Guardar imagen
        plt.savefig(ruta_archivo, dpi=300, bbox_inches='tight', facecolor='white')
        plt.close(fig)
        
        return ruta_archivo
    
    def _calcular_posiciones_jerarquicas(self, G, doc):
        """
        Calcula posiciones jerárquicas para el árbol sintáctico.
        
        Args:
            G: Grafo de networkx
            doc: Documento de spaCy
            
        Returns:
            Diccionario con posiciones de nodos
        """
        # Encontrar la raíz (ROOT)
        raiz = None
        for token in doc:
            if token.dep_ == "ROOT":
                raiz = token.i
                break
        
        if raiz is None:
            # Si no hay raíz explícita, usar layout por defecto
            return nx.spring_layout(G, k=2, iterations=50)
        
        # Calcular niveles (profundidad en el árbol)
        niveles = {}
        self._asignar_niveles(G, raiz, niveles, 0)
        
        # Contar nodos por nivel
        nodos_por_nivel = {}
        for nodo, nivel in niveles.items():
            if nivel not in nodos_por_nivel:
                nodos_por_nivel[nivel] = []
            nodos_por_nivel[nivel].append(nodo)
        
        # Calcular posiciones
        pos = {}
        max_nivel = max(niveles.values()) if niveles else 0
        
        for nivel, nodos in nodos_por_nivel.items():
            num_nodos = len(nodos)
            y = 1 - (nivel / (max_nivel + 1))  # Invertir Y para que la raíz esté arriba
            
            # Distribuir nodos horizontalmente
            for i, nodo in enumerate(sorted(nodos)):
                if num_nodos == 1:
                    x = 0.5
                else:
                    x = i / (num_nodos - 1)
                pos[nodo] = (x, y)
        
        return pos
    
    def _asignar_niveles(self, G, nodo, niveles, nivel_actual):
        """Asigna niveles recursivamente a los nodos del árbol."""
        niveles[nodo] = nivel_actual
        
        # Obtener hijos (sucesores en el grafo dirigido)
        hijos = list(G.successors(nodo))
        for hijo in hijos:
            if hijo not in niveles:  # Evitar ciclos
                self._asignar_niveles(G, hijo, niveles, nivel_actual + 1)
    
    def _agregar_leyenda(self, ax, colores):
        """Agrega una leyenda con los colores de las categorías gramaticales."""
        leyenda_items = [
            ('VERB - Verbo', colores.get('VERB', '#E0E0E0')),
            ('NOUN - Sustantivo', colores.get('NOUN', '#E0E0E0')),
            ('PRON - Pronombre', colores.get('PRON', '#E0E0E0')),
            ('ADJ - Adjetivo', colores.get('ADJ', '#E0E0E0')),
            ('ADV - Adverbio', colores.get('ADV', '#E0E0E0')),
            ('ADP - Preposición', colores.get('ADP', '#E0E0E0')),
            ('DET - Determinante', colores.get('DET', '#E0E0E0')),
        ]
        
        # Crear patches para la leyenda
        from matplotlib.patches import Patch
        patches = [Patch(facecolor=color, edgecolor='#333333', label=label) 
                   for label, color in leyenda_items]
        
        ax.legend(
            handles=patches,
            loc='upper left',
            bbox_to_anchor=(1.02, 1),
            fontsize=9,
            frameon=True,
            fancybox=True,
            shadow=True
        )
    
    def abrir_imagen(self, ruta_archivo: str):
        """
        Abre la imagen generada con el visor predeterminado del sistema.
        
        Args:
            ruta_archivo: Ruta del archivo de imagen
        """
        import subprocess
        import platform
        
        sistema = platform.system()
        
        try:
            if sistema == 'Linux':
                subprocess.run(['xdg-open', ruta_archivo], check=False)
            elif sistema == 'Darwin':  # macOS
                subprocess.run(['open', ruta_archivo], check=False)
            elif sistema == 'Windows':
                os.startfile(ruta_archivo)
            else:
                print(f"⚠️  No se pudo abrir automáticamente. Archivo guardado en: {ruta_archivo}")
        except Exception as e:
            print(f"⚠️  Error al abrir imagen: {e}")
            print(f"   Archivo guardado en: {ruta_archivo}")
    
    def generar_arbol_derivacion(self, nodo_raiz, oracion: str) -> str:
        """
        Genera una imagen del árbol de derivación gramatical.
        
        Args:
            nodo_raiz: Nodo raíz del árbol de derivación
            oracion: Texto original de la oración
            
        Returns:
            Ruta del archivo de imagen generado
        """
        from generador_arbol_derivacion import NodoDerivacion
        
        # Crear grafo dirigido
        G = nx.DiGraph()
        
        # Contador para IDs únicos de nodos
        contador = [0]
        nodos_info = {}
        
        def agregar_nodos_recursivo(nodo: NodoDerivacion, padre_id=None):
            """Agrega nodos recursivamente al grafo."""
            nodo_id = contador[0]
            contador[0] += 1
            
            # Etiqueta del nodo
            if nodo.es_terminal:
                etiqueta = f"{nodo.simbolo}\n'{nodo.palabra}'"
                color = '#FFE5B4'  # Beige para terminales
            else:
                etiqueta = nodo.simbolo
                color = self._obtener_color_no_terminal(nodo.simbolo)
            
            nodos_info[nodo_id] = {
                'label': etiqueta,
                'color': color,
                'es_terminal': nodo.es_terminal
            }
            
            G.add_node(nodo_id, **nodos_info[nodo_id])
            
            # Agregar arista si tiene padre
            if padre_id is not None:
                G.add_edge(padre_id, nodo_id)
            
            # Procesar hijos
            for hijo in nodo.hijos:
                agregar_nodos_recursivo(hijo, nodo_id)
            
            return nodo_id
        
        # Construir el grafo
        agregar_nodos_recursivo(nodo_raiz)
        
        # Crear figura
        fig, ax = plt.subplots(1, 1, figsize=(16, 12))
        
        # Calcular posiciones jerárquicas
        pos = self._calcular_posiciones_jerarquicas_derivacion(G)
        
        # Obtener colores de los nodos
        node_colors = [nodos_info[nodo_id]['color'] for nodo_id in G.nodes()]
        
        # Dibujar aristas
        nx.draw_networkx_edges(
            G, pos, ax=ax,
            edge_color='#444444',
            arrows=True,
            arrowsize=15,
            arrowstyle='->',
            width=2.5,
            connectionstyle='arc3,rad=0'
        )
        
        # Dibujar nodos
        node_sizes = [4000 if nodos_info[n]['es_terminal'] else 5000 for n in G.nodes()]
        nx.draw_networkx_nodes(
            G, pos, ax=ax,
            node_color=node_colors,
            node_size=node_sizes,
            node_shape='s',  # Cuadrados para derivación
            alpha=0.9,
            edgecolors='#333333',
            linewidths=2.5
        )
        
        # Dibujar etiquetas
        labels = {nodo_id: info['label'] for nodo_id, info in nodos_info.items()}
        nx.draw_networkx_labels(
            G, pos, labels, ax=ax,
            font_size=10,
            font_weight='bold',
            font_family='monospace'
        )
        
        # Configurar título
        ax.set_title(
            f'Árbol de Derivación Gramatical\n"{oracion}"',
            fontsize=18,
            fontweight='bold',
            pad=25
        )
        
        # Agregar leyenda de símbolos
        self._agregar_leyenda_derivacion(ax)
        
        # Eliminar ejes
        ax.axis('off')
        
        # Ajustar márgenes
        plt.tight_layout()
        
        # Generar nombre de archivo único
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"derivacion_{timestamp}.png"
        ruta_archivo = os.path.join(self.carpeta_imagenes, nombre_archivo)
        
        # Guardar imagen
        plt.savefig(ruta_archivo, dpi=300, bbox_inches='tight', facecolor='white')
        plt.close(fig)
        
        return ruta_archivo
    
    def _obtener_color_no_terminal(self, simbolo: str) -> str:
        """Obtiene el color para un símbolo no terminal."""
        colores = {
            'S': '#FF6B6B',      # Rojo para oración
            'SN': '#4ECDC4',     # Turquesa para sintagma nominal
            'SV': '#95E1D3',     # Verde para sintagma verbal
            'SP': '#FCBAD3',     # Rosa para sintagma preposicional
            'DET': '#FFFFD2',    # Amarillo para determinante
            'N': '#A8E6CF',      # Verde claro para nombre
            'PRON': '#C7CEEA',   # Azul claro para pronombre
            'V': '#FFDAC1',      # Naranja claro para verbo
            'PREP': '#E2B0FF',   # Morado claro para preposición
            'ADV': '#FFB7B2',    # Rosa salmón para adverbio
            'ADJ': '#B5EAD7',    # Verde menta para adjetivo
        }
        return colores.get(simbolo, '#E0E0E0')
    
    def _calcular_posiciones_jerarquicas_derivacion(self, G):
        """Calcula posiciones jerárquicas para el árbol de derivación."""
        # Encontrar la raíz (nodo sin predecesores)
        raices = [n for n in G.nodes() if G.in_degree(n) == 0]
        
        if not raices:
            return nx.spring_layout(G, k=2, iterations=50)
        
        raiz = raices[0]
        
        # Calcular niveles usando BFS
        niveles = {raiz: 0}
        cola = [raiz]
        
        while cola:
            nodo_actual = cola.pop(0)
            nivel_actual = niveles[nodo_actual]
            
            for sucesor in G.successors(nodo_actual):
                if sucesor not in niveles:
                    niveles[sucesor] = nivel_actual + 1
                    cola.append(sucesor)
        
        # Agrupar nodos por nivel
        nodos_por_nivel = {}
        for nodo, nivel in niveles.items():
            if nivel not in nodos_por_nivel:
                nodos_por_nivel[nivel] = []
            nodos_por_nivel[nivel].append(nodo)
        
        # Calcular posiciones
        pos = {}
        max_nivel = max(niveles.values()) if niveles else 0
        
        for nivel, nodos in nodos_por_nivel.items():
            num_nodos = len(nodos)
            y = 1 - (nivel / (max_nivel + 1))
            
            for i, nodo in enumerate(sorted(nodos)):
                if num_nodos == 1:
                    x = 0.5
                else:
                    x = (i + 0.5) / num_nodos
                pos[nodo] = (x, y)
        
        return pos
    
    def _agregar_leyenda_derivacion(self, ax):
        """Agrega leyenda para el árbol de derivación."""
        from matplotlib.patches import Patch
        
        leyenda_items = [
            ('S - Oración', self._obtener_color_no_terminal('S')),
            ('SN - Sintagma Nominal', self._obtener_color_no_terminal('SN')),
            ('SV - Sintagma Verbal', self._obtener_color_no_terminal('SV')),
            ('SP - Sintagma Preposicional', self._obtener_color_no_terminal('SP')),
            ('Terminal - Palabra', '#FFE5B4'),
        ]
        
        patches = [Patch(facecolor=color, edgecolor='#333333', label=label) 
                   for label, color in leyenda_items]
        
        ax.legend(
            handles=patches,
            loc='upper left',
            bbox_to_anchor=(1.02, 1),
            fontsize=10,
            frameon=True,
            fancybox=True,
            shadow=True
        )
