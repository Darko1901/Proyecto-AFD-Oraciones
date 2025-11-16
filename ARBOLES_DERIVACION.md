# 🌳 NUEVA FUNCIONALIDAD: Árboles de Derivación Gramatical

## ✅ ¿Qué se agregó?

Se implementó la **generación automática de árboles de derivación** que muestran las reglas gramaticales aplicadas paso a paso para construir la oración.

## 📚 ¿Qué es un Árbol de Derivación?

Un árbol de derivación muestra cómo una oración se construye aplicando **reglas gramaticales** de forma jerárquica, partiendo de un símbolo inicial (S = Oración) hasta llegar a las palabras terminales.

### Diferencia entre Árbol Sintáctico y Árbol de Derivación

| Característica | Árbol Sintáctico | Árbol de Derivación |
|---|---|---|
| **Objetivo** | Mostrar dependencias entre palabras | Mostrar reglas gramaticales |
| **Nodos** | Palabras individuales | Sintagmas y categorías |
| **Estructura** | Basada en análisis de spaCy | Basada en gramática formal |
| **Información** | POS tags y dependencias | Reglas de producción |

## 📋 Reglas Gramaticales Implementadas

El generador utiliza las siguientes reglas de gramática generativa:

```
S  → SN + SV          (Oración = Sintagma Nominal + Sintagma Verbal)
SN → DET + N          (Sintagma Nominal = Determinante + Nombre)
SN → PRON             (Sintagma Nominal = Pronombre)
SN → N                (Sintagma Nominal = Nombre solo)
SV → V + SN           (Sintagma Verbal = Verbo + Objeto directo)
SV → V + SP           (Sintagma Verbal = Verbo + Sintagma Preposicional)
SV → V + ADV          (Sintagma Verbal = Verbo + Adverbio)
SV → V                (Sintagma Verbal = Verbo solo)
SP → PREP + SN        (Sintagma Preposicional = Preposición + SN)
```

## 🎨 Visualización del Árbol de Derivación

### Características Visuales

- **Nodos cuadrados** (vs. circulares en árbol sintáctico)
- **Colores por tipo de sintagma**:
  - 🔴 Rojo → S (Oración)
  - 🔵 Turquesa → SN (Sintagma Nominal)
  - 🟢 Verde → SV (Sintagma Verbal)
  - 🟣 Rosa → SP (Sintagma Preposicional)
  - 🟡 Beige → Palabras terminales

### Información en los Nodos

- **No terminales**: Símbolos gramaticales (S, SN, SV, etc.)
- **Terminales**: Palabra + símbolo gramatical (ej: "N → 'gato'")

## 🆕 Nuevos Archivos

### 1. `generador_arbol_derivacion.py` ⭐
Módulo completo para generar árboles de derivación:
- Clase `NodoDerivacion`: Representa nodos del árbol
- Clase `GeneradorArbolDerivacion`: Construye el árbol completo
- Métodos para:
  - Generar estructura de derivación
  - Construir sintagmas nominales y verbales
  - Extraer reglas aplicadas
  - Imprimir árbol en formato ASCII

### 2. Métodos Agregados a `visualizador_arbol.py`
- `generar_arbol_derivacion()`: Crea imagen del árbol
- `_obtener_color_no_terminal()`: Asigna colores a sintagmas
- `_calcular_posiciones_jerarquicas_derivacion()`: Layout del árbol
- `_agregar_leyenda_derivacion()`: Leyenda de símbolos

## 🚀 Cómo Usar

### Modo Interactivo

```bash
python primer_AFD.py
```

Cuando ingreses una oración válida:

```
Oración: el gato come pescado

✓ ORACIÓN ACEPTADA

----------------------------------------------------------------------
GENERANDO ÁRBOLES...
----------------------------------------------------------------------
✓ Árbol sintáctico generado: arboles_sintacticos/arbol_20251116_172336.png
✓ Árbol de derivación generado: arboles_sintacticos/derivacion_20251116_172337.png

📋 Reglas gramaticales aplicadas:
   1. S → SN + SV

----------------------------------------------------------------------
VISUALIZACIÓN DE ÁRBOLES
----------------------------------------------------------------------

¿Deseas abrir el árbol sintáctico? (s/n): s
📊 Abriendo árbol sintáctico...

¿Deseas abrir el árbol de derivación? (s/n): s
🌳 Abriendo árbol de derivación...
```

### Modo de Prueba

```bash
python test_arbol.py
```

Este script:
1. Analiza "el gato come pescado"
2. Genera árbol sintáctico
3. Genera árbol de derivación
4. Muestra reglas aplicadas
5. Imprime árbol ASCII
6. Abre ambas imágenes

## 📊 Ejemplo Visual

### Para la oración: "el gato come pescado"

#### Árbol de Derivación:
```
S
├── SN
│   ├── DET → 'el'
│   └── N → 'gato'
└── SV
    ├── V → 'come'
    └── SN
        └── N → 'pescado'
```

#### Reglas Aplicadas:
1. `S → SN + SV`

Esto se traduce en: "La oración se compone de un Sintagma Nominal seguido de un Sintagma Verbal"

## 🎓 Uso Educativo

Los árboles de derivación son especialmente útiles para:

### 1. Estudio de Gramática Generativa
- Visualizar cómo se aplican las reglas
- Entender la estructura jerárquica del lenguaje
- Aprender teoría lingüística formal

### 2. Análisis Sintáctico
- Identificar sintagmas
- Comprender relaciones gramaticales
- Detectar patrones estructurales

### 3. Lingüística Computacional
- Implementar parsers
- Desarrollar gramáticas formales
- Crear analizadores sintácticos

## 📁 Ubicación de Archivos

Ambos tipos de árboles se guardan en la misma carpeta:

```
Proyecto_AFD_Oraciones/
└── arboles_sintacticos/
    ├── arbol_YYYYMMDD_HHMMSS.png      (Árbol Sintáctico)
    └── derivacion_YYYYMMDD_HHMMSS.png  (Árbol de Derivación)
```

## 🔍 Comparación de Salidas

| Aspecto | Árbol Sintáctico | Árbol de Derivación |
|---|---|---|
| **Formato** | Nodos circulares | Nodos cuadrados |
| **Contenido** | Palabras + POS + DEP | Sintagmas + Terminales |
| **Propósito** | Dependencias | Reglas gramaticales |
| **Orientación** | Top-down | Top-down |
| **Etiquetas** | Técnicas (nsubj, obj) | Formales (SN, SV) |

## 🎯 Integración con el AFD

Ambos árboles se generan **simultáneamente** cuando:
1. ✅ La oración es **aceptada** por el autómata (estado q3)
2. ✅ El análisis NLP es **válido**

El programa genera:
- **Árbol sintáctico** → Análisis técnico de spaCy
- **Árbol de derivación** → Estructura gramatical formal
- **Reglas aplicadas** → Lista de producciones usadas
- **Árbol ASCII** → Representación en terminal (opcional)

## ⚙️ Características Técnicas

### Generación del Árbol
- Análisis recursivo de la estructura
- Construcción bottom-up de sintagmas
- Identificación automática de patrones

### Visualización
- Imágenes PNG de 300 DPI
- Layout jerárquico optimizado
- Colores diferenciados por tipo
- Leyenda explicativa incluida

## 💡 Extensiones Futuras

El sistema puede extenderse para soportar:
- Oraciones coordinadas y subordinadas
- Complementos circunstanciales
- Oraciones interrogativas
- Voz pasiva
- Tiempos compuestos

---

**¡Los árboles de derivación están completamente implementados y funcionando!** 🎉

Ahora el programa genera **dos tipos de árboles** para cada oración válida:
1. **Árbol Sintáctico** (dependencias spaCy)
2. **Árbol de Derivación** (reglas gramaticales formales)
