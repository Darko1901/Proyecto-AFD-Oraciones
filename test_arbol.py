"""
Script de prueba para verificar la generación de árboles sintácticos y de derivación
"""

from analizador_oraciones import AnalizadorOraciones
from visualizador_arbol import VisualizadorArbol
from generador_arbol_derivacion import GeneradorArbolDerivacion

# Inicializar componentes
analizador = AnalizadorOraciones()
visualizador = VisualizadorArbol()
generador_derivacion = GeneradorArbolDerivacion()

# Oración de prueba
oracion = "el gato come pescado"

print(f"Analizando: '{oracion}'")
print("="*60)

# Analizar
resultado = analizador.analizar_oracion(oracion)

print(f"\nSujeto: {resultado['sujeto']}")
print(f"Verbo: {resultado['verbo']}")
print(f"Predicado: {resultado['predicado']}")
print(f"Válida: {resultado['valida']}")

if resultado['valida']:
    print("\n" + "="*60)
    print("GENERANDO ÁRBOLES...")
    print("="*60)
    
    try:
        # 1. Generar árbol sintáctico
        print("\n1️⃣  Generando árbol sintáctico...")
        ruta_sintactico = visualizador.generar_arbol(resultado['doc'], oracion)
        print(f"✓ Árbol sintáctico generado: {ruta_sintactico}")
        
        # 2. Generar árbol de derivación
        print("\n2️⃣  Generando árbol de derivación...")
        arbol_derivacion = generador_derivacion.generar_arbol(resultado['doc'], resultado)
        ruta_derivacion = visualizador.generar_arbol_derivacion(arbol_derivacion, oracion)
        print(f"✓ Árbol de derivación generado: {ruta_derivacion}")
        
        # 3. Mostrar reglas aplicadas
        reglas = generador_derivacion.obtener_reglas_aplicadas(arbol_derivacion)
        if reglas:
            print(f"\n📋 Reglas gramaticales aplicadas:")
            for i, regla in enumerate(reglas, 1):
                print(f"   {i}. {regla}")
        
        # 4. Mostrar árbol en formato ASCII
        print("\n" + "="*60)
        print("ÁRBOL DE DERIVACIÓN (Formato ASCII):")
        print("="*60 + "\n")
        generador_derivacion.imprimir_arbol(arbol_derivacion)
        
        # 5. Abrir imágenes
        print("\n" + "="*60)
        print("Abriendo imágenes...")
        print("="*60)
        visualizador.abrir_imagen(ruta_sintactico)
        visualizador.abrir_imagen(ruta_derivacion)
        
        print("\n✓ ¡Prueba completada exitosamente!")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
else:
    print("\n❌ La oración no es válida, no se generarán los árboles.")
