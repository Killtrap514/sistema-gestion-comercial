from archivos import cargar_datos

ARCHIVO_PRODUCTOS = "productos.json"
ARCHIVO_VENTAS = "ventas.json"


def reporte_listado_productos():
  """Genera un listado general tabular de todos los productos registrados."""
  productos = cargar_datos(ARCHIVO_PRODUCTOS)
  if not productos:
    print("\nNo hay productos registrados en el sistema.")
    return

  print("\n--- REPORTE: LISTADO GENERAL DE PRODUCTOS ---")
  print(f"{'Código':<10} | {'Nombre':<20} | {'Categoría':<15} | {'Precio':<10} | {'Stock':<8} | {'Stock Mín':<10}")
  print("-" * 85)
  for p in productos:
    print(
        f"{p['codigo']:<10} | {p['nombre']:<20} | {p['categoria']:<15} | Q{p['precio']:<9.2f} | {p['cantidad']:<8} | {p['stock_minimo']:<10}"
    )


def reporte_stock_minimo():
  """Identifica y reporta los productos con existencias iguales o inferiores al stock mínimo."""
  productos = cargar_datos(ARCHIVO_PRODUCTOS)
  if not productos:
    print("\nNo hay productos registrados.")
    return

  print("\n--- REPORTE: PRODUCTOS CON STOCK MÍNIMO O INFERIOR ---")
  encontrados = False
  for p in productos:
    if p["cantidad"] <= p["stock_minimo"]:
      encontrados = True
      print(
          f"¡ALERTA! Código: {p['codigo']} | Nombre: {p['nombre']} | Disponible: {p['cantidad']} | Stock Mínimo: {p['stock_minimo']}"
      )

  if not encontrados:
    print("Excelente: Ningún producto se encuentra por debajo de su stock mínimo.")


def reporte_historial_ventas():
  """Muestra el historial completo de ventas registradas."""
  ventas = cargar_datos(ARCHIVO_VENTAS)
  if not ventas:
    print("\nNo hay registros de ventas en el sistema.")
    return

  print("\n--- REPORTE: HISTORIAL DE VENTAS ---")
  for v in ventas:
    print(f"Factura: {v['numero_venta']} | Fecha: {v['fecha']} | Total: Q{v['total']:.2f}")


def reporte_total_ingresos():
  """Calcula y muestra el total de ingresos generados por las ventas acumuladas."""
  ventas = cargar_datos(ARCHIVO_VENTAS)
  if not ventas:
    print("\nNo hay ventas registradas para calcular los ingresos.")
    return

  total_ingresos = sum(v["total"] for v in ventas)
  print("\n--- REPORTE: TOTAL DE INGRESOS POR VENTAS ---")
  print(f"Ingresos Totales Acumulados: Q{total_ingresos:.2f} (Calculados a partir de {len(ventas)} ventas)")


def reporte_producto_mas_vendido():
  """Identifica el producto con mayor cantidad de unidades vendidas."""
  ventas = cargar_datos(ARCHIVO_VENTAS)
  if not ventas:
    print("\nNo hay suficientes datos de ventas registrados.")
    return

  conteo_productos = {}
  for v in ventas:
    for item in v["productos"]:
      codigo = item["codigo"]
      nombre = item["nombre"]
      cantidad = item["cantidad"]
      
      if codigo in conteo_productos:
        conteo_productos[codigo]["cantidad"] += cantidad
      else:
        conteo_productos[codigo] = {"nombre": nombre, "cantidad": cantidad}

  if not conteo_productos:
    print("\nNo se encontraron productos vendidos.")
    return

  # Encontrar el producto con el máximo valor en 'cantidad'
  producto_top = max(conteo_productos.values(), key=lambda x: x["cantidad"])

  print("\n--- REPORTE: PRODUCTO CON MAYOR CANTIDAD DE UNIDADES VENDIDAS ---")
  print(f"Producto: {producto_top['nombre']}")
  print(f"Unidades totales vendidas: {producto_top['cantidad']}")


def reporte_valor_inventario():
  """Calcula el valor monetario total del inventario disponible (precio * cantidad)."""
  productos = cargar_datos(ARCHIVO_PRODUCTOS)
  if not productos:
    print("\nNo hay productos registrados.")
    return

  valor_total = sum(p["precio"] * p["cantidad"] for p in productos)
  print("\n--- REPORTE: VALOR TOTAL DEL INVENTARIO DISPONIBLE ---")
  print(f"Valor Monetario Total en Inventario: Q{valor_total:.2f}")


def reporte_promedio_ventas():
  """Calcula el promedio de ingresos por venta registrada."""
  ventas = cargar_datos(ARCHIVO_VENTAS)
  if not ventas:
    print("\nNo hay ventas registradas para calcular promedios.")
    return

  total_ingresos = sum(v["total"] for v in ventas)
  promedio = total_ingresos / len(ventas)

  print("\n--- REPORTE: PROMEDIO DE VENTAS POR PERÍODO / TRANSACCIÓN ---")
  print(f"Total de transacciones: {len(ventas)}")
  print(f"Promedio de ingreso por venta: Q{promedio:.2f}")