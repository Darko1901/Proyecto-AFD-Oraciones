"""
Diagrama visual del Autómata Finito Determinista
Muestra el flujo de estados y transiciones
"""

def imprimir_diagrama():
    print("\n" + "="*80)
    print(" "*25 + "DIAGRAMA DEL AUTÓMATA")
    print("="*80 + "\n")
    
    print("                              ┌─────────────┐")
    print("                              │     q0      │")
    print("                              │   INICIO    │")
    print("                              └──────┬──────┘")
    print("                                     │")
    print("                    ┌────────────────┴────────────────┐")
    print("                    │                                 │")
    print("              [Sujeto encontrado]            [Verbo sin sujeto]")
    print("                    │                                 │")
    print("                    ▼                                 ▼")
    print("           ┌─────────────┐                   ┌─────────────┐")
    print("           │     q1      │                   │     q2      │")
    print("           │   SUJETO    │──[Verbo found]──▶ │    VERBO    │")
    print("           └─────────────┘                   └──────┬──────┘")
    print("                                                    │")
    print("                                          [Predicado completo]")
    print("                                                    │")
    print("                                                    ▼")
    print("                                           ┌─────────────┐")
    print("                                           │     q3      │")
    print("                                           │ ✓ ACEPTADO  │")
    print("                                           └─────────────┘")
    print()
    print("                            ┌─────────────┐")
    print("                            │     qr      │")
    print("                            │ ✗ RECHAZADO │")
    print("                            └─────────────┘")
    print("                                   ▲")
    print("                                   │")
    print("                    [Cualquier error en el análisis]")
    print()
    print("="*80)
    
    print("\n" + "─"*80)
    print("EJEMPLOS DE TRANSICIONES:")
    print("─"*80 + "\n")
    
    ejemplos = [
        {
            'oracion': 'yo camino por el parque',
            'pasos': [
                'q0 → q1: Sujeto "yo" identificado',
                'q1 → q2: Verbo "camino" identificado',
                'q2 → q3: Predicado completo "yo camino por el parque"',
                '✓ ACEPTADO (estado q3)'
            ]
        },
        {
            'oracion': 'el gato come pescado',
            'pasos': [
                'q0 → q1: Sujeto "el gato" identificado',
                'q1 → q2: Verbo "come" identificado',
                'q2 → q3: Predicado completo "el gato come pescado"',
                '✓ ACEPTADO (estado q3)'
            ]
        },
        {
            'oracion': 'por el parque',
            'pasos': [
                'q0 → qr: No se encontró sujeto ni verbo',
                '✗ RECHAZADO (estado qr)'
            ]
        }
    ]
    
    for i, ejemplo in enumerate(ejemplos, 1):
        print(f"{i}. Oración: '{ejemplo['oracion']}'")
        for paso in ejemplo['pasos']:
            print(f"   {paso}")
        print()
    
    print("="*80 + "\n")


if __name__ == "__main__":
    imprimir_diagrama()
