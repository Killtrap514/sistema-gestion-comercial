from datetime import datetime
from archivos import cargar_datos, guardar_datos

ARCHIVO_PRODUCTOS = "productos.json"
ARCHIVO_INVENTARIO = "inventario.json"


def consultar_existencias():
  """Muestra el inventario actual de todos los productos y sus existencias."""
  productos = cargar_datos(ARCHIVO_PRODUCTOS)
  if not productos:
    print("\nNo hay productos registrados en el sistema.")
    return

  print("\n--- CONSULTA DE EXISTENCIAS ---")
  print(f"{'Código':<10} | {'Nombre':<20} | {'Disponible':<10} | {'Stock Mín.':<10} | {'Estado':<10}")
  print("-" * 68)
  for p in productos:
    stock_min = p["stock_minimo"]
    cantidad = p["cantidad"]
    alerta = "¡BAJO STOCK!" if cantidad <= stock_min else "Normal"
    print(
        f"{p['codigo']:<10} | {p['nombre']:<20} | {cantidad:<10} | {stock_min:<10} | {alerta:<10}"
    )


def registrar_entrada_inventario():
  """Registra una entrada de inventario aumentando las existencias de un producto."""
  productos = cargar_datos(ARCHIVO_PRODUCTOS)
  if not productos:
    print("\nNo hay productos registrados para actualizar.")
    return

  print("\n--- REGISTRO DE ENTRADA DE INVENTARIO ---")
  codigo = input("Ingrese el código del producto a reabastecer: ").strip()

  producto_encontrado = None
  for p in productos:
    if p["codigo"] == codigo:
      producto_encontrado = p
      break

  if not producto_encontrado:
    print("Error: No se encontró ningún producto con ese código.")
    return

  print(f"Producto seleccionado: {producto_encontrado['nombre']} (Stock actual: {producto_encontrado['cantidad']})")

  # Validar cantidad de entrada positiva
  while True:
    try:
      cantidad_entrada = int(input("Ingrese la cantidad que ingresa al inventario: "))
      if cantidad_entrada > 0:
        break
      print("La cantidad de entrada debe ser mayor a cero.")
    except ValueError:
      print("Error: Ingrese un número entero válido.")

  descripcion = input("Ingrese una descripción o motivo de la entrada (ej. Compra a proveedor): ").strip()

  # Actualizar la cantidad del producto
  producto_encontrado["cantidad"] += cantidad_entrada
  guardar_datos(ARCHIVO_PRODUCTOS, productos)

  # Registrar el movimiento en el historial
  registrar_movimiento(codigo, "ENTRADA", cantidad_entrada, descripcion)

  print(f"¡Inventario actualizado con éxito! Nuevo stock de '{producto_encontrado['nombre']}': {producto_encontrado['cantidad']}")


def registrar_movimiento(codigo, tipo, cantidad, descripcion):
  """Guarda un registro detallado en el historial de movimientos de inventario."""
  movimientos = cargar_datos(ARCHIVO_INVENTARIO)
  
  nuevo_movimiento = {
      "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
      "codigo_producto": codigo,
      "tipo_movimiento": tipo,  
      "cantidad": cantidad,
      "descripcion": descripcion,
  }

  movimientos.append(nuevo_movimiento)
  guardar_datos(ARCHIVO_INVENTARIO, movimientos)


def verificar_stock_minimo():
  """Identifica y muestra los productos que han alcanzado o están por debajo del stock mínimo."""
  productos = cargar_datos(ARCHIVO_PRODUCTOS)
  if not productos:
    print("\nNo hay productos registrados.")
    return

  print("\n--- PRODUCTOS CON ALERTA DE STOCK MÍNIMO ---")
  alerta_encontrada = False

  for p in productos:
    if p["cantidad"] <= p["stock_minimo"]:
      alerta_encontrada = True
      print(
          f"¡Alerta! Código: {p['codigo']} | Nombre: {p['nombre']} | Disponible: {p['cantidad']} | Stock Mínimo: {p['stock_minimo']}"
      )

  if not alerta_encontrada:
    print("Todos los productos se encuentran por encima del stock mínimo.")


def consultar_historial_movimientos():
  """Muestra el historial completo de movimientos de inventario almacenados."""
  movimientos = cargar_datos(ARCHIVO_INVENTARIO)
  if not movimientos:
    print("\nNo hay movimientos de inventario registrados todavía.")
    return

  print("\n--- HISTORIAL DE MOVIMIENTOS DE INVENTARIO ---")
  for m in movimientos:
    print(
        f"[{m['fecha']}] Tipo: {m['tipo_movimiento']} | Producto (Código): {m['codigo_producto']} | Cantidad: {m['cantidad']} | Desc: {m['descripcion']}"
    )