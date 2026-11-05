from productos import consultar_producto, listar_productos, registrar_producto


from inventario import (
    consultar_existencias,
    registrar_entrada_inventario,
    verificar_stock_minimo,
    consultar_historial_movimientos,
)

from inventario import (
    consultar_existencias,
    registrar_entrada_inventario,
    verificar_stock_minimo,
    consultar_historial_movimientos,
)

from reportes import (
    reporte_listado_productos,
    reporte_stock_minimo,
    reporte_historial_ventas,
    reporte_total_ingresos,
    reporte_producto_mas_vendido,
    reporte_valor_inventario,
    reporte_promedio_ventas
)


def mostrar_menu():
  print("\n========================================")
  print("   SISTEMA DE GESTIÓN COMERCIAL")
  print("========================================")
  print("1. Módulo de Gestión de Productos")
  print("2. Módulo de Registro de Ventas")
  print("3. Módulo de Control de Inventarios")
  print("4. Módulo de Reportes y Estadísticas")
  print("5. Salir del sistema")
  print("========================================")

from ventas import registrar_venta, consultar_historial_ventas

def menu_ventas():
    while True:
        print("\n--- MÓDULO DE REGISTRO DE VENTAS ---")
        print("1. Registrar nueva venta")
        print("2. Consultar historial de ventas")
        print("3. Regresar al menú principal")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            consultar_historial_ventas()
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 3.")
            
def menu_reportes():
    while True:
        print("\n--- MÓDULO DE REPORTES Y ESTADÍSTICAS ---")
        print("1. Listado general de productos")
        print("2. Productos con stock mínimo o inferior")
        print("3. Historial de ventas")
        print("4. Total de ingresos por ventas")
        print("5. Producto con mayor cantidad de unidades vendidas")
        print("6. Valor total del inventario disponible")
        print("7. Promedio de ventas por período")
        print("8. Regresar al menú principal")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            reporte_listado_productos()
        elif opcion == "2":
            reporte_stock_minimo()
        elif opcion == "3":
            reporte_historial_ventas()
        elif opcion == "4":
            reporte_total_ingresos()
        elif opcion == "5":
            reporte_producto_mas_vendido()
        elif opcion == "6":
            reporte_valor_inventario()
        elif opcion == "7":
            reporte_promedio_ventas()
        elif opcion == "8":
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 8.")

def menu_productos():
  while True:
    print("\n--- GESTIÓN DE PRODUCTOS ---")
    print("1. Registrar producto")
    print("2. Consultar producto por código")
    print("3. Mostrar listado de productos")
    print("4. Regresar al menú principal")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
      registrar_producto()
    elif opcion == "2":
      consultar_producto()
    elif opcion == "3":
      listar_productos()
    elif opcion == "4":
      break
    else:
      print("Opción inválida. Por favor, ingrese un número del 1 al 4.")

def menu_inventario():
  while True:
    print("\n--- CONTROL DE INVENTARIOS ---")
    print("1. Consultar existencias de productos")
    print("2. Registrar entrada de inventario")
    print("3. Ver productos con stock mínimo o inferior")
    print("4. Consultar historial de movimientos")
    print("5. Regresar al menú principal")



    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
      consultar_existencias()
    elif opcion == "2":
      registrar_entrada_inventario()
    elif opcion == "3":
      verificar_stock_minimo()
    elif opcion == "4":
      consultar_historial_movimientos()
    elif opcion == "5":
      break
    else:
      print("Opción inválida. Por favor, ingrese un número del 1 al 5.")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
      registrar_producto()
    elif opcion == "2":
      consultar_producto()
    elif opcion == "3":
      listar_productos()
    elif opcion == "4":
      break
    else:
      print("Opción inválida. Por favor, ingrese un número del 1 al 4.")


def main():
  while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
      menu_productos()
    elif opcion == "2":
      menu_ventas()
      print(
          "\n[Módulo de Ventas en desarrollo...]"
      )  
      
    elif opcion == "3":
      menu_inventario()
      
      print(
          "\n[Módulo de Inventarios en desarrollo...]"
      )  
    elif opcion == "4":
      menu_reportes()
      print(
          "\n[Módulo de Reportes en desarrollo...]"
      )  
    elif opcion == "5":
      print("\nGracias por usar el sistema. ¡Hasta pronto!")
      break
    else:
      print(
          "Error: Opción no válida. Intente de nuevo ingresando una opción del"
          " 1 al 5."
      )

if __name__ == "__main__":
  main()
