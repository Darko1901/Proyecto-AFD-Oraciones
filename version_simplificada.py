"""
VERSIÓN SIMPLIFICADA DEL ANALIZADOR DE ORACIONES
Proyecto 5: Analizador de lenguaje natural simple

Este archivo es una versión alternativa más simple que usa regex
en lugar de spaCy. NO reemplaza tu código actual, solo es un ejemplo
de comparación.

Características:
- ~200 líneas vs ~1000+ de la versión completa
- Sin dependencias externas (no requiere spaCy)
- Alfabeto limitado (vocabulario predefinido)
- AFD explícito con tabla de transiciones
- Árbol de derivación en formato ASCII
- Gramática formal simple
"""

import re
from datetime import datetime


class AnalizadorSimple:
    """
    Analizador simple basado en diccionarios de palabras.
    Usa un alfabeto limitado para demostrar el concepto de lenguaje formal.
    """

    def __init__(self):
        # ALFABETO DEL LENGUAJE (vocabulario limitado)
        self.determinantes = ['el', 'la', 'un', 'una', 'los', 'las', 'mi', 'tu']
        self.sustantivos = ['gato', 'perro', 'niño', 'niña', 'libro', 'parque',
                           'pescado', 'jardín', 'casa', 'María', 'Juan', 'hermano',
                           'matemáticas', 'niños']
        self.verbos = ['come', 'corre', 'estudia', 'lee', 'camino', 'juega',
                      'juegan', 'escribe', 'canta']
        self.pronombres = ['yo', 'tú', 'él', 'ella', 'nosotros']
        self.preposiciones = ['por', 'en', 'de', 'con', 'a']
        self.adverbios = ['rápidamente', 'bien', 'mal', 'rápido']

    def analizar_oracion(self, oracion: str) -> dict:
        """
        Analiza una oración simple y extrae sus componentes.

        Gramática reconocida:
        S  → SN SV
        SN → DET N | PRON | N
        SV → V SN | V SP | V
        SP → PREP SN
        """
        palabras = oracion.lower().strip().split()

        resultado = {
            'valida': False,
            'sujeto': None,
            'verbo': None,
            'predicado': None,
            'estructura': []
        }

        if len(palabras) == 0:
            return resultado

        i = 0

        # PASO 1: Identificar SUJETO (SN)
        sujeto_palabras = []

        # Opción 1: DET + N (ej: "el gato")
        if i < len(palabras) and palabras[i] in self.determinantes:
            sujeto_palabras.append(palabras[i])
            resultado['estructura'].append(('DET', palabras[i]))
            i += 1

            if i < len(palabras) and palabras[i] in self.sustantivos:
                sujeto_palabras.append(palabras[i])
                resultado['estructura'].append(('N', palabras[i]))
                i += 1

        # Opción 2: PRON (ej: "yo")
        elif i < len(palabras) and palabras[i] in self.pronombres:
            sujeto_palabras.append(palabras[i])
            resultado['estructura'].append(('PRON', palabras[i]))
            i += 1

        # Opción 3: N solo (ej: "María")
        elif i < len(palabras) and palabras[i] in self.sustantivos:
            sujeto_palabras.append(palabras[i])
            resultado['estructura'].append(('N', palabras[i]))
            i += 1

        if sujeto_palabras:
            resultado['sujeto'] = ' '.join(sujeto_palabras)

        # PASO 2: Identificar VERBO (V)
        if i < len(palabras) and palabras[i] in self.verbos:
            resultado['verbo'] = palabras[i]
            resultado['estructura'].append(('V', palabras[i]))
            predicado_inicio = i
            i += 1

            # PASO 3: Identificar COMPLEMENTO (resto del SV)
            complemento_palabras = [resultado['verbo']]

            # Puede haber preposición + sintagma
            while i < len(palabras):
                palabra = palabras[i]

                if palabra in self.preposiciones:
                    complemento_palabras.append(palabra)
                    resultado['estructura'].append(('PREP', palabra))
                elif palabra in self.determinantes:
                    complemento_palabras.append(palabra)
                    resultado['estructura'].append(('DET', palabra))
                elif palabra in self.sustantivos:
                    complemento_palabras.append(palabra)
                    resultado['estructura'].append(('N', palabra))
                elif palabra in self.adverbios:
                    complemento_palabras.append(palabra)
                    resultado['estructura'].append(('ADV', palabra))
                else:
                    # Palabra no reconocida
                    complemento_palabras.append(palabra)
                    resultado['estructura'].append(('?', palabra))

                i += 1

            resultado['predicado'] = ' '.join(complemento_palabras)

        # Validar: debe tener al menos sujeto y verbo
        if resultado['sujeto'] and resultado['verbo']:
            resultado['valida'] = True

        return resultado


class AFDSimple:
    """
    Autómata Finito Determinista para validar oraciones.

    Estados:
    - q0: Estado inicial
    - q1: Sujeto identificado
    - q2: Verbo identificado
    - q3: Predicado completo (ESTADO DE ACEPTACIÓN)
    - qr: Estado de rechazo

    Transiciones:
    δ(q0, SN) = q1
    δ(q1, V)  = q2
    δ(q2, complemento) = q3
    """

    def __init__(self):
        self.analizador = AnalizadorSimple()

        # Definición formal del AFD
        self.Q = ['q0', 'q1', 'q2', 'q3', 'qr']  # Conjunto de estados
        self.q0 = 'q0'                            # Estado inicial
        self.F = ['q3']                           # Estados de aceptación

        # Tabla de transiciones
        self.delta = {
            ('q0', 'SN'): 'q1',
            ('q1', 'V'):  'q2',
            ('q2', 'COMPLEMENTO'): 'q3',
        }

        self.estado_actual = self.q0
        self.historial = []

    def procesar_oracion(self, oracion: str) -> dict:
        """Procesa una oración a través del AFD."""
        print("\n" + "="*70)
        print("VERSIÓN SIMPLIFICADA - ANALIZADOR DE ORACIONES CON AFD")
        print("="*70)
        print(f"\nOración: '{oracion}'")

        # Resetear autómata
        self.estado_actual = self.q0
        self.historial = [(self.q0, "Estado inicial")]

        # Análisis léxico
        print("\n" + "-"*70)
        print("FASE 1: Análisis léxico")
        print("-"*70)

        resultado = self.analizador.analizar_oracion(oracion)

        if resultado['estructura']:
            print("\nPalabras reconocidas:")
            for categoria, palabra in resultado['estructura']:
                print(f"  '{palabra}' → {categoria}")

        # Transiciones del AFD
        print("\n" + "-"*70)
        print("FASE 2: Transiciones del AFD")
        print("-"*70)

        # q0 → q1 (Sujeto)
        if resultado['sujeto']:
            self._transicion('q1', f"Sujeto identificado: '{resultado['sujeto']}'")
        else:
            self._transicion('qr', "No se identificó sujeto")
            return self._generar_resultado(resultado, False)

        # q1 → q2 (Verbo)
        if resultado['verbo']:
            self._transicion('q2', f"Verbo identificado: '{resultado['verbo']}'")
        else:
            self._transicion('qr', "No se identificó verbo")
            return self._generar_resultado(resultado, False)

        # q2 → q3 (Predicado completo)
        if resultado['predicado']:
            self._transicion('q3', f"Predicado completo: '{resultado['predicado']}'")
        else:
            self._transicion('qr', "No se completó el predicado")
            return self._generar_resultado(resultado, False)

        # Verificar aceptación
        aceptada = self.estado_actual in self.F

        return self._generar_resultado(resultado, aceptada)

    def _transicion(self, nuevo_estado: str, razon: str):
        """Realiza una transición de estado."""
        print(f"\n  {self.estado_actual} → {nuevo_estado}")
        print(f"  Razón: {razon}")
        self.estado_actual = nuevo_estado
        self.historial.append((nuevo_estado, razon))

    def _generar_resultado(self, analisis: dict, aceptada: bool) -> dict:
        """Genera el resultado final."""
        print("\n" + "="*70)
        print("RESULTADO FINAL")
        print("="*70)
        print(f"\nEstado final: {self.estado_actual}")
        print(f"¿Es estado de aceptación?: {'SÍ' if self.estado_actual in self.F else 'NO'}")

        if aceptada:
            print("\n✓ ORACIÓN ACEPTADA")
            print(f"  Sujeto: {analisis['sujeto']}")
            print(f"  Verbo: {analisis['verbo']}")
            print(f"  Predicado: {analisis['predicado']}")

            # Generar árbol de derivación
            print("\n" + "-"*70)
            print("ÁRBOL DE DERIVACIÓN:")
            print("-"*70)
            self._imprimir_arbol_derivacion(analisis)
        else:
            print("\n✗ ORACIÓN RECHAZADA")

        return {
            'aceptada': aceptada,
            'estado_final': self.estado_actual,
            'historial': self.historial,
            'analisis': analisis
        }

    def _imprimir_arbol_derivacion(self, analisis: dict):
        """
        Imprime el árbol de derivación en formato ASCII.

        Gramática:
        S  → SN + SV
        SN → DET + N | PRON | N
        SV → V + complemento
        """
        print("\nS (Oración)")
        print("├── SN (Sintagma Nominal)")

        # Analizar estructura del sujeto
        sujeto_estructura = [e for e in analisis['estructura']
                            if e[1] in analisis['sujeto'].split()]

        for i, (cat, palabra) in enumerate(sujeto_estructura):
            es_ultimo = (i == len(sujeto_estructura) - 1)
            conector = "└──" if es_ultimo else "├──"
            print(f"│   {conector} {cat} → '{palabra}'")

        print("└── SV (Sintagma Verbal)")

        # Analizar estructura del predicado
        predicado_estructura = [e for e in analisis['estructura']
                               if e[1] in analisis['predicado'].split()]

        for i, (cat, palabra) in enumerate(predicado_estructura):
            es_ultimo = (i == len(predicado_estructura) - 1)
            conector = "└──" if es_ultimo else "├──"
            espacios = "    " if es_ultimo else "    "
            print(f"    {conector} {cat} → '{palabra}'")

        # Mostrar reglas aplicadas
        print("\n" + "-"*70)
        print("REGLAS GRAMATICALES APLICADAS:")
        print("-"*70)
        print("1. S → SN + SV")

        # Determinar regla del SN
        if any(e[0] == 'PRON' for e in sujeto_estructura):
            print("2. SN → PRON")
        elif any(e[0] == 'DET' for e in sujeto_estructura):
            print("2. SN → DET + N")
        else:
            print("2. SN → N")

        print("3. SV → V + complemento")


def main():
    """Función principal."""
    print("\n" + "╔"+"═"*68+"╗")
    print("║" + " "*15 + "VERSIÓN SIMPLIFICADA - AFD" + " "*27 + "║")
    print("║" + " "*20 + "Analizador de Oraciones" + " "*25 + "║")
    print("╚"+"═"*68+"╝")

    print("\nCaracterísticas:")
    print("  - Sin dependencias externas (no requiere spaCy)")
    print("  - Vocabulario limitado (alfabeto finito)")
    print("  - AFD explícito con tabla de transiciones")
    print("  - Árbol de derivación ASCII")

    afd = AFDSimple()

    # Mostrar vocabulario disponible
    print("\n" + "-"*70)
    print("VOCABULARIO DISPONIBLE:")
    print("-"*70)
    print(f"Determinantes: {', '.join(afd.analizador.determinantes)}")
    print(f"Sustantivos: {', '.join(afd.analizador.sustantivos)}")
    print(f"Verbos: {', '.join(afd.analizador.verbos)}")
    print(f"Pronombres: {', '.join(afd.analizador.pronombres)}")
    print(f"Preposiciones: {', '.join(afd.analizador.preposiciones)}")

    print("\n" + "-"*70)
    print("EJEMPLOS DE ORACIONES VÁLIDAS:")
    print("-"*70)
    print("  - el gato come pescado")
    print("  - yo camino por el parque")
    print("  - María estudia matemáticas")
    print("  - los niños juegan en el jardín")

    while True:
        print("\n" + "-"*70)
        print("Ingresa una oración para analizar")
        print("(o escribe 'salir' para terminar)")
        print("-"*70)

        oracion = input("\nOración: ").strip()

        if oracion.lower() in ['salir', 'exit', 'quit']:
            print("\nHasta luego!\n")
            break

        if not oracion:
            print("\nPor favor ingresa una oración válida.")
            continue

        # Procesar la oración
        resultado = afd.procesar_oracion(oracion)

        print("\n" + "="*70)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario!\n")
    except Exception as e:
        print(f"\nError: {e}\n")
