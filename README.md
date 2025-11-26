# Analizador de Oraciones Simples - AFD

## 📝 Descripción

Este proyecto implementa un **Autómata Finito Determinista (AFD)** que analiza oraciones simples en español e identifica sus componentes gramaticales principales:
- **Sujeto**: Quién realiza la acción
- **Verbo**: La acción que se realiza
- **Predicado**: Lo que se dice del sujeto

El programa utiliza procesamiento de lenguaje natural (NLP) con la biblioteca spaCy para realizar un análisis sintáctico profundo de las oraciones.

## ✨ Características Principales

- 🤖 **Análisis automático** de estructura gramatical
- 🎨 **Generación de árboles sintácticos** visuales (imágenes PNG)
- 📊 **Visualización jerárquica** de dependencias gramaticales
- 🔍 **Análisis detallado** con etiquetas POS (Part-of-Speech)
- 💾 **Guardado automático** de árboles en carpeta dedicada

## 🏗️ Arquitectura del Autómata

### Estados del AFD:
- **q0**: Estado inicial (esperando entrada)
- **q1**: Sujeto identificado
- **q2**: Verbo identificado
- **q3**: Predicado completo identificado ✓ (estado de aceptación)
- **qr**: Estado de rechazo ✗

### Transiciones:
```
q0 → q1: Se identifica un sujeto
q0 → q2: Se identifica un verbo (sin sujeto explícito)
q1 → q2: Se identifica un verbo después del sujeto
q2 → q3: Se completa el predicado
Cualquier estado → qr: Falla en la identificación
```

## 📦 Instalación

### Requisitos Previos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Descargar el modelo de español de spaCy:**
   ```bash
   python -m spacy download es_core_news_sm
   ```

## 🚀 Uso

### Ejecución del Programa

```bash
python primer_AFD.py
```

### Ejemplo de Uso

```
╔════════════════════════════════════════════════════════════════════╗
║               ANALIZADOR DE ORACIONES SIMPLES                      ║
║                    Autómata Finito Determinista                    ║
╚════════════════════════════════════════════════════════════════════╝

----------------------------------------------------------------------
Ingresa una oración en español para analizar
(o escribe 'salir' para terminar)
----------------------------------------------------------------------

Oración: yo camino por el parque

======================================================================
AUTÓMATA FINITO DETERMINISTA - ANALIZADOR DE ORACIONES
======================================================================

Oración ingresada: 'yo camino por el parque'
Estado inicial: q0

----------------------------------------------------------------------
FASE 1: Análisis léxico y sintáctico
----------------------------------------------------------------------

----------------------------------------------------------------------
FASE 2: Transiciones del autómata
----------------------------------------------------------------------

  q0 → q1
  Razón: Sujeto encontrado: 'yo'

  q1 → q2
  Razón: Verbo encontrado: 'camino'

  q2 → q3
  Razón: Predicado completo: 'camino por el parque'

======================================================================
RESULTADO FINAL DEL AUTÓMATA
======================================================================

Estado final: q3
¿Estado de aceptación?: SÍ

✓ ORACIÓN ACEPTADA
  La oración tiene una estructura gramatical válida.

----------------------------------------------------------------------
COMPONENTES IDENTIFICADOS:
----------------------------------------------------------------------
Sujeto:    yo
Verbo:     camino
Predicado: camino por el parque

----------------------------------------------------------------------
GENERANDO ÁRBOL SINTÁCTICO...
----------------------------------------------------------------------
✓ Árbol sintáctico generado: arboles_sintacticos/arbol_20251116_171003.png

----------------------------------------------------------------------
¿Deseas abrir el árbol sintáctico? (s/n): s
```

## 🎨 Árbol Sintáctico

Cuando una oración es **aceptada**, el programa genera automáticamente un **árbol sintáctico visual** en formato PNG que muestra:

- 🔵 Nodos coloreados según la categoría gramatical (POS)
- ➡️ Flechas que indican las dependencias sintácticas
- 🏷️ Etiquetas con el texto, POS tag y tipo de dependencia
- 📊 Estructura jerárquica del árbol de análisis

Las imágenes se guardan en la carpeta `arboles_sintacticos/` con un nombre único basado en la fecha y hora.

### Colores del Árbol:
- 🔴 **Rojo**: Verbos (VERB)
- 🔵 **Turquesa**: Sustantivos (NOUN)
- 🟢 **Verde claro**: Pronombres (PRON)
- 🟠 **Rosa**: Adjetivos (ADJ)
- 🟣 **Morado**: Adverbios (ADV)
- 🟡 **Amarillo**: Determinantes (DET)
- ⚪ **Gris**: Otros

## 🧪 Oraciones de Prueba

Aquí hay algunos ejemplos de oraciones que puedes probar:

### Oraciones Válidas ✓
- "yo camino por el parque"
- "el gato come pescado"
- "María estudia matemáticas"
- "los niños juegan en el jardín"
- "mi hermano lee un libro"

### Oraciones Inválidas ✗
- "por el parque" (sin sujeto ni verbo)
- "yo por" (estructura incompleta)
- "camino parque" (sin conectores apropiados)

## 📁 Estructura del Proyecto

```
Proyecto_AFD_Oraciones/
├── primer_AFD.py              # Programa principal con el AFD
├── analizador_oraciones.py    # Módulo de análisis NLP
├── visualizador_arbol.py      # Módulo de visualización de árboles ⭐
├── requirements.txt           # Dependencias del proyecto
├── README.md                  # Esta documentación
├── test_analizador.py         # Suite de pruebas automáticas
├── test_arbol.py              # Prueba de generación de árboles ⭐
├── debug_spacy.py             # Script de debug
├── diagrama_automata.py       # Visualización del diagrama del AFD
└── arboles_sintacticos/       # Carpeta con árboles generados ⭐
    └── arbol_YYYYMMDD_HHMMSS.png
```

## 🔧 Módulos del Proyecto

### `primer_AFD.py`
Contiene la implementación del Autómata Finito Determinista que:
- Define los estados y transiciones
- Procesa las oraciones a través del autómata
- Muestra el resultado del análisis
- **Genera y muestra árboles sintácticos** ⭐

### `analizador_oraciones.py`
Módulo que utiliza spaCy para:
- Tokenizar las oraciones
- Identificar categorías gramaticales (POS tagging)
- Extraer sujeto, verbo y predicado
- Analizar dependencias sintácticas

### `visualizador_arbol.py` ⭐ NUEVO
Módulo especializado para generar árboles sintácticos:
- Crea grafos dirigidos con NetworkX
- Genera imágenes PNG de alta calidad
- Colorea nodos según categorías gramaticales
- Abre automáticamente las imágenes generadas
- Organiza archivos con timestamps únicos

## 🎓 Conceptos Teóricos

### Autómata Finito Determinista (AFD)
Un AFD es un modelo matemático de computación que consiste en:
- Un conjunto finito de estados
- Un alfabeto de entrada (en este caso, componentes gramaticales)
- Una función de transición que determina el siguiente estado
- Un estado inicial
- Uno o más estados de aceptación

### Procesamiento de Lenguaje Natural (NLP)
El programa utiliza técnicas de NLP para:
- **Tokenización**: Dividir la oración en palabras
- **POS Tagging**: Identificar categorías gramaticales (sustantivos, verbos, etc.)
- **Análisis de Dependencias**: Entender las relaciones entre palabras

## 🛠️ Solución de Problemas

### Error: "El modelo de español no está instalado"
**Solución:**
```bash
python -m spacy download es_core_news_sm
```

### Error: "Import 'spacy' could not be resolved"
**Solución:**
```bash
pip install spacy
```

## 📚 Referencias

- [spaCy Documentation](https://spacy.io/)
- [Teoría de Autómatas y Lenguajes Formales](https://en.wikipedia.org/wiki/Automata_theory)
- [Procesamiento de Lenguaje Natural](https://es.wikipedia.org/wiki/Procesamiento_de_lenguajes_naturales)

## 👨‍💻 Autores

Ricardo Méndez
Emiliano Ledesma

## 📄 Licencia

Este proyecto es de uso académico y educativo.
