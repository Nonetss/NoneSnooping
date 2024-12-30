import json
import os

# Cargar el archivo clasificado.json
with open("clasificado.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Crear una carpeta para los archivos clasificados
output_folder = "clasificados_por_categoria"
os.makedirs(output_folder, exist_ok=True)

# Agrupar los datos por categoría
grouped_data = {}
for item in data:
    category = item.get("clasificacion", "Otros").strip()
    category = category.replace(" ", "_").replace("/", "_").lower()
    if category not in grouped_data:
        grouped_data[category] = []
    grouped_data[category].append(item)

# Guardar cada categoría en un archivo separado
for category, items in grouped_data.items():
    filename = f"{category}.json"
    filepath = os.path.join(output_folder, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=4)

    print(f"Archivo creado para la categoría '{category}': {filepath}")

print(
    f"\nTodos los archivos clasificados se han guardado en la carpeta: {output_folder}"
)
