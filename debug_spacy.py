"""
Script de debug para analizar cómo spaCy procesa una oración específica
"""

import spacy

nlp = spacy.load("es_core_news_sm")

oracion = "yo camino por el parque"
doc = nlp(oracion)

print(f"\nAnalizando: '{oracion}'\n")
print("="*60)

for token in doc:
    print(f"Texto: {token.text:15} POS: {token.pos_:10} Tag: {token.tag_:10} Dep: {token.dep_:10} Head: {token.head.text}")

print("\n" + "="*60)
print("\nBuscando verbo principal (ROOT):")
for token in doc:
    if token.pos_ == "VERB" and token.dep_ == "ROOT":
        print(f"  Verbo ROOT encontrado: {token.text}")
        
        print(f"\n  Hijos del verbo:")
        for child in token.children:
            print(f"    - {child.text} ({child.pos_}, {child.dep_})")

print("\n" + "="*60)
print("\nBuscando sujetos (nsubj):")
for token in doc:
    if token.dep_ in ["nsubj", "nsubjpass"]:
        print(f"  Sujeto encontrado: {token.text} (head: {token.head.text})")

print("\n" + "="*60)
print("\nBuscando pronombres:")
for token in doc:
    if token.pos_ == "PRON":
        print(f"  Pronombre encontrado: {token.text} (dep: {token.dep_}, head: {token.head.text})")
