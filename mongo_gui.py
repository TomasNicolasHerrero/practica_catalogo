# main.py
from catalogo.crud import (
    crear_producto,
    listar_productos,
    buscar_producto,
    modificar_producto,
    eliminar_producto,
)

def menu():
    while True:
        print("\n=== GESTOR DE CATÁLOGO ===")
        print("1. Crear producto")
        print("2. Listar productos")
        print("3. Buscar producto por ID")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            descripcion = input("Descripción: ")
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))
            crear_producto(nombre, descripcion, precio, stock)

        elif opcion == "2":
            productos = listar_productos()
            for p in productos:
                print(p)

        elif opcion == "3":
            id = int(input("ID del producto: "))
            producto = buscar_producto(id)
            if producto:
                print(producto)
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            id = int(input("ID del producto a modificar: "))
            nuevo_nombre = input("Nuevo nombre (deja en blanco para no cambiar): ")
            nueva_descripcion = input("Nueva descripción (deja en blanco para no cambiar): ")
            nuevo_precio_input = input("Nuevo precio (deja en blanco para no cambiar): ")
            nuevo_stock_input = input("Nuevo stock (deja en blanco para no cambiar): ")

            nuevo_precio = float(nuevo_precio_input) if nuevo_precio_input else None
            nuevo_stock = int(nuevo_stock_input) if nuevo_stock_input else None

            modificar_producto(
                id,
                nuevo_nombre or None,
                nueva_descripcion or None,
                nuevo_precio,
                nuevo_stock
            )

        elif opcion == "5":
            id = int(input("ID del producto a eliminar: "))
            eliminar_producto(id)

        elif opcion == "0":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()

