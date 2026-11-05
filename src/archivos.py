import json
import os


def guardar_datos(nombre_archivo, datos):
  """Guarda una lista o diccionario en un archivo JSON."""
  try:
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
      json.dump(datos, archivo, indent=4, ensure_ascii=False)
  except Exception as e:
    print(f"Error al guardar el archivo {nombre_archivo}: {e}")


def cargar_datos(nombre_archivo):
  """Carga los datos desde un archivo JSON. Si no existe, retorna una lista vacía."""
  if not os.path.exists(nombre_archivo):
    return []
  try:
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
      return json.load(archivo)
  except Exception as e:
    print(f"Error al cargar el archivo {nombre_archivo}: {e}")
    return []