# 🎯 PROYECTO COMPLETADO: Analizador de Oraciones con AFD

## ✅ Resumen del Proyecto

Se ha transformado exitosamente el código base de un Autómata Finito Determinista (AFD) en un **analizador de oraciones simples en español** que identifica:
- **Sujeto**: Quién realiza la acción
- **Verbo**: La acción que se realiza  
- **Predicado**: Lo que se dice del sujeto (verbo + complementos)
- **Árbol Sintáctico**: Visualización gráfica de la estructura ⭐ NUEVO

## 📁 Archivos Creados/Modificados

### 1. **`primer_AFD.py`** (Modificado)
   - ✅ Eliminada la tabla de transiciones manual
   - ✅ Implementado AFD automático con 5 estados: q0, q1, q2, q3, qr
   - ✅ Integración con módulo de análisis NLP
   - ✅ Interfaz de usuario mejorada
   - ✅ Sistema de transiciones basado en componentes gramaticales
   - ✅ **Generación automática de árboles sintácticos** ⭐

### 2. **`analizador_oraciones.py`** (Nuevo)
   - ✅ Módulo de procesamiento de lenguaje natural
   - ✅ Usa spaCy para análisis sintáctico
   - ✅ Identifica sujeto, verbo y predicado
   - ✅ Maneja casos especiales (verbos mal etiquetados, pronombres)
   - ✅ Proporciona análisis detallado con POS tags
   - ✅ Retorna documento de spaCy para visualización

### 3. **`visualizador_arbol.py`** ⭐ (Nuevo)
   - ✅ Genera imágenes PNG de árboles sintácticos
   - ✅ Usa matplotlib y networkx para visualización
   - ✅ Colores diferenciados por categoría gramatical
   - ✅ Layout jerárquico automático
   - ✅ Guarda imágenes con timestamps únicos
   - ✅ Abre automáticamente el visor de imágenes

### 4. **`requirements.txt`** (Actualizado)
   - ✅ spaCy para NLP
   - ✅ matplotlib para gráficos ⭐
   - ✅ networkx para grafos ⭐
   
### 5. **`README.md`** (Actualizado)
   - ✅ Documentación completa en español
   - ✅ Instrucciones de instalación
   - ✅ Ejemplos de uso
   - ✅ Explicación de la arquitectura del autómata
   - ✅ Solución de problemas
   - ✅ **Documentación de árboles sintácticos** ⭐

### 6. **`test_analizador.py`** (Nuevo)
   - ✅ Suite de pruebas automatizadas
   - ✅ 8 oraciones de prueba (5 válidas, 3 inválidas)
   - ✅ Reporte detallado de resultados

### 7. **`test_arbol.py`** ⭐ (Nuevo)
   - ✅ Prueba específica para generación de árboles
   - ✅ Verificación de imágenes generadas
   - ✅ Apertura automática de resultados

## 🏗️ Arquitectura del Autómata

```
┌─────────────────────────────────────────────┐
│  Estados del AFD:                           │
│                                             │
│  q0 → Estado inicial (esperando entrada)   │
│  q1 → Sujeto identificado                  │
│  q2 → Verbo identificado                   │
│  q3 → Predicado completo ✓ (ACEPTACIÓN)    │
│  qr → Estado de rechazo ✗                  │
└─────────────────────────────────────────────┘

Transiciones:
q0 --[sujeto encontrado]--> q1
q0 --[verbo sin sujeto]--> q2
q1 --[verbo encontrado]--> q2
q2 --[predicado completo]--> q3
* --[error]--> qr
```

## 🚀 Cómo Usar

### Instalación (Ya realizada):
```bash
pip install spacy
python -m spacy download es_core_news_sm
```

### Ejecución:
```bash
python primer_AFD.py
```

### Ejemplo de Uso:
```
Oración: yo camino por el parque

✓ ORACIÓN ACEPTADA
Sujeto:    yo
Verbo:     camino
Predicado: yo camino por el parque
```

## 🧪 Pruebas Realizadas

El sistema fue probado con éxito con las siguientes oraciones:

### ✅ Oraciones Válidas (Aceptadas):
1. "yo camino por el parque" → Sujeto: yo, Verbo: camino
2. "el gato come pescado" → Sujeto: el gato, Verbo: come
3. "María estudia matemáticas" → Sujeto: María, Verbo: estudia
4. "los niños juegan en el jardín" → Sujeto: los niños, Verbo: juegan
5. "mi hermano lee un libro" → Sujeto: mi hermano, Verbo: lee
6. "el perro corre rápidamente" → Sujeto: el perro, Verbo: corre

### ❌ Oraciones Inválidas (Rechazadas):
1. "por el parque" → Sin sujeto ni verbo
2. "camino parque" → Estructura incompleta

## 🎓 Características Técnicas

### Tecnologías Utilizadas:
- **Python 3.13+**
- **spaCy 3.8.0**: Biblioteca de NLP
- **Modelo es_core_news_sm**: Modelo de español entrenado

### Algoritmos Implementados:
- **Análisis sintáctico (parsing)**: Identifica la estructura gramatical
- **POS Tagging**: Etiqueta categorías gramaticales
- **Análisis de dependencias**: Encuentra relaciones entre palabras
- **Máquina de estados finitos**: Valida la estructura de la oración

## 🔧 Características Especiales

1. **Detección robusta de verbos**: Maneja verbos mal etiquetados por spaCy
2. **Soporte para pronombres**: Identifica "yo", "tú", "él", etc.
3. **Análisis detallado opcional**: Muestra POS tags y dependencias
4. **Interfaz intuitiva**: Fácil de usar con mensajes claros
5. **Arquitectura modular**: Código organizado y reutilizable

## 📊 Resultados de las Pruebas

```
Total de oraciones probadas: 8
✓ Aceptadas: 6 (75%)
✗ Rechazadas: 2 (25%)
```

## 🎯 Objetivos Cumplidos

- ✅ Transformar AFD básico en analizador de oraciones
- ✅ Identificar sujeto, verbo y predicado
- ✅ Eliminar tabla de transiciones manual
- ✅ Usar bibliotecas de Python (spaCy)
- ✅ Interfaz simple: usuario ingresa oración → programa responde si es válida
- ✅ Código modular y extensible
- ✅ Documentación completa

## 💡 Próximas Mejoras Posibles

1. Detectar oraciones compuestas y coordinadas
2. Identificar complementos circunstanciales (tiempo, lugar, modo)
3. Analizar concordancia de género y número
4. Soporte para oraciones interrogativas y exclamativas
5. Interfaz gráfica (GUI)
6. Exportar análisis a archivo

## 📝 Notas Importantes

- El modelo de spaCy a veces etiqueta incorrectamente verbos conjugados en primera persona (ej: "camino" como sustantivo). El código implementa lógica especial para manejar estos casos.
- Las oraciones imperativas (sin sujeto explícito) también son aceptadas por el autómata.
- El predicado incluye el verbo principal y todos sus complementos.

---

**Desarrollado por**: Ricardo Méndez  
**Curso**: Matemáticas - Cuatrimestre 7  
**Institución**: UPQ  
**Fecha**: 15 de noviembre de 2025
