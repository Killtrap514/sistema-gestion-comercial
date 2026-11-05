from archivos import cargar_datos, guardar_datos

ARCHIVO_PRODUCTOS = "productos.json"


def registrar_producto():
  productos = cargar_datos(ARCHIVO_PRODUCTOS)

  print("\n--- REGISTRO DE NUEVO PRODUCTO ---")
  codigo = input("Ingrese el código del producto: ").strip()

  # Verificar si el código ya existe
  for p in productos:
    if p["codigo"] == codigo:
      print("Error: Ya existe un producto con ese código.")
      return

  nombre = input("Ingrese el nombre del producto: ").strip()
  categoria = input("Ingrese la categoría: ").strip()

  # Validar precio positivo
  while True:
    try:
      precio = float(input("Ingrese el precio de venta: "))
      if precio > 0:
        break
      print("El precio debe ser mayor a 0.")
    except ValueError:
      print("Error: Ingrese un número válido.")

  # Validar cantidad positiva o cero
  while True:
    try:
      cantidad = int(input("Ingrese la cantidad disponible: "))
      if cantidad >= 0:
        break
      print("La cantidad no puede ser negativa.")
    except ValueError:
      print("Error: Ingrese un número entero válido.")

  # Validar stock mínimo
  while True:
    try:
      stock_minimo = int(input("Ingrese el stock mínimo: "))
      if stock_minimo >= 0:
        break
      print("El stock mínimo no puede ser negativo.")
    except ValueError:
      print("Error: Ingrese un número entero válido.")

  nuevo_producto = {
      "codigo": codigo,
      "nombre": nombre,
      "categoria": categoria,
      "precio": precio,
      "cantidad": cantidad,
      "stock_minimo": stock_minimo,
      "activo": True,
  }

  productos.append(nuevo_producto)
  guardar_datos(ARCHIVO_PRODUCTOS, productos)
  print("¡Producto registrado con éxito!")


def listar_productos():
  productos = cargar_datos(ARCHIVO_PRODUCTOS)
  if not productos:
    print("\nNo hay productos registrados.")
    return

  print("\n--- LISTADO DE PRODUCTOS ---")
  for p in productos:
    estado = "Activo" if p.get("activo", True) else "Inactivo"
    print(
        f"Código: {p['codigo']} | Nombre: {p['nombre']} | Cat: {p['categoria']}"
        f" | Precio: Q{p['precio']:.2f} | Stock: {p['cantidad']} | Min:"
        f" {p['stock_minimo']} | Estado: {estado}"
    )


def consultar_producto():
  productos = cargar_datos(ARCHIVO_PRODUCTOS)
  codigo = input(
      "\nIngrese el código del producto que desea consultar: "
  ).strip()

  for p in productos:
    if p["codigo"] == codigo:
      print("\n--- PRODUCTO ENCONTRADO ---")
      print(f"Código: {p['codigo']}")
      print(f"Nombre: {p['nombre']}")
      print(f"Categoría: {p['categoria']}")
      print(f"Precio de venta: Q{p['precio']:.2f}")
      print(f"Cantidad disponible: {p['cantidad']}")
      print(f"Stock mínimo: {p['stock_minimo']}")
      return

  print("No se encontró ningún producto con ese código.")