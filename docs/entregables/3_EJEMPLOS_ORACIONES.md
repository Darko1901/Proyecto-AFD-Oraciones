# ENTREGABLE 3: Ejemplos de Oraciones Válidas e Inválidas

**Proyecto:** Analizador de Lenguaje Natural Simple
**Autores:** Ricardo Méndez, Emiliano Ledesma
**Fecha:** Noviembre 2024

---

## Introducción

Este documento presenta una colección exhaustiva de ejemplos de oraciones procesadas por el analizador, clasificadas en válidas e inválidas. Cada ejemplo incluye el análisis detallado y la explicación del resultado.

---

## PARTE 1: ORACIONES VÁLIDAS

Las siguientes oraciones cumplen con la gramática definida y son aceptadas por el autómata.

---

### Categoría A: Oraciones con Determinante + Sustantivo

#### Ejemplo A1: "el gato come pescado"

**Análisis:**
- Sujeto: el gato (DET + N)
- Verbo: come
- Predicado: come pescado
- Estructura: DET N V N

**Validación AFD:**
```
q0 → q1 (Sujeto identificado: 'el gato')
q1 → q2 (Verbo identificado: 'come')
q2 → q3 (Predicado completo: 'come pescado')
Estado final: q3 (ACEPTACIÓN)
```

**Reglas gramaticales aplicadas:**
1. S → SN + SV
2. SN → DET + N
3. SV → V + SN
4. SN → N

**Resultado:** VÁLIDA

---

#### Ejemplo A2: "la niña lee un libro"

**Análisis:**
- Sujeto: la niña (DET + N)
- Verbo: lee
- Predicado: lee un libro
- Estructura: DET N V DET N

**Validación AFD:**
```
q0 → q1 (Sujeto identificado: 'la niña')
q1 → q2 (Verbo identificado: 'lee')
q2 → q3 (Predicado completo: 'lee un libro')
Estado final: q3 (ACEPTACIÓN)
```

**Reglas aplicadas:**
1. S → SN + SV
2. SN → DET + N
3. SV → V + SN
4. SN → DET + N

**Resultado:** VÁLIDA

---

#### Ejemplo A3: "los niños juegan en el jardín"

**Análisis:**
- Sujeto: los niños (DET + N)
- Verbo: juegan
- Predicado: juegan en el jardín
- Estructura: DET N V PREP DET N

**Validación AFD:**
```
q0 → q1 (Sujeto identificado: 'los niños')
q1 → q2 (Verbo identificado: 'juegan')
q2 → q3 (Predicado completo: 'juegan en el jardín')
Estado final: q3 (ACEPTACIÓN)
```

**Reglas aplicadas:**
1. S → SN + SV
2. SN → DET + N
3. SV → V + SP
4. SP → PREP + SN
5. SN → DET + N

**Resultado:** VÁLIDA

---

### Categoría B: Oraciones con Pronombres

#### Ejemplo B1: "yo camino por el parque"

**Análisis:**
- Sujeto: yo (PRON)
- Verbo: camino
- Predicado: camino por el parque
- Estructura: PRON V PREP DET N

**Validación AFD:**
```
q0 → q1 (Sujeto identificado: 'yo')
q1 → q2 (Verbo identificado: 'camino')
q2 → q3 (Predicado completo: 'camino por el parque')
Estado final: q3 (ACEPTACIÓN)
```

**Reglas aplicadas:**
1. S → SN + SV
2. SN → PRON
3. SV → V + SP
4. SP → PREP + SN
5. SN → DET + N

**Resultado:** VÁLIDA

---

#### Ejemplo B2: "tú estudia matemáticas"

**Nota:** Aunque existe discordancia de número (tú + estudia), el analizador solo valida estructura sintáctica, no concordancia gramatical.

**Análisis:**
- Sujeto: tú (PRON)
- Verbo: estudia
- Predicado: estudia matemáticas
- Estructura: PRON V N

**Validación AFD:**
```
q0 → q1 (Sujeto identificado: 'tú')
q1 → q2 (Verbo identificado: 'estudia')
q2 → q3 (Predicado completo: 'estudia matemáticas')
Estado final: q3 (ACEPTACIÓN)
```

**Resultado:** VÁLIDA (sintácticamente)

---

#### Ejemplo B3: "ella canta bien"

**Análisis:**
- Sujeto: ella (PRON)
- Verbo: canta
- Predicado: canta bien
- Estructura: PRON V ADV

**Validación AFD:**
```
q0 → q1 (Sujeto identificado: 'ella')
q1 → q2 (Verbo identificado: 'canta')
q2 → q3 (Predicado completo: 'canta bien')
Estado final: q3 (ACEPTACIÓN)
```

**Reglas aplicadas:**
1. S → SN + SV
2. SN → PRON
3. SV → V + ADV

**Resultado:** VÁLIDA

---

### Categoría C: Oraciones con Nombres Propios

#### Ejemplo C1: "María estudia matemáticas"

**Análisis:**
- Sujeto: María (N)
- Verbo: estudia
- Predicado: estudia matemáticas
- Estructura: N V N

**Validación AFD:**
```
q0 → q1 (Sujeto identificado: 'María')
q1 → q2 (Verbo identificado: 'estudia')
q2 → q3 (Predicado completo: 'estudia matemáticas')
Estado final: q3 (ACEPTACIÓN)
```

**Reglas aplicadas:**
1. S → SN + SV
2. SN → N
3. SV → V + SN
4. SN → N

**Resultado:** VÁLIDA

---

#### Ejemplo C2: "Juan lee un libro"

**Análisis:**
- Sujeto: Juan (N)
- Verbo: lee
- Predicado: lee un libro
- Estructura: N V DET N

**Validación AFD:**
```
q0 → q1 (Sujeto identificado: 'Juan')
q1 → q2 (Verbo identificado: 'lee')
q2 → q3 (Predicado completo: 'lee un libro')
Estado final: q3 (ACEPTACIÓN)
```

**Resultado:** VÁLIDA

---

### Categoría D: Oraciones con Adverbios

#### Ejemplo D1: "el perro corre rápidamente"

**Análisis:**
- Sujeto: el perro (DET + N)
- Verbo: corre
- Predicado: corre rápidamente
- Estructura: DET N V ADV

**Validación AFD:**
```
q0 → q1 (Sujeto identificado: 'el perro')
q1 → q2 (Verbo identificado: 'corre')
q2 → q3 (Predicado completo: 'corre rápidamente')
Estado final: q3 (ACEPTACIÓN)
```

**Reglas aplicadas:**
1. S → SN + SV
2. SN → DET + N
3. SV → V + ADV

**Resultado:** VÁLIDA

---

#### Ejemplo D2: "mi hermano escribe bien"

**Análisis:**
- Sujeto: mi hermano (DET + N)
- Verbo: escribe
- Predicado: escribe bien
- Estructura: DET N V ADV

**Validación AFD:**
```
q0 → q1 (Sujeto identificado: 'mi hermano')
q1 → q2 (Verbo identificado: 'escribe')
q2 → q3 (Predicado completo: 'escribe bien')
Estado final: q3 (ACEPTACIÓN)
```

**Resultado:** VÁLIDA

---

### Categoría E: Oraciones con Verbos Intransitivos

#### Ejemplo E1: "los niños juegan"

**Análisis:**
- Sujeto: los niños (DET + N)
- Verbo: juegan
- Predicado: juegan
- Estructura: DET N V

**Validación AFD:**
```
q0 → q1 (Sujeto identificado: 'los niños')
q1 → q2 (Verbo identificado: 'juegan')
q2 → q3 (Predicado completo: 'juegan')
Estado final: q3 (ACEPTACIÓN)
```

**Reglas aplicadas:**
1. S → SN + SV
2. SN → DET + N
3. SV → V

**Resultado:** VÁLIDA

---

#### Ejemplo E2: "el gato corre"

**Análisis:**
- Sujeto: el gato (DET + N)
- Verbo: corre
- Predicado: corre
- Estructura: DET N V

**Validación AFD:**
```
q0 → q1 (Sujeto identificado: 'el gato')
q1 → q2 (Verbo identificado: 'corre')
q2 → q3 (Predicado completo: 'corre')
Estado final: q3 (ACEPTACIÓN)
```

**Resultado:** VÁLIDA

---

## PARTE 2: ORACIONES INVÁLIDAS

Las siguientes oraciones NO cumplen con la gramática y son rechazadas por el autómata.

---

### Categoría X: Sin Sujeto

#### Ejemplo X1: "por el parque"

**Análisis:**
- Sujeto: (no identificado)
- Verbo: (no identificado)
- Estructura: PREP DET N

**Validación AFD:**
```
q0 → qr (No se identificó sujeto)
Estado final: qr (RECHAZO)
```

**Razón de rechazo:** No hay sintagma nominal al inicio. La gramática requiere que toda oración comience con SN.

**Resultado:** INVÁLIDA

---

#### Ejemplo X2: "come pescado"

**Análisis:**
- Sujeto: (no identificado - sujeto tácito no soportado)
- Verbo: come (reconocido)
- Estructura: V N

**Validación AFD:**
```
q0 → qr (No se identificó sujeto explícito)
Estado final: qr (RECHAZO)
```

**Razón de rechazo:** Aunque semánticamente correcta con sujeto tácito, la gramática actual requiere sujeto explícito.

**Resultado:** INVÁLIDA

---

#### Ejemplo X3: "en la casa"

**Análisis:**
- Sujeto: (no identificado)
- Verbo: (no identificado)
- Estructura: PREP DET N

**Validación AFD:**
```
q0 → qr (No se identificó sujeto)
Estado final: qr (RECHAZO)
```

**Razón de rechazo:** Solo sintagma preposicional, sin estructura de oración.

**Resultado:** INVÁLIDA

---

### Categoría Y: Sin Verbo

#### Ejemplo Y1: "el gato pescado"

**Análisis:**
- Sujeto: el gato (DET + N)
- Verbo: (no identificado)
- Estructura: DET N N

**Validación AFD:**
```
q0 → q1 (Sujeto identificado: 'el gato')
q1 → qr (No se identificó verbo)
Estado final: qr (RECHAZO)
```

**Razón de rechazo:** Falta el verbo. La gramática requiere S → SN SV, donde SV debe contener un verbo.

**Resultado:** INVÁLIDA

---

#### Ejemplo Y2: "yo el parque"

**Análisis:**
- Sujeto: yo (PRON)
- Verbo: (no identificado)
- Estructura: PRON DET N

**Validación AFD:**
```
q0 → q1 (Sujeto identificado: 'yo')
q1 → qr (No se identificó verbo)
Estado final: qr (RECHAZO)
```

**Razón de rechazo:** Después del sujeto debe venir un verbo.

**Resultado:** INVÁLIDA

---

#### Ejemplo Y3: "María matemáticas"

**Análisis:**
- Sujeto: María (N)
- Verbo: (no identificado)
- Estructura: N N

**Validación AFD:**
```
q0 → q1 (Sujeto identificado: 'María')
q1 → qr (No se identificó verbo después del sujeto)
Estado final: qr (RECHAZO)
```

**Razón de rechazo:** Estructura incompleta sin verbo.

**Resultado:** INVÁLIDA

---

### Categoría Z: Palabras No Reconocidas

#### Ejemplo Z1: "el dinosaurio come pescado"

**Análisis:**
- Palabras: [el, dinosaurio, come, pescado]
- Categorías: [DET, ?, V, N]
- Problema: "dinosaurio" no está en el vocabulario

**Validación AFD:**
```
Palabras reconocidas:
  'el' → DET
  'dinosaurio' → ? (palabra desconocida)
  'come' → V
  'pescado' → N

q0 → qr (Estructura con palabra no reconocida)
Estado final: qr (RECHAZO)
```

**Razón de rechazo:** La palabra "dinosaurio" no pertenece al alfabeto del lenguaje (vocabulario limitado de 45 palabras).

**Resultado:** INVÁLIDA

---

#### Ejemplo Z2: "yo salto rápido"

**Análisis:**
- Palabras: [yo, salto, rápido]
- Categorías: [PRON, ?, ADV]
- Problema: "salto" no está en la lista de verbos

**Validación AFD:**
```
Palabras reconocidas:
  'yo' → PRON
  'salto' → ? (verbo no reconocido)
  'rápido' → ADV

q0 → q1 (Sujeto identificado: 'yo')
q1 → qr (Verbo no reconocido)
Estado final: qr (RECHAZO)
```

**Razón de rechazo:** "salto" no está en el vocabulario de verbos.

**Resultado:** INVÁLIDA

---

#### Ejemplo Z3: "el elefante camina despacio"

**Análisis:**
- Palabras no reconocidas: "elefante", "despacio"
- Solo reconocidas: "el" (DET), "camina" → ? (no en vocabulario)

**Validación AFD:**
```
q0 → qr (Múltiples palabras no reconocidas)
Estado final: qr (RECHAZO)
```

**Razón de rechazo:** Vocabulario fuera del alfabeto del lenguaje.

**Resultado:** INVÁLIDA

---

### Categoría W: Estructura Incorrecta

#### Ejemplo W1: "come el gato pescado"

**Análisis:**
- Orden: V DET N N
- Problema: Verbo antes del sujeto

**Validación AFD:**
```
q0 → qr (Estructura incorrecta: verbo al inicio)
Estado final: qr (RECHAZO)
```

**Razón de rechazo:** La gramática no permite inicio con verbo. S → SN SV requiere SN primero.

**Resultado:** INVÁLIDA

---

#### Ejemplo W2: "el parque yo camino"

**Análisis:**
- Estructura: DET N PRON V
- Problema: Dos posibles sujetos

**Validación AFD:**
```
q0 → q1 (Sujeto identificado: 'el parque')
q1 → qr (Segundo elemento no es verbo)
Estado final: qr (RECHAZO)
```

**Razón de rechazo:** Después de identificar el sujeto, se espera un verbo, no otro SN.

**Resultado:** INVÁLIDA

---

### Categoría V: Oraciones Vacías o Incompletas

#### Ejemplo V1: "" (cadena vacía)

**Análisis:**
- Palabras: []
- Estructura: vacía

**Validación AFD:**
```
q0 → qr (Sin entrada)
Estado final: qr (RECHAZO)
```

**Razón de rechazo:** No hay palabras para analizar.

**Resultado:** INVÁLIDA

---

#### Ejemplo V2: "el"

**Análisis:**
- Palabras: [el]
- Estructura: DET (incompleta)

**Validación AFD:**
```
q0 → qr (Sujeto incompleto)
Estado final: qr (RECHAZO)
```

**Razón de rechazo:** Solo determinante, falta sustantivo y resto de la oración.

**Resultado:** INVÁLIDA

---

#### Ejemplo V3: "el gato"

**Análisis:**
- Sujeto: el gato (DET + N)
- Verbo: (ausente)
- Estructura: DET N

**Validación AFD:**
```
q0 → q1 (Sujeto identificado: 'el gato')
q1 → qr (Fin de cadena sin verbo)
Estado final: qr (RECHAZO)
```

**Razón de rechazo:** Oración incompleta, falta el predicado.

**Resultado:** INVÁLIDA

---

## PARTE 3: TABLA RESUMEN

### Resumen de Oraciones Válidas

| ID | Oración | Estructura | Tipo |
|----|---------|------------|------|
| A1 | el gato come pescado | DET N V N | Con objeto directo |
| A2 | la niña lee un libro | DET N V DET N | Con objeto directo |
| A3 | los niños juegan en el jardín | DET N V PREP DET N | Con complemento |
| B1 | yo camino por el parque | PRON V PREP DET N | Pronominal + complemento |
| B2 | tú estudia matemáticas | PRON V N | Pronominal |
| B3 | ella canta bien | PRON V ADV | Con adverbio |
| C1 | María estudia matemáticas | N V N | Nombre propio |
| C2 | Juan lee un libro | N V DET N | Nombre propio |
| D1 | el perro corre rápidamente | DET N V ADV | Con adverbio |
| D2 | mi hermano escribe bien | DET N V ADV | Con adverbio |
| E1 | los niños juegan | DET N V | Intransitivo |
| E2 | el gato corre | DET N V | Intransitivo |

**Total de oraciones válidas:** 12

---

### Resumen de Oraciones Inválidas

| ID | Oración | Razón de Rechazo | Categoría |
|----|---------|------------------|-----------|
| X1 | por el parque | Sin sujeto | Estructura incompleta |
| X2 | come pescado | Sin sujeto explícito | Estructura incompleta |
| X3 | en la casa | Sin sujeto ni verbo | Estructura incompleta |
| Y1 | el gato pescado | Sin verbo | Estructura incompleta |
| Y2 | yo el parque | Sin verbo | Estructura incompleta |
| Y3 | María matemáticas | Sin verbo | Estructura incompleta |
| Z1 | el dinosaurio come pescado | Palabra no reconocida | Vocabulario |
| Z2 | yo salto rápido | Verbo no reconocido | Vocabulario |
| Z3 | el elefante camina despacio | Palabras no reconocidas | Vocabulario |
| W1 | come el gato pescado | Orden incorrecto | Estructura |
| W2 | el parque yo camino | Estructura incorrecta | Estructura |
| V1 | (vacía) | Sin palabras | Vacía |
| V2 | el | Incompleta | Estructura |
| V3 | el gato | Incompleta | Estructura |

**Total de oraciones inválidas:** 14

---

## PARTE 4: ANÁLISIS ESTADÍSTICO

### Distribución por Tipo de Estructura (Oraciones Válidas)

| Estructura | Cantidad | Porcentaje |
|------------|----------|------------|
| SN → DET N | 7 | 58.3% |
| SN → PRON | 3 | 25.0% |
| SN → N | 2 | 16.7% |

### Distribución de Complementos (Oraciones Válidas)

| Tipo de Complemento | Cantidad | Porcentaje |
|---------------------|----------|------------|
| Con objeto directo (SN) | 5 | 41.7% |
| Con sintagma preposicional (SP) | 2 | 16.7% |
| Con adverbio (ADV) | 3 | 25.0% |
| Sin complemento (V solo) | 2 | 16.7% |

### Razones de Rechazo (Oraciones Inválidas)

| Razón | Cantidad | Porcentaje |
|-------|----------|------------|
| Sin sujeto | 3 | 21.4% |
| Sin verbo | 3 | 21.4% |
| Vocabulario no reconocido | 3 | 21.4% |
| Estructura incorrecta | 2 | 14.3% |
| Oración incompleta | 3 | 21.4% |

---

## PARTE 5: CONCLUSIONES

### Patrones Identificados en Oraciones Válidas

1. **Presencia obligatoria de sujeto y verbo:** Todas las oraciones válidas tienen ambos componentes
2. **Flexibilidad en complementos:** El predicado puede tener diferentes tipos de complementos
3. **Variedad de sujetos:** DET+N, PRON, o N funcionan correctamente
4. **Orden SVO:** Todas mantienen el orden Sujeto-Verbo-Objeto/Complemento

### Patrones Identificados en Oraciones Inválidas

1. **Estructura incompleta (50%):** La mayoría de rechazos por falta de componentes
2. **Vocabulario limitado (21.4%):** El alfabeto finito causa rechazos de palabras válidas en español
3. **Orden estricto:** No se permite variación en el orden de componentes

### Limitaciones del Sistema

1. No reconoce sujeto tácito (común en español)
2. Vocabulario limitado a 45 palabras
3. No valida concordancia gramatical (número, género)
4. No soporta oraciones complejas o compuestas

### Fortalezas del Sistema

1. Validación sintáctica correcta para oraciones simples
2. Feedback claro sobre razones de rechazo
3. Reconocimiento determinista (sin ambigüedad)
4. Base sólida para extensiones futuras

---

**Fin del Documento: Ejemplos de Oraciones**
