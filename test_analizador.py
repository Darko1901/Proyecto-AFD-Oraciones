"""
Script de prueba para el Analizador de Oraciones
Prueba automáticamente varias oraciones de ejemplo
"""

from primer_AFD import AFDOraciones


def test_oraciones():
    """Prueba el analizador con varias oraciones de ejemplo."""
    
    afd = AFDOraciones()
    
    # Conjunto de oraciones de prueba
    oraciones_prueba = [
        "yo camino por el parque",
        "el gato come pescado",
        "María estudia matemáticas",
        "los niños juegan en el jardín",
        "mi hermano lee un libro",
        "el perro corre rápidamente",
        "por el parque",  # Inválida
        "camino parque",  # Inválida
    ]
    
    print("\n" + "╔"+"═"*68+"╗")
    print("║" + " "*18 + "PRUEBA AUTOMÁTICA DEL AFD" + " "*25 + "║")
    print("╚"+"═"*68+"╝")
    
    resultados = []
    
    for i, oracion in enumerate(oraciones_prueba, 1):
        print(f"\n\n{'='*70}")
        print(f"PRUEBA {i}/{len(oraciones_prueba)}")
        print('='*70)
        
        resultado = afd.procesar_oracion(oracion)
        resultados.append({
            'oracion': oracion,
            'aceptada': resultado['aceptada'],
            'sujeto': resultado['analisis_nlp']['sujeto'],
            'verbo': resultado['analisis_nlp']['verbo'],
            'predicado': resultado['analisis_nlp']['predicado']
        })
    
    # Resumen final
    print("\n\n" + "╔"+"═"*68+"╗")
    print("║" + " "*23 + "RESUMEN DE PRUEBAS" + " "*27 + "║")
    print("╚"+"═"*68+"╝\n")
    
    aceptadas = sum(1 for r in resultados if r['aceptada'])
    rechazadas = len(resultados) - aceptadas
    
    print(f"Total de oraciones probadas: {len(resultados)}")
    print(f"✓ Aceptadas: {aceptadas}")
    print(f"✗ Rechazadas: {rechazadas}")
    
    print("\n" + "-"*70)
    print("DETALLE DE RESULTADOS:")
    print("-"*70)
    
    for i, r in enumerate(resultados, 1):
        estado = "✓" if r['aceptada'] else "✗"
        print(f"\n{i}. {estado} '{r['oracion']}'")
        if r['aceptada']:
            print(f"   Sujeto: {r['sujeto']}")
            print(f"   Verbo: {r['verbo']}")
            print(f"   Predicado: {r['predicado']}")
    
    print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    try:
        test_oraciones()
    except Exception as e:
        print(f"\nError durante las pruebas: {e}\n")
        import traceback
        traceback.print_exc()
