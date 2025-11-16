# 🎨 NUEVA FUNCIONALIDAD: Árboles Sintácticos Visuales

## ✅ ¿Qué se agregó?

Se implementó la **generación automática de árboles sintácticos visuales** que se crean cada vez que una oración es aceptada por el autómata.

## 🌟 Características de los Árboles Sintácticos

### Visualización Gráfica
- 📊 **Grafos jerárquicos** que muestran la estructura de la oración
- 🎨 **Nodos coloreados** según la categoría gramatical:
  - 🔴 Rojo → Verbos
  - 🔵 Turquesa → Sustantivos
  - 🟢 Verde → Pronombres
  - 🟠 Rosa → Adjetivos
  - 🟣 Morado → Adverbios
  - 🟡 Amarillo → Determinantes

### Información en los Nodos
Cada nodo muestra:
1. **Palabra** (el token)
2. **[POS]** (categoría gramatical)
3. **(DEP)** (tipo de dependencia)

### Características Técnicas
- ✅ Imágenes en formato PNG de alta resolución (300 DPI)
- ✅ Guardado automático con timestamp único
- ✅ Apertura automática del visor de imágenes del sistema
- ✅ Organización en carpeta dedicada `arboles_sintacticos/`

## 📦 Nuevas Dependencias Instaladas

```bash
matplotlib>=3.5.0   # Para generación de gráficos
networkx>=2.6.0     # Para estructuras de grafos
```

## 🆕 Nuevos Archivos

### 1. `visualizador_arbol.py`
Módulo completo para generación de árboles sintácticos:
- Clase `VisualizadorArbol` con métodos para:
  - Generar grafos dirigidos
  - Calcular posiciones jerárquicas
  - Colorear nodos según POS tags
  - Guardar imágenes
  - Abrir visor automáticamente

### 2. `test_arbol.py`
Script de prueba específico para árboles sintácticos.

### 3. Carpeta `arboles_sintacticos/`
Directorio donde se guardan todas las imágenes generadas.

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
GENERANDO ÁRBOL SINTÁCTICO...
----------------------------------------------------------------------
✓ Árbol sintáctico generado: arboles_sintacticos/arbol_20251116_171003.png

----------------------------------------------------------------------
¿Deseas abrir el árbol sintáctico? (s/n): s
```

### Prueba Rápida

```bash
python test_arbol.py
```

Este script:
1. Analiza una oración de prueba
2. Genera el árbol sintáctico
3. Abre la imagen automáticamente

## 📊 Ejemplo Visual

Para la oración: **"el gato come pescado"**

El árbol muestra:

```
         [come (VERB, ROOT)]
                |
    ┌───────────┴───────────┐
    |                       |
[gato (NOUN)]         [pescado (NOUN)]
    |
[el (DET)]
```

Con colores y etiquetas detalladas en la imagen PNG.

## 🎯 Integración con el AFD

El árbol sintáctico se genera **SOLO** cuando:
1. ✅ La oración es **aceptada** por el autómata (estado q3)
2. ✅ El análisis NLP es **válido**

Si la oración es rechazada, no se genera el árbol.

## 📁 Ubicación de Archivos

Todas las imágenes se guardan en:
```
Proyecto_AFD_Oraciones/
└── arboles_sintacticos/
    ├── arbol_20251116_171003.png
    ├── arbol_20251116_171205.png
    └── arbol_20251116_171345.png
    ...
```

El nombre incluye fecha y hora para evitar sobrescribir archivos.

## 🔧 Personalización

Puedes modificar los colores editando el diccionario `colores` en `visualizador_arbol.py`:

```python
colores = {
    'VERB': '#FF6B6B',    # Cambiar color de verbos
    'NOUN': '#4ECDC4',    # Cambiar color de sustantivos
    # ...
}
```

## 🎓 Uso Académico

Los árboles sintácticos generados son perfectos para:
- 📚 Estudiar estructuras gramaticales
- 📝 Incluir en presentaciones o reportes
- 🔍 Visualizar dependencias sintácticas
- 👨‍🏫 Material didáctico para enseñanza

## ⚡ Rendimiento

- Generación de árbol: ~1-2 segundos
- Tamaño de imagen: ~200-400 KB
- Resolución: 300 DPI (calidad de impresión)

---

**¡La funcionalidad de árboles sintácticos está completamente implementada y lista para usar!** 🎉
