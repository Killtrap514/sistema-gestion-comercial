from datetime import datetime
from archivos import cargar_datos, guardar_datos
from inventario import registrar_movimiento

ARCHIVO_PRODUCTOS = "productos.json"
ARCHIVO_VENTAS = "ventas.json"


def registrar_venta():
  """Permite registrar una venta con varios productos, calculando subtotales, IVA y total."""
  productos = cargar_datos(ARCHIVO_PRODUCTOS)
  if not productos:
    print("\nNo hay productos registrados en el sistema para realizar ventas.")
    return

  print("\n--- NUEVO REGISTRO DE VENTA ---")
  carrito = []

  # Ciclo para agregar productos a la venta
  while True:
    codigo = input("\nIngrese el código del producto que desea vender (o escriba 'fin' para terminar): ").strip()
    
    if codigo.lower() == "fin":
      break

    # Verificar que el producto exista y esté activo
    producto_encontrado = None
    for p in productos:
      if p["codigo"] == codigo:
        if not p.get("activo", True):
          print("Error: Este producto se encuentra inactivo y no está disponible para la venta.")
          producto_encontrado = "inactivo"
        else:
          producto_encontrado = p
        break

    if producto_encontrado == "inactivo":
      continue
    elif not producto_encontrado:
      print("Error: No se encontró ningún producto con ese código.")
      continue

    print(f"Producto: {producto_encontrado['nombre']} | Precio: Q{producto_encontrado['precio']:.2f} | Stock disponible: {producto_encontrado['cantidad']}")

    # Validar que la cantidad sea positiva
    while True:
      try:
        cantidad_venta = int(input("Ingrese la cantidad a vender: "))
        if cantidad_venta > 0:
          break
        print("La cantidad debe ser mayor a cero.")
      except ValueError:
        print("Error: Ingrese un número entero válido.")

    # Verificar que exista suficiente inventario
    if cantidad_venta > producto_encontrado["cantidad"]:
      print(f"Error: Stock insuficiente. Solo hay {producto_encontrado['cantidad']} unidades disponibles.")
      continue

    # Calcular subtotal del producto
    subtotal_producto = cantidad_venta * producto_encontrado["precio"]

    # Agregar al carrito de la venta actual
    carrito.append({
        "codigo": producto_encontrado["codigo"],
        "nombre": producto_encontrado["nombre"],
        "precio_unitario": producto_encontrado["precio"],
        "cantidad": cantidad_venta,
        "subtotal": subtotal_producto
    })

    print(f"-> Agregado al carrito: {cantidad_venta}x {producto_encontrado['nombre']} (Subtotal: Q{subtotal_producto:.2f})")

    continuar = input("¿Desea agregar otro producto a esta venta? (s/n): ").strip().lower()
    if continuar != 's':
      break

  if not carrito:
    print("\nLa venta fue cancelada o no se agregaron productos.")
    return

  # Calcular totales de la venta
  subtotal_general = sum(item["subtotal"] for item in carrito)
  iva = subtotal_general * 0.12
  total_venta = subtotal_general + iva

  # Generar número de venta único basado en la fecha y hora actual o contador
  ventas = cargar_datos(ARCHIVO_VENTAS)
  numero_venta = f"V-{len(ventas) + 1:04d}"

  # Mostrar resumen de la factura/venta
  print("\n" + "="*40)
  print(f"          FACTURA / TICKET DE VENTA")
  print(f"      No. Venta: {numero_venta}")
  print(f"      Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
  print("="*40)
  for item in carrito:
    print(f"- {item['cantidad']}x {item['nombre']} (@ Q{item['precio_unitario']:.2f}) = Q{item['subtotal']:.2f}")
  print("-" * 40)
  print(f"Subtotal General: Q{subtotal_general:.2f}")
  print(f"IVA (12%):        Q{iva:.2f}")
  print(f"TOTAL A PAGAR:    Q{total_venta:.2f}")
  print("="*40)

  confirmar = input("¿Desea confirmar y procesar esta venta? (s/n): ").strip().lower()
  if confirmar != 's':
    print("\nVenta cancelada por el usuario.")
    detener_venta = False
    return

  # Actualizar las existencias en el inventario de productos y registrar movimientos de salida
  for item in carrito:
    for p in productos:
      if p["codigo"] == item["codigo"]:
        p["cantidad"] -= item["cantidad"]
        # Registrar salida en el historial de inventario
        registrar_movimiento(
            codigo=p["codigo"],
            tipo="SALIDA/VENTA",
            cantidad=item["cantidad"],
            descripcion=f"Venta realizada - Factura {numero_venta}"
        )

  # Guardar los cambios actualizados de los productos
  guardar_datos(ARCHIVO_PRODUCTOS, productos)

  # Guardar el registro completo de la venta
  nueva_venta = {
      "numero_venta": numero_venta,
      "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
      "productos": carrito,
      "subtotal": subtotal_general,
      "iva": iva,
      "total": total_venta
  }

  ventas.append(nueva_venta)
  guardar_datos(ARCHIVO_VENTAS, ventas)

  print(f"\n¡Venta {numero_venta} registrada con éxito y existencias actualizadas!")


def consultar_historial_ventas():
  """Muestra un listado general de todas las ventas registradas en el sistema."""
  ventas = cargar_datos(ARCHIVO_VENTAS)
  if not ventas:
    print("\nNo hay registros de ventas en el sistema.")
    return

  print("\n--- HISTORIAL DE VENTAS REGISTRADAS ---")
  for v in ventas:
    print(f"\nFactura: {v['numero_venta']} | Fecha: {v['fecha']} | Total: Q{v['total']:.2f}")
    print("  Productos:")
    for item in v["productos"]:
      print(f"    - {item['cantidad']}x {item['nombre']} (Q{item['subtotal']:.2f})")