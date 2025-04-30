# mongo_main.py

from catalogo.mongo_crud import (
    crear_producto_mongo,
    listar_productos_mongo,
    buscar_producto_mongo,
    modificar_producto_mongo,
    eliminar_producto_mongo
)
import subprocess
import os

def menu_mongo():
    while True:
        print("\n=== GESTOR DE CATÁLOGO (MongoDB) ===")
        print("1. Crear producto")
        print("2. Listar productos")
        print("3. Buscar producto por nombre")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Visualizar productos en ventana (tkinter)")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            descripcion = input("Descripción: ")
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))
            crear_producto_mongo(nombre, descripcion, precio, stock)

        elif opcion == "2":
            listar_productos_mongo()

        elif opcion == "3":
            nombre = input("Nombre del producto: ")
            buscar_producto_mongo(nombre)

        elif opcion == "4":
            nombre = input("Nombre del producto a modificar: ")
            print("Introduce nuevos valores (deja en blanco para no cambiar):")
            nueva_descripcion = input("Nueva descripción: ")
            nuevo_precio = input("Nuevo precio: ")
            nuevo_stock = input("Nuevo stock: ")

            nuevos_datos = {}
            if nueva_descripcion:
                nuevos_datos["descripcion"] = nueva_descripcion
            if nuevo_precio:
                nuevos_datos["precio"] = float(nuevo_precio)
            if nuevo_stock:
                nuevos_datos["stock"] = int(nuevo_stock)

            modificar_producto_mongo(nombre, nuevos_datos)

        elif opcion == "5":
            nombre = input("Nombre del producto a eliminar: ")
            eliminar_producto_mongo(nombre)

        elif opcion == "6":
            ruta = os.path.join(os.getcwd(), "mongo_gui.py")
            subprocess.run(["python", ruta])

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Inténtalo.")

if __name__ == "__main__":
    menu_mongo()
