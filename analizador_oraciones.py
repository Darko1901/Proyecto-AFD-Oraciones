"""
Analizador de Oraciones Simples
Módulo para analizar oraciones en español e identificar sus componentes.
"""

import spacy
from typing import Dict, List, Tuple, Optional


class AnalizadorOraciones:
    """
    Clase para analizar oraciones simples en español usando procesamiento
    de lenguaje natural (NLP).
    """
    
    def __init__(self):
        """Inicializa el analizador con el modelo de spaCy para español."""
        try:
            self.nlp = spacy.load("es_core_news_sm")
        except OSError:
            print("\n ERROR: El modelo de español no está instalado.")
            print("Por favor, ejecuta el siguiente comando:")
            print("    python -m spacy download es_core_news_sm\n")
            raise
    
    def analizar_oracion(self, oracion: str) -> Dict:
        """
        Analiza una oración y extrae sus componentes gramaticales.
        
        Args:
            oracion: La oración a analizar
            
        Returns:
            Diccionario con los componentes identificados
        """
        doc = self.nlp(oracion.strip())
        
        resultado = {
            'valida': False,
            'sujeto': None,
            'verbo': None,
            'predicado': None,
            'tokens': [],
            'pos_tags': [],
            'dependencias': [],
            'doc': doc  # Agregar el documento de spaCy para visualización
        }
        
        # Extraer información de tokens
        for token in doc:
            resultado['tokens'].append(token.text)
            resultado['pos_tags'].append({
                'texto': token.text,
                'pos': token.pos_,
                'tag': token.tag_,
                'dep': token.dep_
            })
        
        # Buscar el verbo principal
        verbo_principal = None
        for token in doc:
            if token.pos_ == "VERB" and token.dep_ == "ROOT":
                verbo_principal = token
                resultado['verbo'] = token.text
                break
        
        # Si no hay verbo principal, buscar cualquier verbo
        if not verbo_principal:
            for token in doc:
                if token.pos_ == "VERB":
                    verbo_principal = token
                    resultado['verbo'] = token.text
                    break
        
        # Si aún no hay verbo, buscar el ROOT (puede ser un verbo mal etiquetado)
        # Esto es común con verbos conjugados en primera persona
        if not verbo_principal:
            for token in doc:
                if token.dep_ == "ROOT":
                    # Verificar si tiene un sujeto como hijo (indicador de verbo)
                    tiene_sujeto = any(child.dep_ in ["nsubj", "nsubjpass"] for child in token.children)
                    if tiene_sujeto:
                        verbo_principal = token
                        resultado['verbo'] = token.text
                        break
        
        if verbo_principal:
            # Buscar el sujeto
            sujeto_tokens = []
            for token in doc:
                if token.dep_ in ["nsubj", "nsubjpass"] and token.head == verbo_principal:
                    # Obtener el sujeto y sus modificadores
                    sujeto_tokens = self._obtener_frase(token)
                    break
            
            # Si no se encontró sujeto explícito, buscar pronombres antes del verbo
            if not sujeto_tokens:
                for token in doc:
                    if token.pos_ == "PRON" and token.i < verbo_principal.i:
                        sujeto_tokens = [token]
                        break
            
            if sujeto_tokens:
                resultado['sujeto'] = " ".join([t.text for t in sujeto_tokens])
            
            # Buscar el predicado (verbo + complementos)
            predicado_tokens = []
            
            # Agregar el verbo
            predicado_tokens.append(verbo_principal)
            
            # Agregar complementos del verbo
            for token in doc:
                if token.head == verbo_principal and token.dep_ not in ["nsubj", "nsubjpass", "punct"]:
                    predicado_tokens.extend(self._obtener_frase(token))
            
            # Ordenar por posición en la oración
            predicado_tokens = sorted(set(predicado_tokens), key=lambda t: t.i)
            
            if predicado_tokens:
                resultado['predicado'] = " ".join([t.text for t in predicado_tokens])
            
            # La oración es válida si tiene sujeto, verbo y predicado
            if resultado['sujeto'] and resultado['verbo'] and resultado['predicado']:
                resultado['valida'] = True
            # También es válida si tiene al menos verbo (oraciones imperativas)
            elif resultado['verbo']:
                resultado['valida'] = True
        
        return resultado
    
    def _obtener_frase(self, token) -> List:
        """
        Obtiene un token y todos sus dependientes (subtree).
        
        Args:
            token: Token raíz de la frase
            
        Returns:
            Lista de tokens que forman la frase
        """
        return list(token.subtree)
    
    def obtener_estadisticas(self, resultado: Dict) -> str:
        """
        Genera un reporte textual de las estadísticas del análisis.
        
        Args:
            resultado: Diccionario con el resultado del análisis
            
        Returns:
            String con las estadísticas formateadas
        """
        texto = "\n" + "="*60 + "\n"
        texto += "ANÁLISIS DETALLADO DE LA ORACIÓN\n"
        texto += "="*60 + "\n\n"
        
        texto += f"Tokens identificados: {len(resultado['tokens'])}\n"
        texto += f"Oración válida: {'SÍ ✓' if resultado['valida'] else 'NO ✗'}\n\n"
        
        if resultado['sujeto']:
            texto += f"Sujeto: {resultado['sujeto']}\n"
        else:
            texto += "Sujeto: (no identificado)\n"
        
        if resultado['verbo']:
            texto += f"Verbo: {resultado['verbo']}\n"
        else:
            texto += "Verbo: (no identificado)\n"
        
        if resultado['predicado']:
            texto += f"Predicado: {resultado['predicado']}\n"
        else:
            texto += "Predicado: (no identificado)\n"
        
        texto += "\n" + "-"*60 + "\n"
        texto += "ETIQUETAS POS (Part-of-Speech):\n"
        texto += "-"*60 + "\n"
        
        for item in resultado['pos_tags']:
            texto += f"  '{item['texto']}' → POS: {item['pos']}, DEP: {item['dep']}\n"
        
        texto += "\n" + "="*60 + "\n"
        
        return texto
