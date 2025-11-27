# Índice General de Documentación
## Proyecto: Analizador de Oraciones con AFD

**Última actualización:** Noviembre 2024
**Autores:** Ricardo Méndez, Emiliano Ledesma

---

## 📚 Estructura de Documentación

Este proyecto cuenta con **DOS versiones completas**, cada una con su documentación independiente:

```
docs/
├── INDICE_GENERAL.md                      ← Estás aquí
│
├── ────────────────────────────────────────────────────
│   VERSIÓN SIMPLIFICADA (Sin dependencias)
├── ────────────────────────────────────────────────────
├── README_VERSION_SIMPLIFICADA.md         (30 págs) 📘
├── REPORTE_TECNICO_SIMPLIFICADO.md        (20 págs) 📗
├── REFERENCIA_API_SIMPLIFICADA.md         (15 págs) 📙
│
├── ────────────────────────────────────────────────────
│   VERSIÓN COMPLETA (Con spaCy)
├── ────────────────────────────────────────────────────
├── REPORTE_TECNICO.md                     (20 págs) 📕
└── REFERENCIA_MODULOS.md                  (15 págs) 📔
```

---

## 🎯 Guía Rápida: ¿Qué Leer?

### Si eres ESTUDIANTE o estás APRENDIENDO:

```
👉 VERSIÓN SIMPLIFICADA

1. README_VERSION_SIMPLIFICADA.md          (COMPLETO)
   - Fundamentos teóricos detallados
   - Gramática formal
   - Definición matemática del AFD
   - Ejemplos paso a paso

2. REPORTE_TECNICO_SIMPLIFICADO.md         (Complemento)
   - Análisis técnico
   - Comparación con versión completa
   - Guías de extensión

3. REFERENCIA_API_SIMPLIFICADA.md          (Consulta)
   - Documentación de clases
   - Ejemplos de código
```

### Si eres DESARROLLADOR o quieres PRODUCCIÓN:

```
👉 VERSIÓN COMPLETA

1. REPORTE_TECNICO.md                      (COMPLETO)
   - Arquitectura con spaCy
   - Módulos profesionales
   - Flujo end-to-end

2. REFERENCIA_MODULOS.md                   (API)
   - Clases y métodos
   - Parámetros y retornos
```

---

## 📘 Versión Simplificada - Documentación Completa

### 1. README_VERSION_SIMPLIFICADA.md

**📄 30 páginas | Documento principal educativo**

#### Contenido:

**Sección 1: Descripción General** (3 págs)
- Objetivo del proyecto
- Características principales
- ¿Por qué una versión simplificada?
- Comparación visual con versión completa

**Sección 2: Fundamentos Teóricos** ⭐ (10 págs)
- Lenguajes formales (definición, ejemplos)
- Jerarquía de Chomsky (4 tipos)
- Gramáticas independientes del contexto (GIC)
  - Definición formal G = (V, T, P, S)
  - Propiedades y características
- Autómatas finitos deterministas (AFD)
  - Definición formal M = (Q, Σ, δ, q₀, F)
  - Propiedades: determinismo, minimalidad
  - Funcionamiento paso a paso
- Árboles de derivación
  - Definición y propiedades
  - Ejemplos visuales

**Sección 3: Arquitectura del Sistema** (2 págs)
- Diagrama de componentes ASCII
- Flujo de ejecución completo
- Interacción entre módulos

**Sección 4: Gramática Formal** (3 págs)
- Definición completa: G = (V, T, P, S)
- 9 producciones explicadas
- Alfabeto terminal (45 palabras organizadas)
- Justificación de cada regla
- Propiedades (no ambigua, no recursiva)

**Sección 5: Definición del Autómata** (4 págs)
- Especificación formal completa
- Tabla de transiciones detallada
- Diagrama de estados ASCII art
- Descripción de cada estado
- Justificación del diseño
- Propiedades del AFD

**Sección 6: Instalación y Uso** (2 págs)
- Requisitos (solo Python 3.7+)
- Instrucciones de ejecución
- Interfaz de usuario explicada

**Sección 7: Ejemplos y Casos de Prueba** (4 págs)
- 6 casos detallados con salidas completas
- Tabla de 8+ casos de prueba
- Oraciones válidas e inválidas
- Explicación de cada resultado

**Sección 8: Análisis de Complejidad** (3 págs)
- Temporal: O(n) demostrado
- Espacial: O(n) demostrado
- Comparación con versión completa
- 5 limitaciones del modelo identificadas

**Sección 9: Referencias** (1 pág)
- 4 libros fundamentales
- 3 artículos académicos
- Recursos online

**Sección 10: Conclusiones** (2 págs)
- Logros técnicos y pedagógicos
- Aplicación de conceptos teóricos
- Recomendaciones de uso

**🎓 Ideal para:**
- Presentaciones académicas
- Reportes de proyecto
- Aprendizaje de teoría de autómatas
- Entender conceptos fundamentales

---

### 2. REPORTE_TECNICO_SIMPLIFICADO.md

**📗 20 páginas | Análisis técnico profundo**

#### Contenido:

**Sección 1: Introducción** (2 págs)
- Motivación del diseño simplificado
- Diferencias con versión completa (tabla)

**Sección 2: Arquitectura del Sistema** (3 págs)
- Visión general (diagrama)
- Flujo de datos detallado
- Justificación de decisiones

**Sección 3: Componentes del Sistema** (5 págs)
- Clase AnalizadorSimple
  - Responsabilidades
  - Atributos (vocabulario)
  - Método analizar_oracion() (algoritmo)
- Clase AFDSimple
  - Definición formal
  - Método procesar_oracion() (algoritmo)
  - Métodos auxiliares

**Sección 4: Análisis Detallado** (3 págs)
- Gramática del lenguaje
- Tabla de transiciones del AFD
- Análisis de complejidad (temporal y espacial)

**Sección 5: Casos de Uso** (3 págs)
- Caso exitoso completo
- Caso fallido explicado
- Múltiples ejemplos

**Sección 6: Ventajas y Limitaciones** (2 págs)
- 4 ventajas principales
- 5 limitaciones identificadas

**Sección 7: Comparación con Versión Completa** (2 págs)
- Métricas de código
- Métricas de desempeño
- Métricas funcionales

**Sección 8: Guía de Extensión** (1 pág)
- Añadir palabras
- Añadir categorías
- Modificar el AFD

**Sección 9: Conclusiones** (1 pág)
- Logros técnicos y pedagógicos
- Recomendaciones de uso

**🔧 Ideal para:**
- Entender implementación técnica
- Análisis de decisiones de diseño
- Planear extensiones
- Comparar ambas versiones

---

### 3. REFERENCIA_API_SIMPLIFICADA.md

**📙 15 páginas | Documentación de código**

#### Contenido:

**Clase AnalizadorSimple**
- Constructor con todos los atributos
- Método analizar_oracion()
  - Parámetros detallados
  - Valor de retorno explicado
  - Ejemplos de uso
  - Casos especiales

**Clase AFDSimple**
- Constructor con definición formal
- Método procesar_oracion()
  - Flujo de ejecución
  - Ejemplo de salida completa
- Métodos privados
  - _transicion()
  - _generar_resultado()
  - _imprimir_arbol_derivacion()

**Función main()**
- Descripción de la interfaz
- Comandos disponibles

**Tipos de Datos**
- Diccionarios de resultado
- Categorías gramaticales
- Constantes del sistema

**Ejemplos Completos**
- Uso básico
- Análisis múltiple
- Solo análisis léxico
- Verificar vocabulario

**Mejores Prácticas**
- Reutilizar instancias
- Verificar resultados
- Extender vocabulario

**💻 Ideal para:**
- Desarrolladores usando el código
- Integración con otros sistemas
- Referencia rápida
- Ejemplos de implementación

---

## 📕 Versión Completa - Documentación

### 1. REPORTE_TECNICO.md

**📕 20 páginas | Arquitectura profesional**

#### Contenido:

**Sección 1-2: Introducción y Flujo**
- Propósito y alcance
- Tecnologías: spaCy, matplotlib, networkx
- Flujo end-to-end completo

**Sección 3: Fundamentos Teóricos**
- AFD aplicado
- Análisis con spaCy

**Sección 4-8: Módulos del Sistema**
- AFDOraciones (principal)
- AnalizadorOraciones (NLP con spaCy)
- VisualizadorArbol (PNG a color)
- GeneradorArbolDerivacion (gramática formal)

**Sección 9-11: Implementación**
- Estructuras de datos
- Diagramas del sistema
- Consideraciones de diseño

**🏭 Ideal para:**
- Análisis con NLP profesional
- Vocabulario ilimitado
- Visualización avanzada
- Producción/Investigación

---

### 2. REFERENCIA_MODULOS.md

**📔 15 páginas | API completa**

#### Contenido:

- Documentación de 4 clases principales
- Métodos con spaCy
- Generación de imágenes PNG
- Integración de módulos

**🔌 Ideal para:**
- API profesional
- Desarrollo avanzado
- Extensión del sistema

---

## 📊 Tabla Comparativa de Documentos

| Documento | Páginas | Teoría | Código | Ejemplos | Nivel |
|-----------|---------|--------|--------|----------|-------|
| **README_VERSION_SIMPLIFICADA** | 30 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | Básico |
| **REPORTE_TECNICO_SIMPLIFICADO** | 20 | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Intermedio |
| **REFERENCIA_API_SIMPLIFICADA** | 15 | ⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Práctico |
| **REPORTE_TECNICO** | 20 | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | Avanzado |
| **REFERENCIA_MODULOS** | 15 | ⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | Avanzado |

---

## 🗺️ Mapa de Navegación

### Para Proyecto Académico (Teoría de Autómatas)

```
START
  ↓
README_VERSION_SIMPLIFICADA.md
  ├─→ Sección 2: Fundamentos Teóricos      (Para entender teoría)
  ├─→ Sección 4: Gramática Formal          (Para tu reporte)
  ├─→ Sección 5: Definición del AFD        (Para diagramas)
  ├─→ Sección 7: Ejemplos                  (Para presentación)
  └─→ Sección 8: Análisis de Complejidad   (Para conclusiones)
  ↓
REPORTE_TECNICO_SIMPLIFICADO.md
  └─→ Sección 3: Componentes               (Para entender código)
  ↓
Código: version_simplificada.py
  └─→ Ejecutar y probar
```

### Para Desarrollo / Extensión

```
START
  ↓
REFERENCIA_API_SIMPLIFICADA.md
  ├─→ Clase AnalizadorSimple               (Para análisis léxico)
  ├─→ Clase AFDSimple                      (Para validación)
  └─→ Ejemplos Completos                   (Para implementar)
  ↓
REPORTE_TECNICO_SIMPLIFICADO.md
  └─→ Sección 8: Guía de Extensión         (Para modificar)
  ↓
Código: Modificar y extender
```

### Para Comparación de Versiones

```
START
  ↓
README_VERSION_SIMPLIFICADA.md (Sección 1)
  └─→ Tabla comparativa
  ↓
REPORTE_TECNICO_SIMPLIFICADO.md (Sección 7)
  └─→ Comparación detallada
  ↓
REPORTE_TECNICO.md
  └─→ Arquitectura versión completa
```

---

## 📖 Rutas de Lectura Sugeridas

### Ruta 1: Lectura Rápida (30 minutos)

```
1. README_VERSION_SIMPLIFICADA.md
   - Sección 1: Descripción (5 min)
   - Sección 4: Gramática (10 min)
   - Sección 5: AFD (10 min)
   - Sección 7: Ejemplos (5 min)

Total: ~30 páginas seleccionadas
```

### Ruta 2: Comprensión Completa (3 horas)

```
1. README_VERSION_SIMPLIFICADA.md (COMPLETO)     90 min
2. REPORTE_TECNICO_SIMPLIFICADO.md               60 min
3. REFERENCIA_API_SIMPLIFICADA.md                30 min

Total: ~65 páginas
```

### Ruta 3: Dominio Total (6 horas)

```
1. README_VERSION_SIMPLIFICADA.md                90 min
2. REPORTE_TECNICO_SIMPLIFICADO.md               60 min
3. REFERENCIA_API_SIMPLIFICADA.md                30 min
4. Código: version_simplificada.py               60 min
5. REPORTE_TECNICO.md                            60 min
6. Pruebas prácticas                             60 min

Total: ~95 páginas + práctica
```

---

## 🎓 Material para Entregables Académicos

### Para tu REPORTE ESCRITO:

**Estructura sugerida:**

```markdown
1. Portada
2. Índice
3. Resumen Ejecutivo
   └─ Tomar de: README_SIMPLIFICADA (inicio)

4. Introducción
   └─ Tomar de: README_SIMPLIFICADA (Sección 1)

5. Marco Teórico ⭐
   └─ Tomar de: README_SIMPLIFICADA (Sección 2 completa)

6. Diseño del Sistema
   ├─ Gramática: README_SIMPLIFICADA (Sección 4)
   ├─ AFD: README_SIMPLIFICADA (Sección 5)
   └─ Arquitectura: REPORTE_TECNICO_SIMPLIFICADO (Sección 2)

7. Implementación
   └─ Tomar de: REPORTE_TECNICO_SIMPLIFICADO (Sección 3)

8. Resultados y Análisis
   ├─ Casos de prueba: README_SIMPLIFICADA (Sección 7)
   └─ Complejidad: README_SIMPLIFICADA (Sección 8)

9. Conclusiones
   └─ Tomar de: README_SIMPLIFICADA (Sección 10)

10. Referencias
    └─ Tomar de: README_SIMPLIFICADA (Sección 9)

11. Anexos
    └─ Código fuente completo
```

**Total: ~40-50 páginas de reporte profesional**

---

### Para tu PRESENTACIÓN:

**Diapositivas sugeridas (15-20 slides):**

```
Slide 1: Portada
Slide 2: Objetivos
        └─ README_SIMPLIFICADA (Sección 1.2)

Slide 3-4: Fundamentos Teóricos
        ├─ Jerarquía de Chomsky
        └─ AFD (definición)
        └─ README_SIMPLIFICADA (Sección 2)

Slide 5: Gramática del Lenguaje
        └─ Mostrar G = (V, T, P, S)
        └─ README_SIMPLIFICADA (Sección 4)

Slide 6: Diagrama del AFD
        └─ Copiar diagrama ASCII
        └─ README_SIMPLIFICADA (Sección 5)

Slide 7-8: Ejemplos de Ejecución
        └─ Oración válida paso a paso
        └─ README_SIMPLIFICADA (Sección 7)

Slide 9: Demo en Vivo
        └─ Ejecutar version_simplificada.py

Slide 10-11: Resultados
        └─ Tabla de casos de prueba
        └─ Análisis de complejidad
        └─ README_SIMPLIFICADA (Sección 8)

Slide 12: Comparación de Versiones
        └─ REPORTE_TECNICO_SIMPLIFICADO (Sección 7)

Slide 13-14: Conclusiones
        └─ README_SIMPLIFICADA (Sección 10)

Slide 15: Referencias
```

---

## 🔍 Búsqueda por Tema

| Tema | Documento | Sección |
|------|-----------|---------|
| **Definición formal de gramática** | README_SIMPLIFICADA | 4 |
| **Especificación del AFD** | README_SIMPLIFICADA | 5 |
| **Jerarquía de Chomsky** | README_SIMPLIFICADA | 2.1 |
| **Árboles de derivación** | README_SIMPLIFICADA | 2.4 |
| **Complejidad temporal** | README_SIMPLIFICADA | 8 |
| **Tabla de transiciones** | REPORTE_TECNICO_SIMPLIFICADO | 4.2 |
| **Casos de prueba** | README_SIMPLIFICADA | 7 |
| **API de AnalizadorSimple** | REFERENCIA_API_SIMPLIFICADA | 1 |
| **API de AFDSimple** | REFERENCIA_API_SIMPLIFICADA | 2 |
| **Ejemplos de código** | REFERENCIA_API_SIMPLIFICADA | 4+ |
| **Guía de extensión** | REPORTE_TECNICO_SIMPLIFICADO | 8 |
| **Limitaciones del modelo** | README_SIMPLIFICADA | 8.2 |
| **Comparación de versiones** | REPORTE_TECNICO_SIMPLIFICADO | 7 |
| **Arquitectura con spaCy** | REPORTE_TECNICO | 4 |

---

## 📊 Estadísticas de Documentación

### Versión Simplificada

```
Total de páginas: ~65
├── README_VERSION_SIMPLIFICADA: 30 págs (46%)
├── REPORTE_TECNICO_SIMPLIFICADO: 20 págs (31%)
└── REFERENCIA_API_SIMPLIFICADA: 15 págs (23%)

Distribución de contenido:
├── Teoría: 45% (muy detallada)
├── Implementación: 30%
└── Ejemplos: 25%
```

### Versión Completa

```
Total de páginas: ~35
├── REPORTE_TECNICO: 20 págs (57%)
└── REFERENCIA_MODULOS: 15 págs (43%)

Distribución de contenido:
├── Teoría: 20%
├── Implementación: 50%
└── Ejemplos: 30%
```

---

## ✅ Checklist de Completitud

### Documentación Versión Simplificada

- [x] README completo con fundamentos teóricos
- [x] Reporte técnico detallado
- [x] Referencia de API completa
- [x] Gramática formal definida (G = (V, T, P, S))
- [x] AFD especificado (M = (Q, Σ, δ, q₀, F))
- [x] Árbol de derivación documentado
- [x] Casos de prueba (8+ ejemplos)
- [x] Análisis de complejidad (O-notation)
- [x] Referencias académicas (9 fuentes)
- [x] Ejemplos de código funcionales

### Documentación Versión Completa

- [x] Reporte técnico con arquitectura
- [x] Referencia de módulos
- [x] Integración con spaCy
- [x] Generación de imágenes PNG
- [x] Múltiples módulos especializados

---

## 🚀 Inicio Rápido

### Nuevo en el Proyecto?

```
1. Lee primero: README_VERSION_SIMPLIFICADA.md (Sección 1)
2. Ejecuta: python version_simplificada.py
3. Explora: REFERENCIA_API_SIMPLIFICADA.md
```

### Ya conoces Teoría de Autómatas?

```
1. Lee: REPORTE_TECNICO_SIMPLIFICADO.md
2. Consulta: REFERENCIA_API_SIMPLIFICADA.md
3. Modifica el código
```

### Quieres la Versión Profesional?

```
1. Lee: REPORTE_TECNICO.md
2. Instala dependencias: pip install -r requirements.txt
3. Ejecuta: python primer_AFD.py
```

---

## 📞 Ayuda y Soporte

### ¿No encuentras algo?

1. Usa Ctrl+F en este índice para buscar el tema
2. Consulta la tabla "Búsqueda por Tema"
3. Revisa el "Mapa de Navegación"

### ¿Qué versión elegir?

| Criterio | Versión Simplificada | Versión Completa |
|----------|---------------------|------------------|
| Aprendizaje | ✅ Mejor opción | ⚠️ Más compleja |
| Proyecto académico | ✅ Ideal | ✅ También funciona |
| Sin dependencias | ✅ Sí | ❌ Requiere instalación |
| Vocabulario | ⚠️ Limitado (45) | ✅ Ilimitado |
| Código entendible | ✅ Muy claro | ⚠️ Más complejo |

---

## 📝 Notas Finales

- **Versión simplificada:** Enfoque educativo y teórico
- **Versión completa:** Enfoque profesional y práctico
- **Ambas versiones:** Completamente funcionales y documentadas
- **Documentación total:** ~100 páginas
- **Cobertura:** 100% del código y teoría

---

**Autores:** Ricardo Méndez, Emiliano Ledesma
**Fecha:** Noviembre 2024
**Proyecto:** Analizador de Lenguaje Natural Simple

---

## 🎉 ¡Documentación Completa!

Tienes acceso a documentación exhaustiva para ambas versiones del proyecto. Cada documento está diseñado para un propósito específico y audiencia particular.

**¡Feliz lectura y codificación! 📚💻**
