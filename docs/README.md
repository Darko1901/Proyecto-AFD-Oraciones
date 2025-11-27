# Documentación del Proyecto - Analizador de Oraciones con AFD

## 📚 Índice de Documentación

Este directorio contiene toda la documentación técnica y teórica del proyecto de análisis de oraciones mediante autómatas finitos deterministas.

---

## 📄 Documentos Disponibles

### 1. **README_VERSION_SIMPLIFICADA.md** 📘
**Documentación completa de la versión simplificada**

- ✅ Fundamentos teóricos detallados
- ✅ Gramática formal completa
- ✅ Definición matemática del AFD
- ✅ Ejemplos de casos de prueba
- ✅ Análisis de complejidad
- ✅ Conceptos de lenguajes formales
- ✅ Árboles de derivación

**Recomendado para:**
- Estudiantes aprendiendo teoría de autómatas
- Presentaciones académicas
- Entender los conceptos fundamentales
- Proyecto con enfoque educativo

**Tamaño:** ~150KB | **Páginas:** ~30

---

### 2. **REPORTE_TECNICO.md** 📗
**Reporte técnico de la versión completa con spaCy**

- ✅ Arquitectura completa del sistema
- ✅ Módulos y componentes
- ✅ Flujo end-to-end
- ✅ Análisis con NLP profesional
- ✅ Visualización avanzada (PNG)
- ✅ Estructuras de datos

**Recomendado para:**
- Desarrolladores que quieren extender el proyecto
- Entender la implementación con spaCy
- Análisis profesional de oraciones
- Proyecto con enfoque técnico

**Tamaño:** ~80KB | **Páginas:** ~20

---

### 3. **REFERENCIA_MODULOS.md** 📙
**Referencia técnica de módulos y APIs**

- ✅ Documentación de clases
- ✅ Métodos y funciones
- ✅ Parámetros y retornos
- ✅ Ejemplos de uso

**Recomendado para:**
- Desarrolladores usando el código
- Referencia rápida de APIs
- Integración con otros sistemas

---

## 🎯 ¿Qué Documentación Leer?

### Si eres estudiante o estás aprendiendo teoría:
👉 **Comienza con: `README_VERSION_SIMPLIFICADA.md`**

**Razones:**
- Fundamentos teóricos explicados desde cero
- Conceptos matemáticos formales
- Ejemplos pedagógicos
- Sin dependencias complejas

**Ruta de aprendizaje:**
1. Leer sección "Fundamentos Teóricos" (páginas 1-10)
2. Estudiar la gramática formal (páginas 11-15)
3. Analizar el AFD (páginas 16-20)
4. Probar ejemplos (páginas 21-25)

---

### Si eres desarrollador o quieres implementación profesional:
👉 **Comienza con: `REPORTE_TECNICO.md`**

**Razones:**
- Arquitectura completa del sistema
- Uso de bibliotecas profesionales (spaCy)
- Análisis NLP robusto
- Visualización avanzada

**Ruta de aprendizaje:**
1. Entender la arquitectura (sección 4)
2. Revisar módulos principales (secciones 5-8)
3. Analizar flujo de ejecución (sección 2)
4. Consultar referencia de APIs (`REFERENCIA_MODULOS.md`)

---

### Si quieres comparar ambas versiones:
👉 **Lee ambos documentos en paralelo**

| Aspecto | Versión Simplificada | Versión Completa |
|---------|---------------------|------------------|
| **Teoría** | Profunda y detallada | Aplicada |
| **Código** | ~370 líneas | ~1,115 líneas |
| **Dependencias** | Ninguna | spaCy, matplotlib, networkx |
| **Vocabulario** | 45 palabras | Ilimitado |
| **Árbol visual** | ASCII | PNG a color |
| **Enfoque** | Educativo | Profesional |

---

## 📖 Contenido de cada Documento

### README_VERSION_SIMPLIFICADA.md

```
1. Descripción General
   - Objetivo del proyecto
   - Características principales
   - ¿Por qué una versión simplificada?

2. Fundamentos Teóricos (⭐ MÁS EXTENSO)
   - Lenguajes formales
   - Jerarquía de Chomsky
   - Gramáticas independientes del contexto
   - Autómatas finitos deterministas
   - Árboles de derivación

3. Arquitectura del Sistema
   - Diagrama de componentes
   - Flujo de ejecución

4. Gramática Formal
   - Definición completa G = (V, T, P, S)
   - Explicación de producciones
   - Alfabeto terminal (vocabulario)

5. Definición del Autómata
   - Especificación formal M = (Q, Σ, δ, q₀, F)
   - Tabla de transiciones
   - Diagrama de estados
   - Justificación del diseño

6. Instalación y Uso
   - Requisitos
   - Ejecución
   - Interfaz de usuario

7. Ejemplos y Casos de Prueba
   - 6 casos detallados
   - Tabla de resultados

8. Análisis de Complejidad
   - Temporal: O(n)
   - Espacial: O(n)
   - Comparación con versión completa

9. Limitaciones y Trabajo Futuro
   - 5 limitaciones identificadas
   - Plan de extensiones

10. Conclusiones y Referencias
```

---

### REPORTE_TECNICO.md

```
1. Introducción
   - Propósito del documento
   - Alcance del proyecto
   - Tecnologías utilizadas

2. Flujo de Interacción End-to-End
   - Desde la entrada hasta la salida
   - Diagramas de secuencia

3. Fundamentos Teóricos
   - Conceptos de AFD
   - Análisis sintáctico con spaCy

4. Arquitectura del Sistema
   - Módulos principales
   - Dependencias

5-8. Módulos Individuales
   - AFDOraciones
   - AnalizadorOraciones
   - VisualizadorArbol
   - GeneradorArbolDerivacion

9. Estructuras de Datos
   - Formato de resultados
   - Objetos y diccionarios

10. Diagramas del Sistema
    - Arquitectura visual
    - Flujo de datos

11. Consideraciones de Diseño
    - Decisiones técnicas
    - Trade-offs

12. Anexos
    - Código de ejemplo
    - Configuraciones
```

---

## 🔍 Búsqueda Rápida por Tema

| Tema | Documento | Sección |
|------|-----------|---------|
| **Definición formal de gramática** | README_VERSION_SIMPLIFICADA | Sección 4 |
| **Especificación del AFD** | README_VERSION_SIMPLIFICADA | Sección 5 |
| **Jerarquía de Chomsky** | README_VERSION_SIMPLIFICADA | Sección 2.1 |
| **Árboles de derivación** | README_VERSION_SIMPLIFICADA | Sección 2.4 |
| **Complejidad algorítmica** | README_VERSION_SIMPLIFICADA | Sección 8 |
| **Arquitectura con spaCy** | REPORTE_TECNICO | Sección 4 |
| **Visualización PNG** | REPORTE_TECNICO | Sección 7 |
| **API de módulos** | REFERENCIA_MODULOS | Todo |
| **Casos de prueba** | README_VERSION_SIMPLIFICADA | Sección 7 |
| **Instalación** | README_VERSION_SIMPLIFICADA | Sección 6 |

---

## 🎓 Material Académico

### Para Presentaciones

**Diapositivas sugeridas:**

1. **Introducción** (README_SIMPLIFICADA, Sección 1)
   - Objetivo del proyecto
   - Características

2. **Fundamentos Teóricos** (README_SIMPLIFICADA, Sección 2)
   - Lenguajes formales
   - Gramáticas tipo 2
   - AFD

3. **Gramática del Lenguaje** (README_SIMPLIFICADA, Sección 4)
   - Mostrar G = (V, T, P, S)
   - Ejemplos de producciones

4. **Autómata Finito** (README_SIMPLIFICADA, Sección 5)
   - Diagrama de estados
   - Tabla de transiciones

5. **Demo en Vivo** (Código en version_simplificada.py)
   - Ejecutar ejemplos
   - Mostrar árboles ASCII

6. **Resultados** (README_SIMPLIFICADA, Sección 8)
   - Casos de prueba
   - Análisis de complejidad

7. **Conclusiones** (README_SIMPLIFICADA, Sección 10)

---

### Para Reportes Escritos

**Estructura recomendada:**

```
1. Portada
2. Índice
3. Resumen Ejecutivo (README_SIMPLIFICADA, inicio)
4. Introducción (README_SIMPLIFICADA, Sección 1)
5. Marco Teórico (README_SIMPLIFICADA, Sección 2)
6. Diseño del Sistema (README_SIMPLIFICADA, Secciones 3-5)
7. Implementación (Code + README_SIMPLIFICADA, Sección 6)
8. Resultados (README_SIMPLIFICADA, Secciones 7-8)
9. Conclusiones (README_SIMPLIFICADA, Sección 10)
10. Referencias (README_SIMPLIFICADA, Sección 9)
11. Anexos (Código fuente)
```

---

## 🛠️ Guías de Uso

### Ejecutar la Versión Simplificada

```bash
cd Proyecto-AFD-Oraciones
python version_simplificada.py
```

**Sin dependencias**, solo Python estándar.

---

### Ejecutar la Versión Completa

```bash
# Instalar dependencias
pip install -r requirements.txt
python -m spacy download es_core_news_sm

# Ejecutar
python primer_AFD.py
```

**Con NLP profesional** y visualización PNG.

---

## 📊 Comparación Visual

```
┌─────────────────────────────────────────────────────────────┐
│                   VERSIÓN SIMPLIFICADA                      │
├─────────────────────────────────────────────────────────────┤
│ ✅ Sin dependencias                                         │
│ ✅ Código educativo (~370 líneas)                           │
│ ✅ Fundamentos teóricos profundos                           │
│ ✅ Árboles ASCII                                            │
│ ✅ Gramática formal explícita                               │
│ ✅ AFD minimalista (5 estados)                              │
│ ⚠️ Vocabulario limitado (45 palabras)                       │
│                                                             │
│ 📖 Documentación: README_VERSION_SIMPLIFICADA.md           │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                   VERSIÓN COMPLETA                          │
├─────────────────────────────────────────────────────────────┤
│ ✅ NLP profesional con spaCy                                │
│ ✅ Vocabulario ilimitado                                    │
│ ✅ Visualización PNG a color                                │
│ ✅ Análisis robusto                                         │
│ ✅ Múltiples módulos especializados                         │
│ ⚠️ Dependencias externas (3)                                │
│ ⚠️ Más complejo (~1,115 líneas)                             │
│                                                             │
│ 📖 Documentación: REPORTE_TECNICO.md                       │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔗 Enlaces Útiles

### Dentro del Proyecto

- [Código Simplificado](../version_simplificada.py)
- [Código Completo](../primer_AFD.py)
- [Analizador](../analizador_oraciones.py)
- [Visualizador](../visualizador_arbol.py)
- [Generador de Derivación](../generador_arbol_derivacion.py)

### Recursos Externos

- [Teoría de Autómatas - Wikipedia](https://en.wikipedia.org/wiki/Automata_theory)
- [Gramáticas Independientes del Contexto](https://en.wikipedia.org/wiki/Context-free_grammar)
- [spaCy Documentation](https://spacy.io/)
- [Python Documentation](https://docs.python.org/3/)

---

## 📝 Notas de Versión

### Versión 1.0 (Noviembre 2024)

**Versión Simplificada:**
- ✅ Implementación completa
- ✅ Documentación exhaustiva
- ✅ Casos de prueba validados
- ✅ Análisis teórico profundo

**Versión Completa:**
- ✅ Integración con spaCy
- ✅ Generación de árboles PNG
- ✅ Árboles de derivación duales
- ✅ Tests automatizados

---

## 👥 Autores

**Ricardo Méndez**
**Emiliano Ledesma**

---

## 📧 Contacto y Soporte

Para preguntas sobre la documentación:

1. Revisar el documento correspondiente
2. Consultar los ejemplos de código
3. Analizar los casos de prueba

---

## 📄 Licencia

Proyecto de **uso académico y educativo**.

---

**Última actualización:** Noviembre 2024

---

## 🎯 Resumen para Lectura Rápida

**Si tienes 5 minutos:**
- Lee el resumen ejecutivo de `README_VERSION_SIMPLIFICADA.md` (primeras 2 páginas)
- Mira el diagrama del AFD (sección 5)
- Revisa 2-3 ejemplos (sección 7)

**Si tienes 30 minutos:**
- Lee completa la sección 2 (Fundamentos Teóricos)
- Estudia las secciones 4 y 5 (Gramática y AFD)
- Ejecuta el código y prueba ejemplos

**Si tienes 2 horas:**
- Lee `README_VERSION_SIMPLIFICADA.md` completo
- Ejecuta ambas versiones del código
- Compara implementaciones
- Analiza el código fuente

**Si quieres dominar el tema:**
- Lee ambos documentos completos
- Estudia el código línea por línea
- Implementa tus propias extensiones
- Crea casos de prueba adicionales

---

**¡Feliz lectura! 📚**
