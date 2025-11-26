# Reporte Tecnico: Analizador de Oraciones con Automata Finito Determinista

---

## Tabla de Contenidos

1. [Introduccion](#1-introduccion)
2. [Flujo de Interaccion End-to-End](#2-flujo-de-interaccion-end-to-end)
3. [Fundamentos Teoricos](#3-fundamentos-teoricos)
4. [Arquitectura del Sistema](#4-arquitectura-del-sistema)
5. [Modulo Principal: AFDOraciones](#5-modulo-principal-afdoraciones)
6. [Modulo de Analisis: AnalizadorOraciones](#6-modulo-de-analisis-analizadororaciones)
7. [Modulo de Visualizacion: VisualizadorArbol](#7-modulo-de-visualizacion-visualizadorarbol)
8. [Modulo de Derivacion: GeneradorArbolDerivacion](#8-modulo-de-derivacion-generadorarbolderivacion)
9. [Estructuras de Datos](#9-estructuras-de-datos)
10. [Diagramas del Sistema](#10-diagramas-del-sistema)
11. [Consideraciones de Diseno](#11-consideraciones-de-diseno)
12. [Anexos](#12-anexos)

---

## 1. Introduccion

### 1.1 Proposito del Documento

Este documento proporciona una descripcion tecnica exhaustiva del proyecto **Analizador de Oraciones con AFD**. Esta dirigido a desarrolladores, estudiantes y academicos que deseen comprender el funcionamiento interno del sistema, sus componentes y las decisiones de diseno implementadas.

### 1.2 Alcance del Proyecto

El sistema implementa un **Automata Finito Determinista (AFD)** que analiza oraciones simples en espanol, identificando sus componentes gramaticales principales:

- **Sujeto**: Elemento que realiza la accion
- **Verbo**: Accion o estado expresado
- **Predicado**: Informacion completa sobre la accion

Adicionalmente, el sistema genera representaciones visuales mediante:

- Arboles sintacticos basados en dependencias
- Arboles de derivacion gramatical

### 1.3 Tecnologias Utilizadas

| Tecnologia | Version | Proposito |
|------------|---------|-----------|
| Python | 3.7+ | Lenguaje de implementacion |
| spaCy | 3.0.0+ | Procesamiento de Lenguaje Natural |
| es_core_news_sm | - | Modelo de espanol para spaCy |
| matplotlib | 3.5.0+ | Generacion de graficos |
| networkx | 2.6.0+ | Estructuras de grafos |

### 1.4 Estructura de Archivos del Proyecto

```
Proyecto-AFD-Oraciones/
|
|-- primer_AFD.py                    # PUNTO DE ENTRADA PRINCIPAL
|-- analizador_oraciones.py          # Modulo de analisis NLP
|-- visualizador_arbol.py            # Generacion de arboles graficos
|-- generador_arbol_derivacion.py    # Arboles de derivacion gramatical
|-- diagrama_automata.py             # Visualizacion ASCII del AFD
|-- debug_spacy.py                   # Herramienta de depuracion
|-- test_analizador.py               # Suite de pruebas automaticas
|-- test_arbol.py                    # Prueba de generacion de arboles
|-- test_simple.py                   # Prueba basica rapida
|-- requirements.txt                 # Dependencias del proyecto
|-- README.md                        # Documentacion principal
|-- arboles_sintacticos/             # Carpeta de imagenes generadas
|   |-- arbol_YYYYMMDD_HHMMSS.png
|   |-- derivacion_YYYYMMDD_HHMMSS.png
|-- docs/                            # Documentacion tecnica
    |-- REPORTE_TECNICO.md
    |-- REFERENCIA_MODULOS.md
```

---

## 2. Flujo de Interaccion End-to-End

Esta seccion describe el flujo completo de ejecucion del sistema, desde la instalacion hasta la obtencion de resultados.

### 2.1 Diagrama General del Flujo E2E

```
+------------------+     +------------------+     +------------------+
|   INSTALACION    |---->|    EJECUCION     |---->|    RESULTADOS    |
+------------------+     +------------------+     +------------------+
| 1. pip install   |     | 1. primer_AFD.py |     | 1. Aceptada/     |
| 2. spacy download|     | 2. Ingreso texto |     |    Rechazada     |
|                  |     | 3. Procesamiento |     | 2. Componentes   |
|                  |     | 4. Visualizacion |     | 3. Arboles PNG   |
+------------------+     +------------------+     +------------------+
```

### 2.2 Paso 1: Instalacion y Configuracion

**Archivo involucrado:** `requirements.txt`

```bash
# Paso 1.1: Instalar dependencias de Python
pip install -r requirements.txt

# Contenido de requirements.txt:
# spacy>=3.0.0
# matplotlib>=3.5.0
# networkx>=2.6.0
```

```bash
# Paso 1.2: Descargar modelo de espanol de spaCy
python -m spacy download es_core_news_sm
```

**Que esperar:**
- Descarga de aproximadamente 50-100 MB para el modelo
- Tiempo estimado: 1-3 minutos dependiendo de la conexion

**Posibles errores:**
```
ERROR: El modelo de espanol no esta instalado.
Solucion: python -m spacy download es_core_news_sm
```

### 2.3 Paso 2: Ejecucion del Programa Principal

**Archivo a ejecutar:** `primer_AFD.py`

```bash
python primer_AFD.py
```

**Secuencia de carga interna:**

```
primer_AFD.py
    |
    |-- import analizador_oraciones.py
    |       |-- import spacy
    |       |-- Carga modelo es_core_news_sm (2-5 seg)
    |
    |-- import visualizador_arbol.py
    |       |-- import matplotlib
    |       |-- import networkx
    |       |-- Crea carpeta arboles_sintacticos/
    |
    |-- import generador_arbol_derivacion.py
    |
    |-- Instancia AFDOraciones()
    |-- Ejecuta main()
```

**Que esperar en pantalla:**

```
+====================================================================+
|               ANALIZADOR DE ORACIONES SIMPLES                      |
|                    Automata Finito Determinista                    |
+====================================================================+

----------------------------------------------------------------------
Ingresa una oracion en espanol para analizar
(o escribe 'salir' para terminar)
----------------------------------------------------------------------

Oracion: _
```

### 2.4 Paso 3: Ingreso de Oracion

**Interaccion del usuario:**

El usuario escribe una oracion en espanol y presiona Enter.

```
Oracion: el gato come pescado
```

**Que sucede internamente:**

```
1. main() recibe input del usuario
2. Valida que no este vacio y no sea 'salir'
3. Llama a afd.procesar_oracion("el gato come pescado")
```

### 2.5 Paso 4: Procesamiento de la Oracion

**Flujo detallado de procesamiento:**

```
procesar_oracion("el gato come pescado")
|
|-- FASE 1: Analisis NLP
|   |-- analizador.analizar_oracion(oracion)
|   |   |-- nlp(oracion) -> spaCy Doc
|   |   |-- Extrae tokens: [el, gato, come, pescado]
|   |   |-- Extrae POS: [DET, NOUN, VERB, NOUN]
|   |   |-- Extrae DEP: [det, nsubj, ROOT, obj]
|   |   |-- Identifica sujeto: "el gato"
|   |   |-- Identifica verbo: "come"
|   |   |-- Identifica predicado: "come pescado"
|   |   |-- Retorna resultado_nlp
|
|-- FASE 2: Transiciones del AFD
|   |-- Estado actual: q0
|   |-- Hay sujeto? Si -> transicion a q1
|   |-- Hay verbo? Si -> transicion a q2
|   |-- Hay predicado? Si -> transicion a q3
|   |-- Estado final: q3 (ACEPTACION)
|
|-- FASE 3: Generacion de Arboles (solo si aceptada)
|   |-- visualizador.generar_arbol(doc, oracion)
|   |   |-- Crea grafo NetworkX
|   |   |-- Calcula posiciones
|   |   |-- Dibuja con matplotlib
|   |   |-- Guarda PNG
|   |
|   |-- generador_derivacion.generar_arbol(doc, resultado)
|   |   |-- Construye estructura de nodos
|   |   |-- visualizador.generar_arbol_derivacion()
|   |   |-- Guarda PNG
|
|-- Retorna resultado completo
```

**Que esperar en pantalla:**

```
======================================================================
AUTOMATA FINITO DETERMINISTA - ANALIZADOR DE ORACIONES
======================================================================

Oracion ingresada: 'el gato come pescado'
Estado inicial: q0

----------------------------------------------------------------------
FASE 1: Analisis lexico y sintactico
----------------------------------------------------------------------

----------------------------------------------------------------------
FASE 2: Transiciones del automata
----------------------------------------------------------------------

  q0 -> q1
  Razon: Sujeto encontrado: 'el gato'

  q1 -> q2
  Razon: Verbo encontrado: 'come'

  q2 -> q3
  Razon: Predicado completo: 'come pescado'

======================================================================
RESULTADO FINAL DEL AUTOMATA
======================================================================

Estado final: q3
Estado de aceptacion?: SI

[CHECK] ORACION ACEPTADA
  La oracion tiene una estructura gramatical valida.

----------------------------------------------------------------------
COMPONENTES IDENTIFICADOS:
----------------------------------------------------------------------
Sujeto:    el gato
Verbo:     come
Predicado: come pescado

----------------------------------------------------------------------
GENERANDO ARBOLES...
----------------------------------------------------------------------
[CHECK] Arbol sintactico generado: arboles_sintacticos/arbol_20251126_183000.png
[CHECK] Arbol de derivacion generado: arboles_sintacticos/derivacion_20251126_183001.png

Reglas gramaticales aplicadas:
   1. S -> SN + SV
```

### 2.6 Paso 5: Visualizacion de Arboles

**Interaccion del usuario:**

```
----------------------------------------------------------------------
VISUALIZACION DE ARBOLES
----------------------------------------------------------------------

Deseas abrir el arbol sintactico? (s/n): s
Abriendo arbol sintactico...

Deseas abrir el arbol de derivacion? (s/n): s
Abriendo arbol de derivacion...
```

**Que sucede:**
- Se abre el visor de imagenes predeterminado del sistema
- En Linux: `xdg-open`
- En macOS: `open`
- En Windows: `os.startfile`

**Archivos generados:**
```
arboles_sintacticos/
|-- arbol_20251126_183000.png      # Arbol de dependencias
|-- derivacion_20251126_183001.png # Arbol de derivacion
```

### 2.7 Paso 6: Analisis Detallado (Opcional)

**Interaccion del usuario:**

```
----------------------------------------------------------------------
Deseas ver el analisis detallado (con arbol ASCII)? (s/n): s
```

**Que esperar:**

```
============================================================
ANALISIS DETALLADO DE LA ORACION
============================================================

Tokens identificados: 4
Oracion valida: SI

Sujeto: el gato
Verbo: come
Predicado: come pescado

------------------------------------------------------------
ETIQUETAS POS (Part-of-Speech):
------------------------------------------------------------
  'el' -> POS: DET, DEP: det
  'gato' -> POS: NOUN, DEP: nsubj
  'come' -> POS: VERB, DEP: ROOT
  'pescado' -> POS: NOUN, DEP: obj

============================================================

======================================================================
ARBOL DE DERIVACION (Formato ASCII):
======================================================================

+-- S
    +-- SN
    |   +-- DET -> 'el'
    |   +-- N -> 'gato'
    +-- SV
        +-- V -> 'come'
        +-- SN
            +-- N -> 'pescado'
```

### 2.8 Paso 7: Ciclo Continuo o Salida

El programa vuelve al prompt para ingresar otra oracion:

```
----------------------------------------------------------------------
Ingresa una oracion en espanol para analizar
(o escribe 'salir' para terminar)
----------------------------------------------------------------------

Oracion: salir

Hasta luego!
```

### 2.9 Flujo para Oracion Rechazada

Si la oracion no cumple con la estructura esperada:

```
Oracion: por el parque

======================================================================
AUTOMATA FINITO DETERMINISTA - ANALIZADOR DE ORACIONES
======================================================================

Oracion ingresada: 'por el parque'
Estado inicial: q0

----------------------------------------------------------------------
FASE 2: Transiciones del automata
----------------------------------------------------------------------

  q0 -> qr
  Razon: No se encontro sujeto ni verbo

======================================================================
RESULTADO FINAL DEL AUTOMATA
======================================================================

Estado final: qr
Estado de aceptacion?: NO

[X] ORACION RECHAZADA
  La oracion no cumple con la estructura esperada.

----------------------------------------------------------------------
COMPONENTES IDENTIFICADOS:
----------------------------------------------------------------------
Sujeto:    (no identificado)
Verbo:     (no identificado)
Predicado: (no identificado)
```

**Nota:** No se generan arboles para oraciones rechazadas.

### 2.10 Resumen del Flujo E2E

```
+=========================================================================+
|                    FLUJO COMPLETO END-TO-END                            |
+=========================================================================+
|                                                                         |
|  [1] INSTALACION                                                        |
|      pip install -r requirements.txt                                    |
|      python -m spacy download es_core_news_sm                           |
|                           |                                             |
|                           v                                             |
|  [2] EJECUCION                                                          |
|      python primer_AFD.py                                               |
|                           |                                             |
|                           v                                             |
|  [3] ENTRADA                                                            |
|      Usuario escribe oracion                                            |
|                           |                                             |
|                           v                                             |
|  [4] ANALISIS NLP                                                       |
|      analizador_oraciones.py procesa con spaCy                          |
|                           |                                             |
|                           v                                             |
|  [5] AUTOMATA AFD                                                       |
|      primer_AFD.py ejecuta transiciones q0->q1->q2->q3                  |
|                           |                                             |
|              +------------+------------+                                |
|              |                         |                                |
|              v                         v                                |
|  [6a] ACEPTADA                  [6b] RECHAZADA                          |
|       Genera arboles                  Muestra error                     |
|       visualizador_arbol.py           No genera arboles                 |
|       generador_arbol_derivacion.py                                     |
|              |                         |                                |
|              v                         v                                |
|  [7] SALIDA                                                             |
|      - Muestra componentes identificados                                |
|      - Ofrece abrir imagenes PNG                                        |
|      - Ofrece analisis detallado                                        |
|                           |                                             |
|                           v                                             |
|  [8] CICLO                                                              |
|      Vuelve a [3] o sale con 'salir'                                    |
|                                                                         |
+=========================================================================+
```

### 2.11 Archivos Alternativos de Ejecucion

Ademas del programa principal, existen otros archivos ejecutables:

**test_analizador.py - Suite de pruebas automaticas**
```bash
python test_analizador.py
```
- Ejecuta 8 oraciones de prueba automaticamente
- No requiere interaccion del usuario
- Muestra resumen de resultados

**test_arbol.py - Prueba de generacion de arboles**
```bash
python test_arbol.py
```
- Analiza "el gato come pescado"
- Genera ambos tipos de arboles
- Abre las imagenes automaticamente

**test_simple.py - Prueba basica rapida**
```bash
python test_simple.py
```
- Ejecuta un analisis rapido de "yo camino por el parque"
- Muestra solo los componentes basicos

**debug_spacy.py - Herramienta de depuracion**
```bash
python debug_spacy.py
```
- Muestra informacion detallada de tokenizacion
- Util para entender como spaCy procesa una oracion

**diagrama_automata.py - Diagrama ASCII del AFD**
```bash
python diagrama_automata.py
```
- Muestra el diagrama del automata en formato ASCII
- Incluye ejemplos de transiciones

---

## 3. Fundamentos Teoricos

### 3.1 Automatas Finitos Deterministas

Un **Automata Finito Determinista (AFD)** es una quintupla M = (Q, Sigma, delta, q0, F) donde:

- **Q**: Conjunto finito de estados
- **Sigma**: Alfabeto de entrada (simbolos de entrada)
- **delta**: Funcion de transicion Q x Sigma -> Q
- **q0**: Estado inicial (q0 pertenece a Q)
- **F**: Conjunto de estados de aceptacion (F esta contenido en Q)

### 3.2 Definicion Formal del AFD del Proyecto

```
M = (Q, Sigma, delta, q0, F)

Q = {q0, q1, q2, q3, qr}

Sigma = {SUJETO, VERBO, PREDICADO, ERROR}

q0 = q0 (estado inicial)

F = {q3} (estado de aceptacion)

delta (funcion de transicion):
    delta(q0, SUJETO)    = q1
    delta(q0, VERBO)     = q2
    delta(q0, ERROR)     = qr
    delta(q1, VERBO)     = q2
    delta(q1, ERROR)     = qr
    delta(q2, PREDICADO) = q3
    delta(q2, ERROR)     = qr
```

### 3.3 Semantica de los Estados

| Estado | Nombre | Descripcion |
|--------|--------|-------------|
| q0 | Inicial | Esperando entrada, ningun componente identificado |
| q1 | Sujeto | Sujeto identificado, esperando verbo |
| q2 | Verbo | Verbo identificado, esperando predicado completo |
| q3 | Aceptacion | Oracion valida con estructura completa |
| qr | Rechazo | Oracion invalida, estructura incorrecta |

### 3.4 Procesamiento de Lenguaje Natural (NLP)

El sistema utiliza tecnicas de NLP para el analisis gramatical:

**3.4.1 Tokenizacion**

Proceso de dividir el texto en unidades minimas (tokens):

```
Entrada: "el gato come pescado"
Tokens: ["el", "gato", "come", "pescado"]
```

**3.4.2 Etiquetado POS (Part-of-Speech)**

Asignacion de categorias gramaticales a cada token:

| Token | POS | Significado |
|-------|-----|-------------|
| el | DET | Determinante |
| gato | NOUN | Sustantivo |
| come | VERB | Verbo |
| pescado | NOUN | Sustantivo |

**3.4.3 Analisis de Dependencias**

Identificacion de relaciones sintacticas entre tokens:

| Token | Dependencia | Cabeza | Significado |
|-------|-------------|--------|-------------|
| el | det | gato | Determinante de "gato" |
| gato | nsubj | come | Sujeto nominal de "come" |
| come | ROOT | come | Raiz de la oracion |
| pescado | obj | come | Objeto directo de "come" |

### 3.5 Gramaticas Libres de Contexto

Para los arboles de derivacion, se implementan reglas de produccion:

```
Gramatica G = (V, T, P, S)

V (Variables): {S, SN, SV, SP}
T (Terminales): {DET, N, PRON, V, PREP, ADV, ADJ}
S (Simbolo inicial): S (Oracion)

P (Producciones):
    S  -> SN SV
    SN -> DET N
    SN -> PRON
    SN -> N
    SV -> V SN
    SV -> V SP
    SV -> V ADV
    SV -> V
    SP -> PREP SN
```

---

## 4. Arquitectura del Sistema

### 4.1 Diagrama de Componentes

```
+------------------------------------------------------------------+
|                        primer_AFD.py                              |
|                      (Modulo Principal)                           |
|                                                                   |
|  +------------------+    +-------------------+    +--------------+|
|  |  AFDOraciones    |    | Interface Usuario |    | Coordinador  ||
|  |  (Clase)         |<-->| (main)            |<-->| Analisis     ||
|  +------------------+    +-------------------+    +--------------+|
+------------------------------------------------------------------+
           |                        |                      |
           v                        v                      v
+--------------------+   +----------------------+   +----------------+
| analizador_        |   | visualizador_        |   | generador_     |
| oraciones.py       |   | arbol.py             |   | arbol_         |
|                    |   |                      |   | derivacion.py  |
| +----------------+ |   | +------------------+ |   | +------------+ |
| | Analizador-    | |   | | Visualizador-    | |   | | Generador- | |
| | Oraciones      | |   | | Arbol            | |   | | ArbolDeriv | |
| +----------------+ |   | +------------------+ |   | +------------+ |
+--------------------+   +----------------------+   +----------------+
           |                        |
           v                        v
    +------------+           +-------------+
    |   spaCy    |           | matplotlib  |
    | NLP Engine |           | networkx    |
    +------------+           +-------------+
```

### 4.2 Patron de Diseno

El sistema implementa un patron de **Fachada (Facade)** donde:

- `AFDOraciones` actua como fachada principal
- Coordina la interaccion entre componentes especializados
- Oculta la complejidad del sistema al usuario

### 4.3 Responsabilidades por Modulo

| Modulo | Responsabilidad |
|--------|-----------------|
| primer_AFD.py | Logica del automata, interfaz de usuario, coordinacion |
| analizador_oraciones.py | Procesamiento NLP, extraccion de componentes |
| visualizador_arbol.py | Generacion de imagenes de arboles |
| generador_arbol_derivacion.py | Construccion de arboles de derivacion |

### 4.4 Diagrama de Dependencias entre Modulos

```
                    primer_AFD.py
                          |
        +-----------------+-----------------+
        |                 |                 |
        v                 v                 v
analizador_         visualizador_     generador_arbol_
oraciones.py        arbol.py          derivacion.py
        |                 |                 |
        v                 v                 |
    spaCy            matplotlib             |
                     networkx               |
                          |                 |
                          +---------+-------+
                                    |
                                    v
                          generador_arbol_
                          derivacion.py
                          (NodoDerivacion)
```

---

## 5. Modulo Principal: AFDOraciones

### 5.1 Ubicacion y Proposito

**Archivo:** `primer_AFD.py`

**Proposito:** Implementar la logica del Automata Finito Determinista y coordinar todos los componentes del sistema.

### 5.2 Estructura de la Clase

```python
class AFDOraciones:
    """
    Atributos:
        analizador: AnalizadorOraciones
        visualizador: VisualizadorArbol
        generador_derivacion: GeneradorArbolDerivacion
        estados: List[str]
        estado_inicial: str
        estados_aceptacion: List[str]
        estado_actual: str
        historial: List[Tuple[str, str]]
    
    Metodos:
        procesar_oracion(oracion: str) -> dict
        _transicion(nuevo_estado: str, razon: str)
        _generar_resultado(resultado_nlp: dict, aceptada: bool) -> dict
        mostrar_analisis_detallado(resultado: dict)
    """
```

### 5.3 Metodo: procesar_oracion

Este metodo implementa el algoritmo principal del automata:

```python
def procesar_oracion(self, oracion: str) -> dict:
    """
    Algoritmo:
    1. Resetear estado del automata a q0
    2. Ejecutar analisis NLP de la oracion
    3. Evaluar transiciones basadas en componentes encontrados:
       a. Si hay sujeto -> transicion a q1
       b. Si hay verbo (con o sin sujeto) -> transicion a q2
       c. Si hay predicado completo -> transicion a q3
       d. Si hay error en cualquier paso -> transicion a qr
    4. Verificar si estado final es de aceptacion
    5. Generar arboles si la oracion fue aceptada
    6. Retornar resultado completo
    """
```

### 5.4 Diagrama de Flujo del Metodo procesar_oracion

```
                    INICIO
                       |
                       v
              +----------------+
              | Resetear AFD   |
              | estado = q0    |
              +----------------+
                       |
                       v
              +----------------+
              | Analisis NLP   |
              | de la oracion  |
              +----------------+
                       |
                       v
              +----------------+
              | Hay sujeto?    |
              +----------------+
               /            \
            Si/              \No
             /                \
            v                  v
    +------------+      +----------------+
    | q0 -> q1   |      | Hay verbo?     |
    +------------+      +----------------+
            |            /            \
            v         Si/              \No
    +------------+     /                \
    | Hay verbo? |    v                  v
    +------------+  +------------+  +------------+
     /          \   | q0 -> q2   |  | q0 -> qr   |
  Si/            \No+------------+  | RECHAZADA  |
   /              \      |          +------------+
  v                v     |
+--------+    +--------+ |
|q1 -> q2|    |q1 -> qr| |
+--------+    +--------+ |
     |             |     |
     +------+------+     |
            |            |
            v            v
    +----------------+
    | Hay predicado? |
    +----------------+
     /            \
  Si/              \No
   /                \
  v                  v
+--------+      +--------+
|q2 -> q3|      |q2 -> qr|
|ACEPTADA|      |RECHZDA |
+--------+      +--------+
     |               |
     v               v
+------------------+
| Generar arboles  |
| (solo si q3)     |
+------------------+
     |
     v
   RETORNO
```

### 5.5 Logica de Transiciones

```python
def _transicion(self, nuevo_estado: str, razon: str):
    """
    Ejecuta una transicion de estado del automata.
    
    Parametros:
        nuevo_estado: Estado destino de la transicion
        razon: Descripcion de por que ocurre la transicion
    
    Efectos:
        - Actualiza estado_actual
        - Registra la transicion en el historial
        - Imprime informacion de la transicion
    """
    print(f"\n  {self.estado_actual} -> {nuevo_estado}")
    print(f"  Razon: {razon}")
    self.estado_actual = nuevo_estado
    self.historial.append((nuevo_estado, razon))
```

### 5.6 Estructura del Resultado

El metodo `procesar_oracion` retorna un diccionario con la siguiente estructura:

```python
resultado = {
    'aceptada': bool,           # True si la oracion fue aceptada
    'estado_final': str,        # Estado final del automata (q0-q3, qr)
    'historial': List[Tuple],   # Lista de (estado, razon) 
    'analisis_nlp': {           # Resultado del analisis NLP
        'valida': bool,
        'sujeto': str | None,
        'verbo': str | None,
        'predicado': str | None,
        'tokens': List[str],
        'pos_tags': List[dict],
        'dependencias': List,
        'doc': spacy.Doc
    },
    'ruta_arbol_sintactico': str | None,    # Ruta al archivo PNG
    'ruta_arbol_derivacion': str | None,    # Ruta al archivo PNG
    'arbol_derivacion': NodoDerivacion | None  # Estructura del arbol
}
```

---

## 6. Modulo de Analisis: AnalizadorOraciones

### 6.1 Ubicacion y Proposito

**Archivo:** `analizador_oraciones.py`

**Proposito:** Realizar el analisis de lenguaje natural usando spaCy para identificar componentes gramaticales.

### 6.2 Estructura de la Clase

```python
class AnalizadorOraciones:
    """
    Atributos:
        nlp: spacy.Language  # Pipeline de procesamiento de spaCy
    
    Metodos:
        analizar_oracion(oracion: str) -> Dict
        _obtener_frase(token) -> List
        obtener_estadisticas(resultado: Dict) -> str
    """
```

### 6.3 Inicializacion del Modelo NLP

```python
def __init__(self):
    """
    Carga el modelo de espanol de spaCy.
    
    El modelo 'es_core_news_sm' incluye:
    - Tokenizador
    - Tagger POS
    - Parser de dependencias
    - Named Entity Recognition (NER)
    """
    try:
        self.nlp = spacy.load("es_core_news_sm")
    except OSError:
        print("ERROR: El modelo de espanol no esta instalado.")
        raise
```

### 6.4 Algoritmo de Analisis

```
ALGORITMO: analizar_oracion(oracion)
ENTRADA: String oracion
SALIDA: Diccionario con componentes gramaticales

1. PROCESAR oracion con spaCy -> doc
2. INICIALIZAR resultado con valores por defecto
3. EXTRAER tokens y etiquetas POS

4. BUSCAR verbo principal:
   4.1. Buscar token con POS="VERB" y DEP="ROOT"
   4.2. Si no existe, buscar cualquier token con POS="VERB"
   4.3. Si no existe, buscar ROOT que tenga hijos con DEP="nsubj"

5. SI existe verbo_principal:
   5.1. BUSCAR sujeto:
        - Token con DEP in ["nsubj", "nsubjpass"] y HEAD=verbo
        - Si no existe, buscar PRON antes del verbo
   5.2. OBTENER frase completa del sujeto (subtree)
   
   5.3. CONSTRUIR predicado:
        - Agregar verbo principal
        - Agregar complementos del verbo (obj, obl, advmod, etc.)
        - Ordenar por posicion en la oracion
   
   5.4. VALIDAR oracion:
        - Valida si tiene sujeto, verbo y predicado
        - Tambien valida si solo tiene verbo (imperativas)

6. RETORNAR resultado
```

### 6.5 Tabla de Etiquetas POS Relevantes

| Etiqueta | Categoria | Ejemplos |
|----------|-----------|----------|
| VERB | Verbo | come, corre, estudia |
| NOUN | Sustantivo | gato, libro, casa |
| PROPN | Nombre propio | Maria, Juan |
| PRON | Pronombre | yo, el, ella |
| DET | Determinante | el, la, un, una |
| ADJ | Adjetivo | grande, bonito |
| ADV | Adverbio | rapidamente, muy |
| ADP | Preposicion | por, para, con |
| AUX | Verbo auxiliar | ha, esta, fue |

### 6.6 Tabla de Dependencias Relevantes

| Dependencia | Significado | Ejemplo |
|-------------|-------------|---------|
| nsubj | Sujeto nominal | "Maria" en "Maria come" |
| ROOT | Raiz de la oracion | Verbo principal |
| obj | Objeto directo | "pescado" en "come pescado" |
| det | Determinante | "el" en "el gato" |
| obl | Oblicuo | "parque" en "por el parque" |
| case | Marca de caso | "por" en "por el parque" |

---

## 7. Modulo de Visualizacion: VisualizadorArbol

### 7.1 Ubicacion y Proposito

**Archivo:** `visualizador_arbol.py`

**Proposito:** Generar representaciones graficas de arboles sintacticos y de derivacion en formato PNG.

### 7.2 Estructura de la Clase

```python
class VisualizadorArbol:
    """
    Atributos:
        carpeta_imagenes: str  # Ruta donde se guardan las imagenes
    
    Metodos publicos:
        generar_arbol(doc, oracion: str) -> str
        generar_arbol_derivacion(nodo_raiz, oracion: str) -> str
        abrir_imagen(ruta_archivo: str)
    
    Metodos privados:
        _calcular_posiciones_jerarquicas(G, doc) -> dict
        _asignar_niveles(G, nodo, niveles, nivel_actual)
        _agregar_leyenda(ax, colores)
    """
```

### 7.3 Algoritmo de Generacion del Arbol Sintactico

```
ALGORITMO: generar_arbol(doc, oracion)
ENTRADA: doc (documento spaCy), oracion (string)
SALIDA: Ruta del archivo PNG generado

1. CREAR grafo dirigido G (networkx.DiGraph)

2. PARA cada token en doc:
   2.1. Crear nodo con id = token.i
   2.2. Etiqueta = "texto\n[POS]\n(DEP)"
   2.3. Agregar nodo a G

3. PARA cada token en doc:
   3.1. SI token.head != token:
        Agregar arista desde token.head.i hacia token.i

4. CALCULAR posiciones jerarquicas de nodos

5. ASIGNAR colores segun categoria POS

6. DIBUJAR con matplotlib:
   - Aristas con flechas
   - Nodos circulares coloreados
   - Etiquetas de texto
   - Titulo y leyenda

7. GUARDAR imagen PNG con timestamp unico

8. RETORNAR ruta del archivo
```

### 7.4 Esquema de Colores

**Arbol Sintactico:**

| Categoria | Color | Codigo Hex |
|-----------|-------|------------|
| VERB | Rojo | #FF6B6B |
| NOUN | Turquesa | #4ECDC4 |
| PRON | Verde claro | #95E1D3 |
| ADJ | Rosa | #F38181 |
| ADV | Morado | #AA96DA |
| ADP | Rosa claro | #FCBAD3 |
| DET | Amarillo claro | #FFFFD2 |
| PROPN | Verde | #A8E6CF |
| Otros | Gris | #E0E0E0 |

**Arbol de Derivacion:**

| Simbolo | Color | Codigo Hex |
|---------|-------|------------|
| S | Rojo | #FF6B6B |
| SN | Turquesa | #4ECDC4 |
| SV | Verde | #95E1D3 |
| SP | Rosa | #FCBAD3 |
| Terminal | Beige | #FFE5B4 |

---

## 8. Modulo de Derivacion: GeneradorArbolDerivacion

### 8.1 Ubicacion y Proposito

**Archivo:** `generador_arbol_derivacion.py`

**Proposito:** Construir arboles de derivacion gramatical basados en reglas de produccion formales.

### 8.2 Estructura de Clases

```python
class NodoDerivacion:
    """
    Representa un nodo en el arbol de derivacion.
    
    Atributos:
        simbolo: str      # S, SN, SV, DET, N, V, etc.
        nivel: int        # Profundidad en el arbol
        hijos: List[NodoDerivacion]
        es_terminal: bool
        palabra: str | None  # Solo si es_terminal
    """

class GeneradorArbolDerivacion:
    """
    Genera arboles de derivacion gramatical.
    
    Metodos:
        generar_arbol(doc, analisis: Dict) -> NodoDerivacion
        obtener_reglas_aplicadas(raiz) -> List[str]
        imprimir_arbol(nodo, prefijo, es_ultimo)
    """
```

### 8.3 Reglas Gramaticales Implementadas

```
S  -> SN + SV          (Oracion = Sintagma Nominal + Sintagma Verbal)
SN -> DET + N          (Sintagma Nominal = Determinante + Nombre)
SN -> PRON             (Sintagma Nominal = Pronombre)
SN -> N                (Sintagma Nominal = Nombre solo)
SV -> V + SN           (Sintagma Verbal = Verbo + Objeto directo)
SV -> V + SP           (Sintagma Verbal = Verbo + Sintagma Preposicional)
SV -> V + ADV          (Sintagma Verbal = Verbo + Adverbio)
SV -> V                (Sintagma Verbal = Verbo solo)
SP -> PREP + SN        (Sintagma Preposicional = Preposicion + SN)
```

### 8.4 Mapeo de Etiquetas POS a Simbolos

```python
pos_a_simbolo = {
    'DET': 'DET',    # Determinante
    'NOUN': 'N',     # Nombre/Sustantivo
    'PROPN': 'N',    # Nombre propio -> N
    'PRON': 'PRON',  # Pronombre
    'VERB': 'V',     # Verbo
    'ADP': 'PREP',   # Preposicion
    'ADV': 'ADV',    # Adverbio
    'ADJ': 'ADJ',    # Adjetivo
    'AUX': 'V'       # Auxiliar -> V
}
```

---

## 9. Estructuras de Datos

### 9.1 Documento spaCy (Doc)

```
spacy.Doc
+-- texto_original: str
+-- tokens: List[Token]
    +-- Token
        +-- text: str           # Texto del token
        +-- i: int              # Indice en el documento
        +-- pos_: str           # Etiqueta POS
        +-- tag_: str           # Etiqueta morfologica detallada
        +-- dep_: str           # Tipo de dependencia
        +-- head: Token         # Token cabeza (padre)
        +-- children: Iterator  # Tokens hijos
        +-- subtree: Iterator   # Subarbol completo
```

### 9.2 Grafo de Dependencias (NetworkX)

```
networkx.DiGraph
+-- nodes: Dict[int, Dict]
    +-- id: int (indice del token)
    +-- label: str
    +-- pos: str
    +-- dep: str
    +-- text: str
+-- edges: List[Tuple[int, int]]
    +-- (head_id, child_id)
```

### 9.3 Arbol de Derivacion

```
NodoDerivacion (raiz)
+-- simbolo: "S"
+-- nivel: 0
+-- hijos: [
    NodoDerivacion (SN)
    +-- simbolo: "SN"
    +-- nivel: 1
    +-- hijos: [
        NodoDerivacion (DET)
        +-- es_terminal: True
        +-- palabra: "el"
        ,
        NodoDerivacion (N)
        +-- es_terminal: True
        +-- palabra: "gato"
    ]
    ,
    NodoDerivacion (SV)
    +-- simbolo: "SV"
    +-- nivel: 1
    +-- hijos: [...]
]
```

---

## 10. Diagramas del Sistema

### 10.1 Diagrama del Automata Finito Determinista

```
                         +-------------+
                         |     q0      |
                         |   INICIAL   |
                         +------+------+
                                |
               +----------------+----------------+
               |                                 |
         [SUJETO]                            [VERBO]
               |                           (sin sujeto)
               v                                 |
        +------+------+                          |
        |     q1      |                          |
        |   SUJETO    |-------[VERBO]-------+    |
        +-------------+                     |    |
               |                            |    |
             [ERROR]                        v    v
               |                     +------+----+--+
               v                     |     q2       |
        +------+------+              |    VERBO     |
        |     qr      |              +------+-------+
        |  RECHAZO    |                     |
        +-------------+        +------------+------------+
               ^               |                         |
               |          [PREDICADO]                 [ERROR]
               |               |                         |
               |               v                         |
               |        +------+------+                  |
               +--------|     q3      |------------------+
                        | ACEPTACION  |
                        +-------------+
```

### 10.2 Diagrama de Secuencia

```
Usuario          main()        AFDOraciones    AnalizadorOrac.    Visualizador
   |               |                |                |                |
   |--"oracion"--->|                |                |                |
   |               |--procesar----->|                |                |
   |               |                |---analizar---->|                |
   |               |                |                |--spaCy-------->|
   |               |                |                |<--doc----------|
   |               |                |<--resultado----|                |
   |               |                |                |                |
   |               |                |--transiciones--|                |
   |               |                |                |                |
   |               |                |---generar_arbol-------->|       |
   |               |                |                         |--PNG--|
   |               |                |<---ruta-----------------|       |
   |               |                |                |                |
   |               |<--resultado----|                |                |
   |<--mostrar-----|                |                |                |
```

### 10.3 Diagrama de Clases

```
+-------------------+        +------------------------+
|   AFDOraciones    |        |  AnalizadorOraciones   |
+-------------------+        +------------------------+
| - analizador      |------->| - nlp: spacy.Language  |
| - visualizador    |        +------------------------+
| - generador_deriv |        | + analizar_oracion()   |
| - estados         |        | + obtener_estadisticas |
| - estado_actual   |        +------------------------+
| - historial       |
+-------------------+        +------------------------+
| + procesar_oracion|        |   VisualizadorArbol    |
| + mostrar_analisis|        +------------------------+
| - _transicion()   |------->| - carpeta_imagenes     |
+-------------------+        +------------------------+
         |                   | + generar_arbol()      |
         |                   | + generar_arbol_deriv()|
         v                   +------------------------+
+------------------------+
| GeneradorArbolDeriv.   |   +------------------------+
+------------------------+   |    NodoDerivacion      |
| - pos_a_simbolo        |   +------------------------+
+------------------------+   | - simbolo: str         |
| + generar_arbol()      |<--| - nivel: int           |
| + obtener_reglas()     |   | - hijos: List          |
| + imprimir_arbol()     |   | - es_terminal: bool    |
+------------------------+   +------------------------+
```

---

## 11. Consideraciones de Diseno

### 11.1 Decisiones de Arquitectura

**Separacion de responsabilidades:**

El sistema sigue el principio de responsabilidad unica (SRP):

- `AFDOraciones`: Solo logica del automata y coordinacion
- `AnalizadorOraciones`: Solo analisis NLP
- `VisualizadorArbol`: Solo generacion de graficos
- `GeneradorArbolDerivacion`: Solo construccion de arboles formales

### 11.2 Manejo de Casos Especiales

**Verbos mal etiquetados por spaCy:**

```python
# Problema: "yo camino" -> "camino" etiquetado como NOUN
# Solucion: Buscar ROOT con hijos nsubj
if not verbo_principal:
    for token in doc:
        if token.dep_ == "ROOT":
            tiene_sujeto = any(child.dep_ in ["nsubj"] for child in token.children)
            if tiene_sujeto:
                verbo_principal = token
```

**Oraciones imperativas (sin sujeto explicito):**

```python
# La oracion es valida si tiene verbo, aunque no tenga sujeto
elif resultado['verbo']:
    resultado['valida'] = True
```

### 11.3 Limitaciones Conocidas

| Limitacion | Descripcion |
|------------|-------------|
| Oraciones simples | Solo analiza oraciones simples |
| Modelo NLP | Depende de precision de spaCy |
| Interfaz | Solo linea de comandos |
| Idioma | Solo espanol |

### 11.4 Rendimiento

| Operacion | Tiempo Aproximado |
|-----------|-------------------|
| Carga del modelo spaCy | 2-5 segundos |
| Analisis de oracion | 10-50 milisegundos |
| Generacion de arbol PNG | 1-2 segundos |

---

## 12. Anexos

### 12.1 Ejemplos de Uso

**Oraciones validas:**

| Oracion | Sujeto | Verbo | Predicado |
|---------|--------|-------|-----------|
| yo camino por el parque | yo | camino | camino por el parque |
| el gato come pescado | el gato | come | come pescado |
| Maria estudia matematicas | Maria | estudia | estudia matematicas |

**Oraciones invalidas:**

| Oracion | Razon de Rechazo |
|---------|------------------|
| por el parque | Sin sujeto ni verbo |
| camino parque | Estructura incompleta |

### 12.2 Glosario

| Termino | Definicion |
|---------|------------|
| AFD | Automata Finito Determinista |
| NLP | Procesamiento de Lenguaje Natural |
| POS | Part-of-Speech (Categoria gramatical) |
| DEP | Dependencia sintactica |
| Token | Unidad minima de texto |
| Sintagma | Grupo de palabras con funcion gramatical |
| ROOT | Raiz del arbol de dependencias |
| nsubj | Sujeto nominal |

### 12.3 Referencias

1. Hopcroft, J. E., Motwani, R., & Ullman, J. D. (2006). Introduction to Automata Theory, Languages, and Computation.
2. Jurafsky, D., & Martin, J. H. (2020). Speech and Language Processing.
3. spaCy Documentation: https://spacy.io/
4. NetworkX Documentation: https://networkx.org/
5. Matplotlib Documentation: https://matplotlib.org/

---

**Documento generado para el proyecto Analizador de Oraciones con AFD**

**Autores:** Ricardo Mendez, Emiliano Ledesma

**Institucion:** UPQ - Curso de Matematicas
