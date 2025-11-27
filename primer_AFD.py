"""
Autómata Finito Determinista para Análisis de Oraciones Simples
Versión adaptada para procesar oraciones en español e identificar su estructura.
"""

from analizador_oraciones import AnalizadorOraciones
from visualizador_arbol import VisualizadorArbol
from generador_arbol_derivacion import GeneradorArbolDerivacion


class AFDOraciones:
    """
    Autómata Finito Determinista que analiza oraciones simples en español.
    
    Estados del autómata:
    - q0: Estado inicial (esperando entrada)
    - q1: Sujeto identificado
    - q2: Verbo identificado
    - q3: Predicado identificado (estado de aceptación)
    - qr: Estado de rechazo
    """
    
    def __init__(self):
        self.analizador = AnalizadorOraciones()
        self.visualizador = VisualizadorArbol()
        self.generador_derivacion = GeneradorArbolDerivacion()
        
        # Definición del autómata
        self.estados = ['q0', 'q1', 'q2', 'q3', 'qr']
        self.estado_inicial = 'q0'
        self.estados_aceptacion = ['q3']
        self.estado_actual = self.estado_inicial
        
        # Historial de transiciones
        self.historial = []
    
    def procesar_oracion(self, oracion: str) -> dict:
        """
        Procesa una oración a través del autómata.
        
        Args:
            oracion: La oración a analizar
            
        Returns:
            Diccionario con el resultado del análisis y el estado del autómata
        """
        print("\n" + "="*70)
        print("AUTÓMATA FINITO DETERMINISTA - ANALIZADOR DE ORACIONES")
        print("="*70)
        print(f"\nOración ingresada: '{oracion}'")
        print(f"Estado inicial: {self.estado_inicial}")
        
        # Resetear el autómata
        self.estado_actual = self.estado_inicial
        self.historial = [(self.estado_actual, "Inicio")]
        
        # Analizar la oración con NLP
        print("\n" + "-"*70)
        print("FASE 1: Análisis léxico y sintáctico")
        print("-"*70)
        
        resultado = self.analizador.analizar_oracion(oracion)
        
        # Transiciones del autómata basadas en el análisis
        print("\n" + "-"*70)
        print("FASE 2: Transiciones del autómata")
        print("-"*70)
        
        # Transición q0 -> q1 o q2
        if resultado['sujeto']:
            self._transicion('q1', f"Sujeto encontrado: '{resultado['sujeto']}'")
        elif resultado['verbo']:
            self._transicion('q2', f"Verbo encontrado (sin sujeto explícito): '{resultado['verbo']}'")
        else:
            self._transicion('qr', "No se encontró sujeto ni verbo")
            return self._generar_resultado(resultado, False)
        
        # Transición q1 -> q2
        if self.estado_actual == 'q1':
            if resultado['verbo']:
                self._transicion('q2', f"Verbo encontrado: '{resultado['verbo']}'")
            else:
                self._transicion('qr', "No se encontró verbo después del sujeto")
                return self._generar_resultado(resultado, False)
        
        # Transición q2 -> q3
        if self.estado_actual == 'q2':
            if resultado['predicado']:
                self._transicion('q3', f"Predicado completo: '{resultado['predicado']}'")
            else:
                self._transicion('qr', "No se encontró predicado completo")
                return self._generar_resultado(resultado, False)
        
        # Verificar si llegamos a un estado de aceptación
        aceptada = self.estado_actual in self.estados_aceptacion
        
        return self._generar_resultado(resultado, aceptada)
    
    def _transicion(self, nuevo_estado: str, razon: str):
        """Realiza una transición de estado."""
        print(f"\n  {self.estado_actual} → {nuevo_estado}")
        print(f"  Razón: {razon}")
        self.estado_actual = nuevo_estado
        self.historial.append((nuevo_estado, razon))
    
    def _generar_resultado(self, resultado_nlp: dict, aceptada: bool) -> dict:
        """Genera el resultado final del autómata."""
        print("\n" + "="*70)
        print("RESULTADO FINAL DEL AUTÓMATA")
        print("="*70)
        print(f"\nEstado final: {self.estado_actual}")
        print(f"¿Estado de aceptación?: {'SÍ' if self.estado_actual in self.estados_aceptacion else 'NO'}")
        
        if aceptada and resultado_nlp['valida']:
            print("\n✓ ORACIÓN ACEPTADA")
            print("  La oración tiene una estructura gramatical válida.")
        else:
            print("\n✗ ORACIÓN RECHAZADA")
            print("  La oración no cumple con la estructura esperada.")
        
        # Mostrar componentes identificados
        print("\n" + "-"*70)
        print("COMPONENTES IDENTIFICADOS:")
        print("-"*70)
        print(f"Sujeto:    {resultado_nlp['sujeto'] if resultado_nlp['sujeto'] else '(no identificado)'}")
        print(f"Verbo:     {resultado_nlp['verbo'] if resultado_nlp['verbo'] else '(no identificado)'}")
        print(f"Predicado: {resultado_nlp['predicado'] if resultado_nlp['predicado'] else '(no identificado)'}")
        
        # Generar árboles si la oración fue aceptada
        ruta_arbol_sintactico = None
        ruta_arbol_derivacion = None
        arbol_derivacion = None
        
        if aceptada and resultado_nlp['valida']:
            print("\n" + "-"*70)
            print("GENERANDO ÁRBOLES...")
            print("-"*70)
            
            # 1. Generar árbol sintáctico
            try:
                ruta_arbol_sintactico = self.visualizador.generar_arbol(
                    resultado_nlp['doc'], 
                    resultado_nlp['doc'].text
                )
                print(f"✓ Árbol sintáctico generado: {ruta_arbol_sintactico}")
            except Exception as e:
                print(f"  Error al generar árbol sintáctico: {e}")
            
            # 2. Generar árbol de derivación
            try:
                arbol_derivacion = self.generador_derivacion.generar_arbol(
                    resultado_nlp['doc'],
                    resultado_nlp
                )
                ruta_arbol_derivacion = self.visualizador.generar_arbol_derivacion(
                    arbol_derivacion,
                    resultado_nlp['doc'].text
                )
                print(f"✓ Árbol de derivación generado: {ruta_arbol_derivacion}")
                
                # Mostrar reglas aplicadas
                reglas = self.generador_derivacion.obtener_reglas_aplicadas(arbol_derivacion)
                if reglas:
                    print(f"\nReglas gramaticales aplicadas:")
                    for i, regla in enumerate(reglas, 1):
                        print(f"   {i}. {regla}")
                
            except Exception as e:
                print(f"Error al generar árbol de derivación: {e}")
                import traceback
                traceback.print_exc()
        
        return {
            'aceptada': aceptada,
            'estado_final': self.estado_actual,
            'historial': self.historial,
            'analisis_nlp': resultado_nlp,
            'ruta_arbol_sintactico': ruta_arbol_sintactico,
            'ruta_arbol_derivacion': ruta_arbol_derivacion,
            'arbol_derivacion': arbol_derivacion
        }
    
    def mostrar_analisis_detallado(self, resultado: dict):
        """Muestra un análisis detallado de la oración."""
        print(self.analizador.obtener_estadisticas(resultado['analisis_nlp']))
        
        # Mostrar árbol de derivación en ASCII
        if resultado.get('arbol_derivacion'):
            print("\n" + "="*70)
            print("ÁRBOL DE DERIVACIÓN (Formato ASCII):")
            print("="*70 + "\n")
            self.generador_derivacion.imprimir_arbol(resultado['arbol_derivacion'])
    
    def mostrar_analisis_detallado_old(self, resultado: dict):
        """Muestra un análisis detallado de la oración."""
        print(self.analizador.obtener_estadisticas(resultado['analisis_nlp']))


def main():
    """Función principal del programa."""
    print("\n" + "╔"+"═"*68+"╗")
    print("║" + " "*15 + "ANALIZADOR DE ORACIONES SIMPLES" + " "*22 + "║")
    print("║" + " "*20 + "Autómata Finito Determinista" + " "*20 + "║")
    print("╚"+"═"*68+"╝")
    
    afd = AFDOraciones()
    
    while True:
        print("\n" + "-"*70)
        print("Ingresa una oración en español para analizar")
        print("(o escribe 'salir' para terminar)")
        print("-"*70)
        
        oracion = input("\nOración: ").strip()
        
        if oracion.lower() in ['salir', 'exit', 'quit']:
            print("\n¡Hasta luego! \n")
            break
        
        if not oracion:
            print("\n Por favor ingresa una oración válida.")
            continue
        
        # Procesar la oración
        resultado = afd.procesar_oracion(oracion)
        
        # Si se generaron árboles, preguntar si desea abrirlos
        if resultado.get('ruta_arbol_sintactico') or resultado.get('ruta_arbol_derivacion'):
            print("\n" + "-"*70)
            print("VISUALIZACIÓN DE ÁRBOLES")
            print("-"*70)
            
            if resultado.get('ruta_arbol_sintactico'):
                respuesta = input("\n¿Deseas abrir el árbol sintáctico? (s/n): ").strip().lower()
                if respuesta == 's':
                    print(" Abriendo árbol sintáctico...")
                    afd.visualizador.abrir_imagen(resultado['ruta_arbol_sintactico'])
            
            if resultado.get('ruta_arbol_derivacion'):
                respuesta = input("\n¿Deseas abrir el árbol de derivación? (s/n): ").strip().lower()
                if respuesta == 's':
                    print(" Abriendo árbol de derivación...")
                    afd.visualizador.abrir_imagen(resultado['ruta_arbol_derivacion'])
        
        # Preguntar si desea ver análisis detallado
        print("\n" + "-"*70)
        respuesta = input("¿Deseas ver el análisis detallado (con árbol ASCII)? (s/n): ").strip().lower()
        
        if respuesta == 's':
            afd.mostrar_analisis_detallado(resultado)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n¡Programa interrumpido por el usuario!\n")
    except Exception as e:
        print(f"\n Error: {e}\n")

