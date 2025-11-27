# ENTREGABLE 2: Árboles de Derivación

**Proyecto:** Analizador de Lenguaje Natural Simple
**Autores:** Ricardo Méndez, Emiliano Ledesma
**Fecha:** Noviembre 2024

---

## Introducción

Este documento presenta los árboles de derivación generados por el analizador para oraciones válidas del mini-lenguaje. Cada árbol muestra la estructura sintáctica de la oración según la gramática formal definida.

---

## Fundamento Teórico

### Definición de Árbol de Derivación

Un árbol de derivación (o árbol sintáctico) es una representación gráfica del proceso de generación de una cadena a partir de una gramática independiente del contexto.

**Propiedades:**
- **Raíz:** El símbolo inicial S
- **Nodos internos:** Símbolos no terminales (S, SN, SV, SP)
- **Hojas:** Símbolos terminales (palabras del vocabulario)
- **Ramas:** Representan la aplicación de una regla de producción

### Notación Utilizada

```
S                    Nodo raíz
├── SN               Rama izquierda
│   ├── DET → 'el'   Hoja con palabra terminal
│   └── N → 'gato'   Hoja con palabra terminal
└── SV               Rama derecha
    ├── V → 'come'
    └── N → 'pescado'
```

---

## Ejemplo 1: Oración con Determinante + Sustantivo

### Oración: "el gato come pescado"

#### Componentes Identificados
- **Sujeto:** el gato
- **Verbo:** come
- **Predicado:** come pescado

#### Árbol de Derivación

```
S (Oración)
├── SN (Sintagma Nominal)
│   ├── DET → 'el'
│   └── N → 'gato'
└── SV (Sintagma Verbal)
    ├── V → 'come'
    └── SN (Sintagma Nominal)
        └── N → 'pescado'
```

#### Reglas Gramaticales Aplicadas

1. S → SN + SV
2. SN → DET + N
3. SV → V + SN
4. SN → N

#### Derivación Paso a Paso

```
Paso 1: S
Paso 2: S ⇒ SN SV                    (Regla 1)
Paso 3: SN SV ⇒ DET N SV             (Regla 2 aplicada a SN)
Paso 4: DET N SV ⇒ el N SV           (Sustitución terminal)
Paso 5: el N SV ⇒ el gato SV         (Sustitución terminal)
Paso 6: el gato SV ⇒ el gato V SN    (Regla 3 aplicada a SV)
Paso 7: el gato V SN ⇒ el gato come SN   (Sustitución terminal)
Paso 8: el gato come SN ⇒ el gato come N (Regla 4 aplicada a SN)
Paso 9: el gato come N ⇒ el gato come pescado (Sustitución terminal)
```

---

## Ejemplo 2: Oración con Pronombre

### Oración: "yo camino por el parque"

#### Componentes Identificados
- **Sujeto:** yo
- **Verbo:** camino
- **Predicado:** camino por el parque

#### Árbol de Derivación

```
S (Oración)
├── SN (Sintagma Nominal)
│   └── PRON → 'yo'
└── SV (Sintagma Verbal)
    ├── V → 'camino'
    └── SP (Sintagma Preposicional)
        ├── PREP → 'por'
        └── SN (Sintagma Nominal)
            ├── DET → 'el'
            └── N → 'parque'
```

#### Reglas Gramaticales Aplicadas

1. S → SN + SV
2. SN → PRON
3. SV → V + SP
4. SP → PREP + SN
5. SN → DET + N

#### Derivación Paso a Paso

```
Paso 1: S
Paso 2: S ⇒ SN SV                           (Regla 1)
Paso 3: SN SV ⇒ PRON SV                     (Regla 2)
Paso 4: PRON SV ⇒ yo SV                     (Sustitución)
Paso 5: yo SV ⇒ yo V SP                     (Regla 3)
Paso 6: yo V SP ⇒ yo camino SP              (Sustitución)
Paso 7: yo camino SP ⇒ yo camino PREP SN    (Regla 4)
Paso 8: yo camino PREP SN ⇒ yo camino por SN    (Sustitución)
Paso 9: yo camino por SN ⇒ yo camino por DET N  (Regla 5)
Paso 10: yo camino por DET N ⇒ yo camino por el N (Sustitución)
Paso 11: yo camino por el N ⇒ yo camino por el parque (Sustitución)
```

---

## Ejemplo 3: Oración con Nombre Propio

### Oración: "María estudia matemáticas"

#### Componentes Identificados
- **Sujeto:** María
- **Verbo:** estudia
- **Predicado:** estudia matemáticas

#### Árbol de Derivación

```
S (Oración)
├── SN (Sintagma Nominal)
│   └── N → 'María'
└── SV (Sintagma Verbal)
    ├── V → 'estudia'
    └── SN (Sintagma Nominal)
        └── N → 'matemáticas'
```

#### Reglas Gramaticales Aplicadas

1. S → SN + SV
2. SN → N
3. SV → V + SN
4. SN → N

#### Derivación Paso a Paso

```
Paso 1: S
Paso 2: S ⇒ SN SV                       (Regla 1)
Paso 3: SN SV ⇒ N SV                    (Regla 2)
Paso 4: N SV ⇒ María SV                 (Sustitución)
Paso 5: María SV ⇒ María V SN           (Regla 3)
Paso 6: María V SN ⇒ María estudia SN   (Sustitución)
Paso 7: María estudia SN ⇒ María estudia N  (Regla 4)
Paso 8: María estudia N ⇒ María estudia matemáticas (Sustitución)
```

---

## Ejemplo 4: Oración con Adverbio

### Oración: "el perro corre rápidamente"

#### Componentes Identificados
- **Sujeto:** el perro
- **Verbo:** corre
- **Predicado:** corre rápidamente

#### Árbol de Derivación

```
S (Oración)
├── SN (Sintagma Nominal)
│   ├── DET → 'el'
│   └── N → 'perro'
└── SV (Sintagma Verbal)
    ├── V → 'corre'
    └── ADV → 'rápidamente'
```

#### Reglas Gramaticales Aplicadas

1. S → SN + SV
2. SN → DET + N
3. SV → V + ADV

#### Derivación Paso a Paso

```
Paso 1: S
Paso 2: S ⇒ SN SV                       (Regla 1)
Paso 3: SN SV ⇒ DET N SV                (Regla 2)
Paso 4: DET N SV ⇒ el N SV              (Sustitución)
Paso 5: el N SV ⇒ el perro SV           (Sustitución)
Paso 6: el perro SV ⇒ el perro V ADV    (Regla 3)
Paso 7: el perro V ADV ⇒ el perro corre ADV (Sustitución)
Paso 8: el perro corre ADV ⇒ el perro corre rápidamente (Sustitución)
```

---

## Ejemplo 5: Oración con Verbo Intransitivo

### Oración: "los niños juegan"

#### Componentes Identificados
- **Sujeto:** los niños
- **Verbo:** juegan
- **Predicado:** juegan

#### Árbol de Derivación

```
S (Oración)
├── SN (Sintagma Nominal)
│   ├── DET → 'los'
│   └── N → 'niños'
└── SV (Sintagma Verbal)
    └── V → 'juegan'
```

#### Reglas Gramaticales Aplicadas

1. S → SN + SV
2. SN → DET + N
3. SV → V

#### Derivación Paso a Paso

```
Paso 1: S
Paso 2: S ⇒ SN SV                (Regla 1)
Paso 3: SN SV ⇒ DET N SV         (Regla 2)
Paso 4: DET N SV ⇒ los N SV      (Sustitución)
Paso 5: los N SV ⇒ los niños SV  (Sustitución)
Paso 6: los niños SV ⇒ los niños V   (Regla 3)
Paso 7: los niños V ⇒ los niños juegan (Sustitución)
```

---

## Ejemplo 6: Oración con Complemento Preposicional

### Oración: "mi hermano lee en la casa"

#### Componentes Identificados
- **Sujeto:** mi hermano
- **Verbo:** lee
- **Predicado:** lee en la casa

#### Árbol de Derivación

```
S (Oración)
├── SN (Sintagma Nominal)
│   ├── DET → 'mi'
│   └── N → 'hermano'
└── SV (Sintagma Verbal)
    ├── V → 'lee'
    └── SP (Sintagma Preposicional)
        ├── PREP → 'en'
        └── SN (Sintagma Nominal)
            ├── DET → 'la'
            └── N → 'casa'
```

#### Reglas Gramaticales Aplicadas

1. S → SN + SV
2. SN → DET + N
3. SV → V + SP
4. SP → PREP + SN
5. SN → DET + N

---

## Análisis de Complejidad de los Árboles

### Altura del Árbol

La altura de un árbol de derivación es el número máximo de niveles desde la raíz hasta las hojas.

| Oración | Altura | Observación |
|---------|--------|-------------|
| "el gato come pescado" | 4 | Árbol balanceado |
| "yo camino por el parque" | 5 | Mayor profundidad por SP |
| "María estudia matemáticas" | 4 | Estructura simple |
| "el perro corre rápidamente" | 3 | Sin anidamiento profundo |
| "los niños juegan" | 3 | Árbol mínimo |

**Altura promedio:** 3.8 niveles

### Número de Nodos

| Tipo de Nodo | Promedio |
|--------------|----------|
| No terminales | 4.2 |
| Terminales | 4.6 |
| Total | 8.8 |

---

## Representación Visual en el Sistema

El sistema genera estos árboles en dos formatos:

### Formato ASCII (Consola)

Ejemplo de salida del programa:

```
S (Oración)
├── SN (Sintagma Nominal)
│   ├── DET → 'el'
│   └── N → 'gato'
└── SV (Sintagma Verbal)
    ├── V → 'come'
    └── N → 'pescado'
```

### Formato de Reglas Aplicadas

```
REGLAS GRAMATICALES APLICADAS:
1. S → SN + SV
2. SN → DET + N
3. SV → V + complemento
```

---

## Verificación de Unicidad

Cada oración válida del lenguaje tiene un único árbol de derivación, lo que confirma que la gramática es no ambigua.

**Prueba por contradicción:**

Supongamos que existe una oración con dos árboles distintos. Dado que:
1. Solo hay una regla para expandir S (R1: S → SN SV)
2. Las reglas de SN son mutuamente excluyentes (DET N, PRON, o N)
3. Las reglas de SV son mutuamente excluyentes

No es posible construir dos árboles diferentes para la misma oración. Por tanto, la gramática es no ambigua.

---

## Proceso de Construcción de Árboles en el Sistema

### Algoritmo

```
1. Analizar oración léxicamente
   - Tokenizar palabras
   - Identificar categoría gramatical de cada palabra

2. Crear nodo raíz S

3. Identificar sujeto (SN)
   - Si hay DET + N: aplicar regla SN → DET N
   - Si hay PRON: aplicar regla SN → PRON
   - Si hay N solo: aplicar regla SN → N

4. Identificar predicado (SV)
   - Si hay V + SN: aplicar regla SV → V SN
   - Si hay V + SP: aplicar regla SV → V SP
   - Si hay V + ADV: aplicar regla SV → V ADV
   - Si hay V solo: aplicar regla SV → V

5. Si hay SP: aplicar regla SP → PREP SN

6. Retornar árbol completo
```

### Complejidad

- **Temporal:** O(n) donde n es el número de palabras
- **Espacial:** O(n) para almacenar el árbol

---

## Casos Especiales

### Sujeto Tácito (No Soportado)

El sistema actual requiere sujeto explícito. Oraciones como "come pescado" son rechazadas.

**Árbol hipotético con sujeto tácito:**

```
S (Oración)
├── SN (Sintagma Nominal)
│   └── (sujeto tácito)
└── SV (Sintagma Verbal)
    ├── V → 'come'
    └── N → 'pescado'
```

**Estado:** No implementado en versión actual

---

## Exportación de Árboles

El sistema puede mostrar los árboles de las siguientes formas:

1. **En consola (ASCII):** Inmediato durante ejecución
2. **En archivo de texto:** Para documentación
3. **Estructura de datos:** Para procesamiento posterior

---

## Conclusiones

Los árboles de derivación generados por el sistema:

1. Reflejan correctamente la gramática formal definida
2. Son únicos para cada oración (gramática no ambigua)
3. Tienen altura y complejidad razonables (O(n))
4. Son legibles y comprensibles
5. Demuestran la aplicación correcta de las reglas gramaticales

Los árboles sirven como evidencia visual del proceso de análisis sintáctico y validan el correcto funcionamiento del analizador.

---

**Fin del Documento: Árboles de Derivación**
