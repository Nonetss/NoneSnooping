import json

from ollama import chat

# Cargar el archivo de entrada
with open("salida.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Archivo de salida
output_file = "clasificado.json"
classified_data = []

# Categorías permitidas
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


# Función para validar la categoría
def is_valid_category(category):
    return category in categories


# Procesar cada objeto del archivo de entrada
for idx, item in enumerate(data):  # Trabajar con todos los objetos
    print(f"Procesando elemento {idx + 1}...")
    try:
        classification = ""
        invalid_attempts = 0

        while not is_valid_category(classification):
            # Crear el mensaje para enviar al modelo
            if invalid_attempts == 0:
                user_message = (
                    f"Clasifica este contenido:\n\n"
                    f"Título: {item.get('titulo', 'Sin título')}\n"
                    f"Contenido: {item.get('contenido', ['Sin contenido'])[0]}\n\n"
                    "Responde únicamente con el nombre de la categoría."
                )
            else:
                user_message = (
                    f"La categoría que diste no es válida: '{classification}'.\n"
                    f"Por favor, selecciona una categoría de esta lista:\n"
                    f"{', '.join(categories)}\n\n"
                    f"Clasifica nuevamente:\n"
                    f"Título: {item.get('titulo', 'Sin título')}\n"
                    f"Contenido: {item.get('contenido', ['Sin contenido'])[0]}\n\n"
                    "Responde únicamente con el nombre de la categoría."
                )

            messages = [
                {
                    "role": "system",
                    "content": (
                        "Eres un modelo especializado en clasificar contenido en las siguientes categorías: "
                        f"{', '.join(categories)}. "
                        "Tu tarea es leer el título y contenido proporcionados y seleccionar la categoría más adecuada. "
                        "Responde únicamente con el nombre de la categoría."
                    ),
                },
                {
                    "role": "user",
                    "content": user_message,
                },
            ]

            # Enviar al modelo de Ollama
            response = chat(model="llama3.2", messages=messages)

            # Extraer la clasificación del contenido
            classification = response.message.content.strip()
            invalid_attempts += 1

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
