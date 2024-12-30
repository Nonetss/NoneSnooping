import json

from ollama import chat

# Cargar el archivo de entrada
with open("salida.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Archivo de salida
output_file = "clasificado.json"
classified_data = []

# Categorías disponibles
categories = [
    "Problemas y Desafíos",
    "Demanda de Servicios o Productos",
    "Ideas y Proyectos Emprendedores",
    "Tendencias del Mercado",
    "Oportunidades de Colaboración o Networking",
    "Sugerencias para Mejorar Procesos o Productos",
    "Casos de Éxito o Fracaso",
    "Otros",
]

# Procesar cada objeto del archivo de entrada
for idx, item in enumerate(data):  # Trabajar con todos los objetos
    print(f"Procesando elemento {idx + 1}...")
    try:

        # Crear el mensaje para enviar al modelo
        messages = [
            {
                "role": "system",
                "content": (
                    "Eres un modelo especializado en clasificar contenido en las siguientes categorías: "
                    "Problemas y Desafíos, "
                    "Demanda de Servicios o Productos, "
                    "Ideas y Proyectos Emprendedores, "
                    "Tendencias del Mercado, "
                    "Oportunidades de Colaboración o Networking, "
                    "Sugerencias para Mejorar Procesos o Productos, "
                    "Casos de Éxito o Fracaso, "
                    "Otros. "
                    "Tu tarea es leer el título y contenido proporcionados y seleccionar la categoría más adecuada, presta muchísima atención"
                    "de esta lista. Responde únicamente con el nombre de la categoría, sin explicaciones ni comentarios adicionales."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Clasifica este contenido:\n\n"
                    f"Título: {item.get('titulo', 'Sin título')}.\n"
                    f"Contenido: {item.get('contenido', ['Sin contenido'])[0]}.\n\n"
                    "Responde únicamente con el nombre de la categoría."
                ),
            },
        ]

        # Enviar al modelo de Ollama
        response = chat(model="llama3.2", messages=messages)

        # Extraer la clasificación del contenido
        classification = response.message.content.strip()

        # Añadir la clasificación al objeto
        item["clasificacion"] = classification

        # Agregar al archivo clasificado
        classified_data.append(item)

        # Guardar resultados parciales en el archivo de salida
        with open(output_file, "w", encoding="utf-8") as out_f:
            json.dump(classified_data, out_f, ensure_ascii=False, indent=4)

        print(f"Elemento {idx + 1} clasificado como: {classification}")

    except Exception as e:
        print(f"Error procesando el elemento {idx + 1}: {e}")

print(f"\nClasificación completada. Resultados guardados en {output_file}.")
