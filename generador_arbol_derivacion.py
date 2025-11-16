"""
Generador de Árboles de Derivación
Módulo para construir árboles de derivación gramatical basados en reglas de producción.
"""

from typing import Dict, List, Tuple, Optional


class NodoDerivacion:
    """Representa un nodo en el árbol de derivación."""
    
    def __init__(self, simbolo: str, nivel: int = 0):
        """
        Inicializa un nodo del árbol de derivación.
        
        Args:
            simbolo: Símbolo gramatical (S, SN, SV, etc.) o palabra terminal
            nivel: Nivel de profundidad en el árbol
        """
        self.simbolo = simbolo
        self.nivel = nivel
        self.hijos: List[NodoDerivacion] = []
        self.es_terminal = False
        self.palabra = None
        
    def agregar_hijo(self, hijo: 'NodoDerivacion'):
        """Agrega un hijo al nodo."""
        self.hijos.append(hijo)
    
    def marcar_terminal(self, palabra: str):
        """Marca este nodo como terminal y asocia una palabra."""
        self.es_terminal = True
        self.palabra = palabra


class GeneradorArbolDerivacion:
    """
    Clase para generar árboles de derivación gramatical.
    
    Reglas gramaticales implementadas:
    S  → SN + SV          (Oración = Sintagma Nominal + Sintagma Verbal)
    SN → DET + N          (Sintagma Nominal = Determinante + Nombre)
    SN → PRON             (Sintagma Nominal = Pronombre)
    SN → N                (Sintagma Nominal = Nombre)
    SV → V + SN           (Sintagma Verbal = Verbo + Sintagma Nominal)
    SV → V + SP           (Sintagma Verbal = Verbo + Sintagma Preposicional)
    SV → V + ADV          (Sintagma Verbal = Verbo + Adverbio)
    SV → V                (Sintagma Verbal = Verbo)
    SP → PREP + SN        (Sintagma Preposicional = Preposición + SN)
    """
    
    def __init__(self):
        """Inicializa el generador."""
        # Mapeo de POS tags de spaCy a símbolos gramaticales
        self.pos_a_simbolo = {
            'DET': 'DET',
            'NOUN': 'N',
            'PROPN': 'N',
            'PRON': 'PRON',
            'VERB': 'V',
            'ADP': 'PREP',
            'ADV': 'ADV',
            'ADJ': 'ADJ',
            'AUX': 'V'
        }
    
    def generar_arbol(self, doc, analisis: Dict) -> NodoDerivacion:
        """
        Genera el árbol de derivación para una oración.
        
        Args:
            doc: Documento procesado por spaCy
            analisis: Diccionario con el análisis de la oración
            
        Returns:
            Nodo raíz del árbol de derivación
        """
        # Crear nodo raíz (S = Oración)
        raiz = NodoDerivacion('S', 0)
        
        # Dividir en SN (Sintagma Nominal) y SV (Sintagma Verbal)
        sn = NodoDerivacion('SN', 1)
        sv = NodoDerivacion('SV', 1)
        
        raiz.agregar_hijo(sn)
        raiz.agregar_hijo(sv)
        
        # Buscar el verbo principal
        verbo_principal = None
        for token in doc:
            if token.pos_ in ['VERB', 'AUX'] and (token.dep_ == 'ROOT' or 
                                                    any(child.dep_ in ['nsubj', 'nsubjpass'] 
                                                        for child in token.children)):
                verbo_principal = token
                break
        
        if not verbo_principal:
            # Si no hay verbo principal, usar el ROOT
            for token in doc:
                if token.dep_ == 'ROOT':
                    verbo_principal = token
                    break
        
        if verbo_principal:
            # Construir SN (Sujeto)
            sujeto_token = None
            for token in doc:
                if token.dep_ in ['nsubj', 'nsubjpass'] and token.head == verbo_principal:
                    sujeto_token = token
                    break
            
            # Si no hay sujeto explícito, buscar pronombre antes del verbo
            if not sujeto_token:
                for token in doc:
                    if token.pos_ == 'PRON' and token.i < verbo_principal.i:
                        sujeto_token = token
                        break
            
            if sujeto_token:
                self._construir_sintagma_nominal(sn, sujeto_token, doc)
            else:
                # SN implícito (sujeto tácito)
                sn_implicito = NodoDerivacion('(sujeto tácito)', 2)
                sn_implicito.es_terminal = True
                sn.agregar_hijo(sn_implicito)
            
            # Construir SV (Predicado)
            self._construir_sintagma_verbal(sv, verbo_principal, doc)
        
        return raiz
    
    def _construir_sintagma_nominal(self, nodo_sn: NodoDerivacion, token_nucleo, doc):
        """Construye un sintagma nominal."""
        # Obtener todos los tokens del sintagma
        tokens_sn = list(token_nucleo.subtree)
        tokens_sn.sort(key=lambda t: t.i)
        
        # Determinar la estructura del SN
        if token_nucleo.pos_ == 'PRON':
            # SN → PRON
            pron = NodoDerivacion('PRON', nodo_sn.nivel + 1)
            pron.marcar_terminal(token_nucleo.text)
            nodo_sn.agregar_hijo(pron)
        
        elif token_nucleo.pos_ in ['NOUN', 'PROPN']:
            # Buscar determinante
            tiene_det = False
            for token in tokens_sn:
                if token.pos_ == 'DET':
                    tiene_det = True
                    break
            
            if tiene_det:
                # SN → DET + N
                for token in tokens_sn:
                    if token.pos_ == 'DET':
                        det = NodoDerivacion('DET', nodo_sn.nivel + 1)
                        det.marcar_terminal(token.text)
                        nodo_sn.agregar_hijo(det)
                
                # Agregar sustantivo(s) y modificadores
                for token in tokens_sn:
                    if token.pos_ in ['NOUN', 'PROPN']:
                        n = NodoDerivacion('N', nodo_sn.nivel + 1)
                        n.marcar_terminal(token.text)
                        nodo_sn.agregar_hijo(n)
            else:
                # SN → N
                n = NodoDerivacion('N', nodo_sn.nivel + 1)
                n.marcar_terminal(token_nucleo.text)
                nodo_sn.agregar_hijo(n)
    
    def _construir_sintagma_verbal(self, nodo_sv: NodoDerivacion, verbo: any, doc):
        """Construye un sintagma verbal."""
        # Agregar el verbo
        v = NodoDerivacion('V', nodo_sv.nivel + 1)
        v.marcar_terminal(verbo.text)
        nodo_sv.agregar_hijo(v)
        
        # Buscar complementos del verbo
        complementos = []
        tiene_obj = False
        tiene_prep = False
        tiene_adv = False
        
        for token in doc:
            if token.head == verbo and token != verbo:
                if token.dep_ in ['obj', 'dobj', 'iobj']:
                    complementos.append(('obj', token))
                    tiene_obj = True
                elif token.pos_ == 'ADP':
                    complementos.append(('prep', token))
                    tiene_prep = True
                elif token.pos_ == 'ADV':
                    complementos.append(('adv', token))
                    tiene_adv = True
        
        # Construir complementos
        for tipo, token in complementos:
            if tipo == 'obj':
                # SV → V + SN
                sn_complemento = NodoDerivacion('SN', nodo_sv.nivel + 1)
                nodo_sv.agregar_hijo(sn_complemento)
                self._construir_sintagma_nominal(sn_complemento, token, doc)
            
            elif tipo == 'prep':
                # SV → V + SP
                sp = NodoDerivacion('SP', nodo_sv.nivel + 1)
                nodo_sv.agregar_hijo(sp)
                
                # SP → PREP + SN
                prep = NodoDerivacion('PREP', sp.nivel + 1)
                prep.marcar_terminal(token.text)
                sp.agregar_hijo(prep)
                
                # Buscar el SN que sigue a la preposición
                for hijo in token.children:
                    if hijo.pos_ in ['NOUN', 'PROPN', 'PRON']:
                        sn = NodoDerivacion('SN', sp.nivel + 1)
                        sp.agregar_hijo(sn)
                        self._construir_sintagma_nominal(sn, hijo, doc)
                        break
            
            elif tipo == 'adv':
                # SV → V + ADV
                adv = NodoDerivacion('ADV', nodo_sv.nivel + 1)
                adv.marcar_terminal(token.text)
                nodo_sv.agregar_hijo(adv)
    
    def obtener_reglas_aplicadas(self, raiz: NodoDerivacion) -> List[str]:
        """
        Extrae las reglas de derivación aplicadas en el árbol.
        
        Args:
            raiz: Nodo raíz del árbol
            
        Returns:
            Lista de reglas aplicadas
        """
        reglas = []
        self._extraer_reglas(raiz, reglas)
        return reglas
    
    def _extraer_reglas(self, nodo: NodoDerivacion, reglas: List[str]):
        """Extrae reglas recursivamente."""
        if not nodo.hijos:
            return
        
        # Construir la regla
        lado_izquierdo = nodo.simbolo
        lado_derecho = ' + '.join([hijo.simbolo for hijo in nodo.hijos])
        
        if not any(hijo.es_terminal for hijo in nodo.hijos):
            regla = f"{lado_izquierdo} → {lado_derecho}"
            if regla not in reglas:
                reglas.append(regla)
        
        # Recursión en los hijos
        for hijo in nodo.hijos:
            self._extraer_reglas(hijo, reglas)
    
    def imprimir_arbol(self, nodo: NodoDerivacion, prefijo: str = "", es_ultimo: bool = True):
        """
        Imprime el árbol en formato ASCII.
        
        Args:
            nodo: Nodo actual
            prefijo: Prefijo para la indentación
            es_ultimo: Si es el último hijo
        """
        # Símbolo del conector
        conector = "└── " if es_ultimo else "├── "
        
        # Imprimir el nodo actual
        if nodo.es_terminal:
            print(f"{prefijo}{conector}{nodo.simbolo} → '{nodo.palabra}'")
        else:
            print(f"{prefijo}{conector}{nodo.simbolo}")
        
        # Preparar prefijo para los hijos
        if nodo.hijos:
            extension = "    " if es_ultimo else "│   "
            nuevo_prefijo = prefijo + extension
            
            # Recursión para cada hijo
            for i, hijo in enumerate(nodo.hijos):
                es_ultimo_hijo = (i == len(nodo.hijos) - 1)
                self.imprimir_arbol(hijo, nuevo_prefijo, es_ultimo_hijo)
