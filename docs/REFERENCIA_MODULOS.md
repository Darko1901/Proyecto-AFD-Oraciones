# Referencia de Modulos: Analizador de Oraciones con AFD

---

## Tabla de Contenidos

1. [Vista General de Modulos](#1-vista-general-de-modulos)
2. [primer_AFD.py - Modulo Principal](#2-primer_afdpy---modulo-principal)
3. [analizador_oraciones.py - Analisis NLP](#3-analizador_oracionespy---analisis-nlp)
4. [visualizador_arbol.py - Visualizacion](#4-visualizador_arbolpy---visualizacion)
5. [generador_arbol_derivacion.py - Derivacion](#5-generador_arbol_derivacionpy---derivacion)
6. [Archivos de Prueba](#6-archivos-de-prueba)
7. [Archivos de Utilidad](#7-archivos-de-utilidad)
8. [Guia de Ejecucion por Archivo](#8-guia-de-ejecucion-por-archivo)

---

## 1. Vista General de Modulos

### 1.1 Mapa de Archivos del Proyecto

```
Proyecto-AFD-Oraciones/
|
|-- MODULOS PRINCIPALES
|   |-- primer_AFD.py                 [EJECUTABLE] Punto de entrada
|   |-- analizador_oraciones.py       [MODULO] Analisis NLP
|   |-- visualizador_arbol.py         [MODULO] Generacion graficos
|   |-- generador_arbol_derivacion.py [MODULO] Arboles derivacion
|
|-- ARCHIVOS DE PRUEBA
|   |-- test_analizador.py            [EJECUTABLE] Suite completa
|   |-- test_arbol.py                 [EJECUTABLE] Prueba arboles
|   |-- test_simple.py                [EJECUTABLE] Prueba rapida
|
|-- UTILIDADES
|   |-- diagrama_automata.py          [EJECUTABLE] Diagrama ASCII
|   |-- debug_spacy.py                [EJECUTABLE] Depuracion NLP
|
|-- CONFIGURACION
|   |-- requirements.txt              Dependencias Python
|   |-- README.md                     Documentacion usuario
|
|-- SALIDA
    |-- arboles_sintacticos/          Imagenes generadas
```

### 1.2 Relaciones entre Modulos

```
+------------------+
|  primer_AFD.py   |<------ PUNTO DE ENTRADA
+------------------+
        |
        | importa
        |
        +------------------------+------------------------+
        |                        |                        |
        v                        v                        v
+------------------+   +------------------+   +------------------+
| analizador_      |   | visualizador_    |   | generador_arbol_ |
| oraciones.py     |   | arbol.py         |   | derivacion.py    |
+------------------+   +------------------+   +------------------+
        |                        |                        |
        v                        v                        |
    [spaCy]              [matplotlib]                     |
                         [networkx]                       |
                               |                          |
                               +--------> usa <-----------+
                                    NodoDerivacion
```

### 1.3 Resumen de Propositos

| Archivo | Tipo | Proposito |
|---------|------|-----------|
| primer_AFD.py | Ejecutable | Programa principal con interfaz de usuario |
| analizador_oraciones.py | Modulo | Procesamiento de lenguaje natural |
| visualizador_arbol.py | Modulo | Generacion de graficos PNG |
| generador_arbol_derivacion.py | Modulo | Construccion de arboles formales |
| test_analizador.py | Ejecutable | Pruebas automaticas completas |
| test_arbol.py | Ejecutable | Prueba de generacion de arboles |
| test_simple.py | Ejecutable | Prueba rapida minima |
| diagrama_automata.py | Ejecutable | Visualizacion ASCII del AFD |
| debug_spacy.py | Ejecutable | Herramienta de depuracion |

---

## 2. primer_AFD.py - Modulo Principal

### 2.1 Informacion General

| Atributo | Valor |
|----------|-------|
| Ubicacion | `/primer_AFD.py` |
| Tipo | Ejecutable |
| Lineas de codigo | ~260 |
| Dependencias | analizador_oraciones, visualizador_arbol, generador_arbol_derivacion |

### 2.2 Como Ejecutar

```bash
python primer_AFD.py
```

### 2.3 Que Esperar

1. Se muestra banner de bienvenida
2. Prompt para ingresar oracion
3. Analisis automatico de la oracion
4. Resultado de aceptacion/rechazo
5. Generacion de arboles (si acepta)
6. Opciones para visualizar

### 2.4 Clase AFDOraciones

```python
class AFDOraciones:
    """
    Automata Finito Determinista para analisis de oraciones.
    
    Atributos de Instancia:
    -----------------------
    analizador : AnalizadorOraciones
        Instancia del analizador NLP
    visualizador : VisualizadorArbol
        Instancia del generador de graficos
    generador_derivacion : GeneradorArbolDerivacion
        Instancia del generador de arboles de derivacion
    estados : list
        Lista de estados del AFD ['q0', 'q1', 'q2', 'q3', 'qr']
    estado_inicial : str
        Estado inicial 'q0'
    estados_aceptacion : list
        Estados de aceptacion ['q3']
    estado_actual : str
        Estado actual del automata
    historial : list
        Lista de tuplas (estado, razon) con historial de transiciones
    """
```

### 2.5 Metodos Publicos

#### 2.5.1 __init__(self)

```python
def __init__(self):
    """
    Inicializa el AFD con todos sus componentes.
    
    Acciones:
        - Crea instancias de los tres modulos auxiliares
        - Configura estados del automata
        - Inicializa historial vacio
    
    Ejemplo:
        afd = AFDOraciones()
    """
```

#### 2.5.2 procesar_oracion(self, oracion: str) -> dict

```python
def procesar_oracion(self, oracion: str) -> dict:
    """
    Procesa una oracion a traves del automata.
    
    Parametros:
        oracion : str
            Oracion en espanol a analizar
    
    Retorna:
        dict : Diccionario con estructura:
            {
                'aceptada': bool,
                'estado_final': str,
                'historial': list,
                'analisis_nlp': dict,
                'ruta_arbol_sintactico': str | None,
                'ruta_arbol_derivacion': str | None,
                'arbol_derivacion': NodoDerivacion | None
            }
    
    Ejemplo:
        resultado = afd.procesar_oracion("el gato come pescado")
        if resultado['aceptada']:
            print("Oracion valida")
    """
```

#### 2.5.3 mostrar_analisis_detallado(self, resultado: dict)

```python
def mostrar_analisis_detallado(self, resultado: dict):
    """
    Muestra analisis detallado incluyendo arbol ASCII.
    
    Parametros:
        resultado : dict
            Resultado de procesar_oracion()
    
    Salida:
        Imprime en consola:
        - Estadisticas del analisis
        - Arbol de derivacion en formato ASCII
    
    Ejemplo:
        resultado = afd.procesar_oracion("el gato come")
        afd.mostrar_analisis_detallado(resultado)
    """
```

### 2.6 Metodos Privados

#### 2.6.1 _transicion(self, nuevo_estado: str, razon: str)

```python
def _transicion(self, nuevo_estado: str, razon: str):
    """
    Realiza una transicion de estado.
    
    Parametros:
        nuevo_estado : str
            Estado destino ('q0', 'q1', 'q2', 'q3', 'qr')
        razon : str
            Descripcion de la causa de la transicion
    
    Efectos:
        - Actualiza self.estado_actual
        - Agrega entrada al historial
        - Imprime informacion de transicion
    """
```

#### 2.6.2 _generar_resultado(self, resultado_nlp: dict, aceptada: bool) -> dict

```python
def _generar_resultado(self, resultado_nlp: dict, aceptada: bool) -> dict:
    """
    Genera el diccionario de resultado final.
    
    Parametros:
        resultado_nlp : dict
            Resultado del analisis NLP
        aceptada : bool
            Si la oracion fue aceptada
    
    Retorna:
        dict : Resultado completo del analisis
    
    Efectos secundarios:
        - Si aceptada, genera arboles PNG
        - Imprime resultado en consola
    """
```

### 2.7 Funcion main()

```python
def main():
    """
    Funcion principal del programa.
    
    Flujo:
        1. Muestra banner de bienvenida
        2. Crea instancia de AFDOraciones
        3. Loop infinito:
           a. Solicita oracion al usuario
           b. Si 'salir', termina
           c. Procesa oracion
           d. Ofrece visualizar arboles
           e. Ofrece analisis detallado
    
    Manejo de excepciones:
        - KeyboardInterrupt: Mensaje de despedida
        - Exception: Muestra error
    """
```

### 2.8 Diagrama de Flujo de Ejecucion

```
primer_AFD.py
      |
      v
[Importaciones]
      |
      v
[Definicion clase AFDOraciones]
      |
      v
[Definicion main()]
      |
      v
[if __name__ == "__main__"]
      |
      v
[try: main()]
      |
      +---> [Banner bienvenida]
      |           |
      |           v
      |     [Crear AFDOraciones]
      |           |
      |           v
      |     [Loop: solicitar oracion]
      |           |
      |           +---> [Si "salir": break]
      |           |
      |           v
      |     [procesar_oracion()]
      |           |
      |           v
      |     [Mostrar resultado]
      |           |
      |           v
      |     [Ofrecer visualizar arboles]
      |           |
      |           v
      |     [Ofrecer analisis detallado]
      |           |
      |           +---> [Volver al loop]
      |
      v
[except KeyboardInterrupt]
      |
      v
[except Exception]
      |
      v
[FIN]
```

---

## 3. analizador_oraciones.py - Analisis NLP

### 3.1 Informacion General

| Atributo | Valor |
|----------|-------|
| Ubicacion | `/analizador_oraciones.py` |
| Tipo | Modulo (no ejecutable directamente) |
| Lineas de codigo | ~186 |
| Dependencias externas | spaCy |

### 3.2 Clase AnalizadorOraciones

```python
class AnalizadorOraciones:
    """
    Analizador de oraciones usando procesamiento de lenguaje natural.
    
    Atributos de Instancia:
    -----------------------
    nlp : spacy.Language
        Pipeline de spaCy con modelo es_core_news_sm
    
    Excepciones:
    ------------
    OSError
        Si el modelo de spaCy no esta instalado
    """
```

### 3.3 Metodos Publicos

#### 3.3.1 __init__(self)

```python
def __init__(self):
    """
    Inicializa el analizador cargando el modelo de spaCy.
    
    Carga:
        - Modelo 'es_core_news_sm' para espanol
    
    Raises:
        OSError: Si el modelo no esta instalado
    
    Ejemplo:
        try:
            analizador = AnalizadorOraciones()
        except OSError:
            print("Instalar modelo con: python -m spacy download es_core_news_sm")
    """
```

#### 3.3.2 analizar_oracion(self, oracion: str) -> Dict

```python
def analizar_oracion(self, oracion: str) -> Dict:
    """
    Analiza una oracion y extrae componentes gramaticales.
    
    Parametros:
        oracion : str
            Oracion en espanol a analizar
    
    Retorna:
        dict : Diccionario con estructura:
            {
                'valida': bool,           # Si cumple estructura basica
                'sujeto': str | None,     # Sujeto identificado
                'verbo': str | None,      # Verbo principal
                'predicado': str | None,  # Predicado completo
                'tokens': list,           # Lista de strings
                'pos_tags': list,         # Lista de dicts con POS
                'dependencias': list,     # (no usado actualmente)
                'doc': spacy.Doc          # Documento procesado
            }
    
    Algoritmo:
        1. Procesa oracion con spaCy
        2. Busca verbo principal (ROOT o VERB)
        3. Busca sujeto (nsubj del verbo)
        4. Construye predicado (verbo + complementos)
        5. Valida estructura
    
    Ejemplo:
        resultado = analizador.analizar_oracion("el gato come")
        print(resultado['sujeto'])  # "el gato"
        print(resultado['verbo'])   # "come"
    """
```

#### 3.3.3 obtener_estadisticas(self, resultado: Dict) -> str

```python
def obtener_estadisticas(self, resultado: Dict) -> str:
    """
    Genera reporte textual del analisis.
    
    Parametros:
        resultado : dict
            Resultado de analizar_oracion()
    
    Retorna:
        str : Texto formateado con:
            - Numero de tokens
            - Estado de validez
            - Componentes identificados
            - Tabla de etiquetas POS
    
    Ejemplo:
        resultado = analizador.analizar_oracion("el gato come")
        print(analizador.obtener_estadisticas(resultado))
    """
```

### 3.4 Metodos Privados

#### 3.4.1 _obtener_frase(self, token) -> List

```python
def _obtener_frase(self, token) -> List:
    """
    Obtiene el subtree completo de un token.
    
    Parametros:
        token : spacy.Token
            Token del cual obtener la frase
    
    Retorna:
        list : Lista de tokens que forman el subtree
    
    Uso interno:
        Se usa para obtener frases completas como
        "el gato" a partir del token "gato"
    """
```

### 3.5 Estructura del Resultado

```python
resultado = {
    'valida': True,
    'sujeto': 'el gato',
    'verbo': 'come',
    'predicado': 'come pescado',
    'tokens': ['el', 'gato', 'come', 'pescado'],
    'pos_tags': [
        {'texto': 'el', 'pos': 'DET', 'tag': 'DET', 'dep': 'det'},
        {'texto': 'gato', 'pos': 'NOUN', 'tag': 'NOUN', 'dep': 'nsubj'},
        {'texto': 'come', 'pos': 'VERB', 'tag': 'VERB', 'dep': 'ROOT'},
        {'texto': 'pescado', 'pos': 'NOUN', 'tag': 'NOUN', 'dep': 'obj'}
    ],
    'dependencias': [],
    'doc': <spacy.tokens.doc.Doc object>
}
```

### 3.6 Diagrama de Flujo del Analisis

```
analizar_oracion(oracion)
         |
         v
   [spaCy procesa oracion]
         |
         v
   [Inicializar resultado vacio]
         |
         v
   [Extraer tokens y POS tags]
         |
         v
   [Buscar verbo principal]
         |
         +---> VERB con ROOT? --Si--> [verbo_principal]
         |           |
         |          No
         |           v
         +---> Cualquier VERB? --Si--> [verbo_principal]
         |           |
         |          No
         |           v
         +---> ROOT con hijos nsubj? --Si--> [verbo_principal]
         |           |
         |          No
         |           v
         |     [verbo_principal = None]
         |
         v
   [Si hay verbo_principal:]
         |
         v
   [Buscar sujeto (nsubj)]
         |
         +---> nsubj del verbo? --Si--> [sujeto = subtree]
         |           |
         |          No
         |           v
         +---> PRON antes de verbo? --Si--> [sujeto = pron]
         |
         v
   [Construir predicado]
         |
         v
   [verbo + complementos ordenados]
         |
         v
   [Validar: sujeto+verbo+pred OR verbo]
         |
         v
   [Retornar resultado]
```

---

## 4. visualizador_arbol.py - Visualizacion

### 4.1 Informacion General

| Atributo | Valor |
|----------|-------|
| Ubicacion | `/visualizador_arbol.py` |
| Tipo | Modulo (no ejecutable directamente) |
| Lineas de codigo | ~475 |
| Dependencias externas | matplotlib, networkx |

### 4.2 Clase VisualizadorArbol

```python
class VisualizadorArbol:
    """
    Generador de visualizaciones de arboles sintacticos.
    
    Atributos de Instancia:
    -----------------------
    carpeta_imagenes : str
        Ruta de la carpeta donde se guardan imagenes
        Default: "arboles_sintacticos"
    
    Configuracion:
    --------------
    - matplotlib en modo no interactivo (plt.ioff())
    - Crea carpeta de imagenes si no existe
    """
```

### 4.3 Metodos Publicos

#### 4.3.1 __init__(self)

```python
def __init__(self):
    """
    Inicializa el visualizador.
    
    Acciones:
        - Configura matplotlib en modo no interactivo
        - Crea carpeta 'arboles_sintacticos' si no existe
    
    Ejemplo:
        visualizador = VisualizadorArbol()
    """
```

#### 4.3.2 generar_arbol(self, doc, oracion: str) -> str

```python
def generar_arbol(self, doc, oracion: str) -> str:
    """
    Genera imagen PNG del arbol sintactico.
    
    Parametros:
        doc : spacy.Doc
            Documento procesado por spaCy
        oracion : str
            Texto original de la oracion
    
    Retorna:
        str : Ruta del archivo PNG generado
              Formato: "arboles_sintacticos/arbol_YYYYMMDD_HHMMSS.png"
    
    Proceso:
        1. Crea grafo dirigido con NetworkX
        2. Agrega nodos (tokens) con atributos
        3. Agrega aristas (dependencias)
        4. Calcula posiciones jerarquicas
        5. Asigna colores por categoria POS
        6. Dibuja con matplotlib
        7. Guarda imagen PNG (300 DPI)
    
    Ejemplo:
        ruta = visualizador.generar_arbol(doc, "el gato come")
        print(f"Imagen guardada en: {ruta}")
    """
```

#### 4.3.3 generar_arbol_derivacion(self, nodo_raiz, oracion: str) -> str

```python
def generar_arbol_derivacion(self, nodo_raiz, oracion: str) -> str:
    """
    Genera imagen PNG del arbol de derivacion.
    
    Parametros:
        nodo_raiz : NodoDerivacion
            Raiz del arbol de derivacion
        oracion : str
            Texto original de la oracion
    
    Retorna:
        str : Ruta del archivo PNG generado
              Formato: "arboles_sintacticos/derivacion_YYYYMMDD_HHMMSS.png"
    
    Diferencias con arbol sintactico:
        - Nodos cuadrados (vs circulares)
        - Colores por tipo de sintagma (S, SN, SV, SP)
        - Etiquetas con simbolos gramaticales
    
    Ejemplo:
        ruta = visualizador.generar_arbol_derivacion(arbol, "el gato come")
    """
```

#### 4.3.4 abrir_imagen(self, ruta_archivo: str)

```python
def abrir_imagen(self, ruta_archivo: str):
    """
    Abre imagen con el visor predeterminado del sistema.
    
    Parametros:
        ruta_archivo : str
            Ruta del archivo de imagen
    
    Comportamiento por sistema:
        - Linux: xdg-open
        - macOS: open
        - Windows: os.startfile
    
    Manejo de errores:
        - Si falla, muestra mensaje con ruta del archivo
    
    Ejemplo:
        visualizador.abrir_imagen("arboles_sintacticos/arbol_20251126.png")
    """
```

### 4.4 Metodos Privados

#### 4.4.1 _calcular_posiciones_jerarquicas(self, G, doc) -> dict

```python
def _calcular_posiciones_jerarquicas(self, G, doc) -> dict:
    """
    Calcula posiciones X,Y para layout jerarquico.
    
    Parametros:
        G : networkx.DiGraph
            Grafo del arbol
        doc : spacy.Doc
            Documento de spaCy
    
    Retorna:
        dict : {nodo_id: (x, y)}
    
    Algoritmo:
        1. Encuentra nodo ROOT
        2. Asigna niveles por BFS
        3. Distribuye nodos horizontalmente por nivel
        4. Invierte Y para raiz arriba
    """
```

#### 4.4.2 _asignar_niveles(self, G, nodo, niveles, nivel_actual)

```python
def _asignar_niveles(self, G, nodo, niveles, nivel_actual):
    """
    Asigna niveles recursivamente (DFS).
    
    Modifica:
        niveles : dict
            Diccionario {nodo_id: nivel}
    """
```

#### 4.4.3 _agregar_leyenda(self, ax, colores)

```python
def _agregar_leyenda(self, ax, colores):
    """
    Agrega leyenda de colores al grafico.
    
    Incluye:
        - VERB, NOUN, PRON, ADJ, ADV, ADP, DET
        - Patch coloreado con etiqueta
    """
```

#### 4.4.4 _obtener_color_no_terminal(self, simbolo: str) -> str

```python
def _obtener_color_no_terminal(self, simbolo: str) -> str:
    """
    Obtiene color hexadecimal para simbolo gramatical.
    
    Mapeo:
        S    -> #FF6B6B (rojo)
        SN   -> #4ECDC4 (turquesa)
        SV   -> #95E1D3 (verde)
        SP   -> #FCBAD3 (rosa)
        otros -> #E0E0E0 (gris)
    """
```

### 4.5 Configuracion de Colores

**Arbol Sintactico (por POS):**

```python
colores = {
    'VERB': '#FF6B6B',    # Rojo
    'NOUN': '#4ECDC4',    # Turquesa
    'PRON': '#95E1D3',    # Verde claro
    'ADJ': '#F38181',     # Rosa
    'ADV': '#AA96DA',     # Morado
    'ADP': '#FCBAD3',     # Rosa claro
    'DET': '#FFFFD2',     # Amarillo claro
    'PROPN': '#A8E6CF',   # Verde
}
```

**Arbol Derivacion (por Sintagma):**

```python
colores = {
    'S': '#FF6B6B',       # Rojo
    'SN': '#4ECDC4',      # Turquesa
    'SV': '#95E1D3',      # Verde
    'SP': '#FCBAD3',      # Rosa
    'DET': '#FFFFD2',     # Amarillo
    'N': '#A8E6CF',       # Verde claro
    'PRON': '#C7CEEA',    # Azul claro
    'V': '#FFDAC1',       # Naranja claro
    'PREP': '#E2B0FF',    # Morado claro
    'ADV': '#FFB7B2',     # Rosa salmon
    'ADJ': '#B5EAD7',     # Verde menta
}
```

---

## 5. generador_arbol_derivacion.py - Derivacion

### 5.1 Informacion General

| Atributo | Valor |
|----------|-------|
| Ubicacion | `/generador_arbol_derivacion.py` |
| Tipo | Modulo (no ejecutable directamente) |
| Lineas de codigo | ~289 |
| Dependencias externas | Ninguna |

### 5.2 Clase NodoDerivacion

```python
class NodoDerivacion:
    """
    Nodo individual en el arbol de derivacion.
    
    Atributos de Instancia:
    -----------------------
    simbolo : str
        Simbolo gramatical (S, SN, SV, DET, N, V, etc.)
    nivel : int
        Profundidad en el arbol (raiz = 0)
    hijos : list
        Lista de NodoDerivacion hijos
    es_terminal : bool
        True si es nodo terminal (palabra)
    palabra : str | None
        Palabra asociada (solo si es_terminal)
    """
```

### 5.3 Metodos de NodoDerivacion

#### 5.3.1 __init__(self, simbolo: str, nivel: int = 0)

```python
def __init__(self, simbolo: str, nivel: int = 0):
    """
    Inicializa un nodo de derivacion.
    
    Parametros:
        simbolo : str
            Simbolo gramatical del nodo
        nivel : int
            Nivel de profundidad (default: 0)
    
    Ejemplo:
        raiz = NodoDerivacion('S', 0)
        sn = NodoDerivacion('SN', 1)
    """
```

#### 5.3.2 agregar_hijo(self, hijo: 'NodoDerivacion')

```python
def agregar_hijo(self, hijo: 'NodoDerivacion'):
    """
    Agrega un nodo hijo.
    
    Parametros:
        hijo : NodoDerivacion
            Nodo a agregar como hijo
    
    Ejemplo:
        raiz.agregar_hijo(sn)
        raiz.agregar_hijo(sv)
    """
```

#### 5.3.3 marcar_terminal(self, palabra: str)

```python
def marcar_terminal(self, palabra: str):
    """
    Marca el nodo como terminal con su palabra.
    
    Parametros:
        palabra : str
            Palabra del texto original
    
    Efectos:
        - self.es_terminal = True
        - self.palabra = palabra
    
    Ejemplo:
        det = NodoDerivacion('DET', 2)
        det.marcar_terminal('el')
    """
```

### 5.4 Clase GeneradorArbolDerivacion

```python
class GeneradorArbolDerivacion:
    """
    Generador de arboles de derivacion gramatical.
    
    Atributos de Instancia:
    -----------------------
    pos_a_simbolo : dict
        Mapeo de etiquetas POS a simbolos gramaticales
    
    Reglas Gramaticales:
    --------------------
    S  -> SN + SV
    SN -> DET + N | PRON | N
    SV -> V + SN | V + SP | V + ADV | V
    SP -> PREP + SN
    """
```

### 5.5 Metodos de GeneradorArbolDerivacion

#### 5.5.1 __init__(self)

```python
def __init__(self):
    """
    Inicializa el generador con mapeo POS -> Simbolo.
    
    Mapeo:
        'DET'   -> 'DET'
        'NOUN'  -> 'N'
        'PROPN' -> 'N'
        'PRON'  -> 'PRON'
        'VERB'  -> 'V'
        'ADP'   -> 'PREP'
        'ADV'   -> 'ADV'
        'ADJ'   -> 'ADJ'
        'AUX'   -> 'V'
    """
```

#### 5.5.2 generar_arbol(self, doc, analisis: Dict) -> NodoDerivacion

```python
def generar_arbol(self, doc, analisis: Dict) -> NodoDerivacion:
    """
    Genera arbol de derivacion completo.
    
    Parametros:
        doc : spacy.Doc
            Documento procesado
        analisis : dict
            Resultado de AnalizadorOraciones
    
    Retorna:
        NodoDerivacion : Raiz del arbol (simbolo 'S')
    
    Estructura generada:
        S
        +-- SN (construido segun sujeto)
        +-- SV (construido segun predicado)
    
    Ejemplo:
        arbol = generador.generar_arbol(doc, resultado_nlp)
    """
```

#### 5.5.3 obtener_reglas_aplicadas(self, raiz: NodoDerivacion) -> List[str]

```python
def obtener_reglas_aplicadas(self, raiz: NodoDerivacion) -> List[str]:
    """
    Extrae lista de reglas de produccion usadas.
    
    Parametros:
        raiz : NodoDerivacion
            Raiz del arbol
    
    Retorna:
        list : Lista de strings con formato "A -> B + C"
    
    Ejemplo:
        reglas = generador.obtener_reglas_aplicadas(arbol)
        # ['S -> SN + SV', 'SN -> DET + N']
    """
```

#### 5.5.4 imprimir_arbol(self, nodo, prefijo="", es_ultimo=True)

```python
def imprimir_arbol(self, nodo: NodoDerivacion, prefijo: str = "", 
                   es_ultimo: bool = True):
    """
    Imprime arbol en formato ASCII.
    
    Parametros:
        nodo : NodoDerivacion
            Nodo a imprimir
        prefijo : str
            Prefijo de indentacion
        es_ultimo : bool
            Si es el ultimo hijo
    
    Salida ejemplo:
        +-- S
            +-- SN
            |   +-- DET -> 'el'
            |   +-- N -> 'gato'
            +-- SV
                +-- V -> 'come'
    """
```

### 5.6 Metodos Privados

#### 5.6.1 _construir_sintagma_nominal(self, nodo_sn, token_nucleo, doc)

```python
def _construir_sintagma_nominal(self, nodo_sn, token_nucleo, doc):
    """
    Construye estructura de sintagma nominal.
    
    Reglas aplicadas:
        - Si PRON: SN -> PRON
        - Si tiene DET: SN -> DET + N
        - Solo sustantivo: SN -> N
    """
```

#### 5.6.2 _construir_sintagma_verbal(self, nodo_sv, verbo, doc)

```python
def _construir_sintagma_verbal(self, nodo_sv, verbo, doc):
    """
    Construye estructura de sintagma verbal.
    
    Proceso:
        1. Agrega nodo V con el verbo
        2. Busca complementos (obj, prep, adv)
        3. Para cada complemento:
           - obj -> SN anidado
           - prep -> SP = PREP + SN
           - adv -> ADV terminal
    """
```

#### 5.6.3 _extraer_reglas(self, nodo, reglas)

```python
def _extraer_reglas(self, nodo: NodoDerivacion, reglas: List[str]):
    """
    Extrae reglas recursivamente.
    
    Solo incluye reglas donde ningun hijo es terminal.
    """
```

---

## 6. Archivos de Prueba

### 6.1 test_analizador.py

| Atributo | Valor |
|----------|-------|
| Proposito | Suite completa de pruebas automaticas |
| Oraciones de prueba | 8 (6 validas, 2 invalidas) |

**Como ejecutar:**
```bash
python test_analizador.py
```

**Que esperar:**
- Analiza 8 oraciones automaticamente
- Muestra resultado de cada una
- Resumen final con estadisticas

**Oraciones incluidas:**
1. "yo camino por el parque" (valida)
2. "el gato come pescado" (valida)
3. "Maria estudia matematicas" (valida)
4. "los ninos juegan en el jardin" (valida)
5. "mi hermano lee un libro" (valida)
6. "el perro corre rapidamente" (valida)
7. "por el parque" (invalida)
8. "camino parque" (invalida)

### 6.2 test_arbol.py

| Atributo | Valor |
|----------|-------|
| Proposito | Prueba generacion de arboles |
| Oracion de prueba | "el gato come pescado" |

**Como ejecutar:**
```bash
python test_arbol.py
```

**Que esperar:**
1. Analiza la oracion
2. Genera arbol sintactico PNG
3. Genera arbol derivacion PNG
4. Muestra reglas aplicadas
5. Imprime arbol ASCII
6. Abre ambas imagenes automaticamente

### 6.3 test_simple.py

| Atributo | Valor |
|----------|-------|
| Proposito | Prueba rapida minima |
| Oracion de prueba | "yo camino por el parque" |

**Como ejecutar:**
```bash
python test_simple.py
```

**Que esperar:**
- Solo imprime componentes basicos
- No genera arboles ni graficos

---

## 7. Archivos de Utilidad

### 7.1 diagrama_automata.py

| Atributo | Valor |
|----------|-------|
| Proposito | Mostrar diagrama ASCII del AFD |

**Como ejecutar:**
```bash
python diagrama_automata.py
```

**Que esperar:**
- Diagrama visual del automata en texto
- Ejemplos de transiciones

**Salida:**
```
                         DIAGRAMA DEL AUTOMATA
================================================================

                              +-------------+
                              |     q0      |
                              |   INICIO    |
                              +------+------+
                                     |
                    +----------------+----------------+
                    |                                 |
              [Sujeto encontrado]            [Verbo sin sujeto]
                    |                                 |
                    v                                 v
           +-------------+                   +-------------+
           |     q1      |                   |     q2      |
           |   SUJETO    |--[Verbo found]--> |    VERBO    |
           +-------------+                   +------+------+
                                                    |
                                          [Predicado completo]
                                                    |
                                                    v
                                           +-------------+
                                           |     q3      |
                                           | ACEPTADO    |
                                           +-------------+

                            +-------------+
                            |     qr      |
                            | RECHAZADO   |
                            +-------------+
```

### 7.2 debug_spacy.py

| Atributo | Valor |
|----------|-------|
| Proposito | Depurar procesamiento de spaCy |
| Oracion de prueba | "yo camino por el parque" |

**Como ejecutar:**
```bash
python debug_spacy.py
```

**Que esperar:**
- Tabla detallada de tokens
- POS, Tag, Dep, Head de cada palabra
- Busqueda de verbos ROOT
- Busqueda de sujetos
- Busqueda de pronombres

**Salida ejemplo:**
```
Analizando: 'yo camino por el parque'

============================================================
Texto: yo              POS: PRON       Tag: PRON       Dep: nsubj      Head: camino
Texto: camino          POS: VERB       Tag: VERB       Dep: ROOT       Head: camino
Texto: por             POS: ADP        Tag: ADP        Dep: case       Head: parque
Texto: el              POS: DET        Tag: DET        Dep: det        Head: parque
Texto: parque          POS: NOUN       Tag: NOUN       Dep: obl        Head: camino
```

---

## 8. Guia de Ejecucion por Archivo

### 8.1 Orden Recomendado para Nuevos Usuarios

```
1. INSTALACION
   pip install -r requirements.txt
   python -m spacy download es_core_news_sm

2. FAMILIARIZACION
   python diagrama_automata.py      # Ver estructura del AFD
   python debug_spacy.py            # Entender procesamiento NLP

3. PRUEBAS BASICAS
   python test_simple.py            # Verificar instalacion
   python test_arbol.py             # Ver generacion de arboles

4. PRUEBAS COMPLETAS
   python test_analizador.py        # Suite completa

5. USO INTERACTIVO
   python primer_AFD.py             # Programa principal
```

### 8.2 Resumen de Comandos

| Comando | Descripcion | Tiempo |
|---------|-------------|--------|
| `python primer_AFD.py` | Programa interactivo principal | Continuo |
| `python test_analizador.py` | Suite de 8 pruebas | ~30 seg |
| `python test_arbol.py` | Genera arboles de ejemplo | ~5 seg |
| `python test_simple.py` | Prueba rapida | ~3 seg |
| `python diagrama_automata.py` | Muestra diagrama AFD | Inmediato |
| `python debug_spacy.py` | Depura tokenizacion | ~3 seg |

### 8.3 Diagrama de Decision: Que Archivo Ejecutar

```
                    [Inicio]
                       |
                       v
            +---------------------+
            | Primera vez usando? |
            +---------------------+
               /            \
             Si              No
             /                \
            v                  v
    [diagrama_automata.py]  +-------------------+
            |               | Quieres probar    |
            v               | interactivamente? |
    [test_simple.py]        +-------------------+
            |                  /           \
            v                Si             No
    [test_arbol.py]          /               \
            |               v                 v
            v         [primer_AFD.py]   +-----------+
    [test_analizador.py]                | Depurar?  |
            |                           +-----------+
            v                              /     \
    [primer_AFD.py]                      Si       No
                                         /         \
                                        v           v
                                [debug_spacy.py]  [FIN]
```

### 8.4 Archivos de Salida Generados

| Archivo Ejecutado | Salida Generada |
|-------------------|-----------------|
| primer_AFD.py | arboles_sintacticos/arbol_*.png, derivacion_*.png |
| test_arbol.py | arboles_sintacticos/arbol_*.png, derivacion_*.png |
| test_analizador.py | arboles_sintacticos/arbol_*.png, derivacion_*.png (multiples) |
| test_simple.py | Ninguna (solo consola) |
| diagrama_automata.py | Ninguna (solo consola) |
| debug_spacy.py | Ninguna (solo consola) |

---

## Apendice: Estructura de Imports

### Imports de primer_AFD.py

```python
from analizador_oraciones import AnalizadorOraciones
from visualizador_arbol import VisualizadorArbol
from generador_arbol_derivacion import GeneradorArbolDerivacion
```

### Imports de analizador_oraciones.py

```python
import spacy
from typing import Dict, List, Tuple, Optional
```

### Imports de visualizador_arbol.py

```python
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import FancyBboxPatch
import os
from datetime import datetime
```

### Imports de generador_arbol_derivacion.py

```python
from typing import Dict, List, Tuple, Optional
```

---

**Documento de referencia para el proyecto Analizador de Oraciones con AFD**

**Autores:** Ricardo Mendez, Emiliano Ledesma

**Institucion:** UPQ - Curso de Matematicas
