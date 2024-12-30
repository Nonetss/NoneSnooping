# **NoneSnooping**

## Descripción del Proyecto

**NoneSnooping** es un proyecto de scraping que utiliza Scrapy para extraer información de páginas web y categorizar el contenido en diferentes clasificaciones. Posteriormente, se organiza y almacena en archivos JSON según su categoría para facilitar su análisis.

El objetivo principal del proyecto es estructurar contenido extraído, como ideas y debates, en categorías predefinidas, y potencialmente analizarlo para identificar oportunidades de negocio u otras aplicaciones informáticas.

---

## Características

- **Scraping Automatizado**: Extrae datos de Forocoches u otros sitios configurados.
- **Clasificación Basada en IA**: Utiliza modelos de lenguaje para categorizar contenido.
- **Organización por Categorías**: Divide el contenido en archivos JSON según su categoría.
- **Escalabilidad**: Diseñado para ser ampliable a otras webs con facilidad.

---

## Posibles Mejoras

- **Puntuación de Relevancia**: Añadir una funcionalidad que permita al usuario definir qué tipo de datos busca y que la IA asigne una puntuación del 1 al 10 a cada entrada, reduciendo progresivamente el conjunto de datos y destacando los resultados más relevantes. Evidentemente, este enfoque implica una pérdida de información, pero resulta necesario cuando se trabaja con cantidades de datos inmensas, ya que priorizar lo más relevante es fundamental para un análisis eficiente.
