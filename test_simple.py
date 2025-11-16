"""Test simple para una sola oración"""
from analizador_oraciones import AnalizadorOraciones

analizador = AnalizadorOraciones()
resultado = analizador.analizar_oracion("yo camino por el parque")

print(f"Válida: {resultado['valida']}")
print(f"Sujeto: {resultado['sujeto']}")
print(f"Verbo: {resultado['verbo']}")
print(f"Predicado: {resultado['predicado']}")
