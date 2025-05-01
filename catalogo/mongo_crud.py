# catalogo/mongo_crud.py
from pymongo import MongoClient

# Conexión a MongoDB local
client = MongoClient("mongodb://localhost:27017/")
db = client["catalogo"]
coleccion = db["productos"]

# Crear un producto
def crear_producto_mongo(nombre, descripcion, precio, stock):
    producto = {
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio,
        "stock": stock
    }
    resultado = coleccion.insert_one(producto)
    print("Producto insertado con ID:", resultado.inserted_id)

# Listar todos los productos
def listar_productos_mongo():
    productos = coleccion.find()
    for p in productos:
        print(f"{p['_id']} | {p['nombre']} | {p['precio']}€ | stock: {p['stock']}")

# Buscar producto por nombre
def buscar_producto_mongo(nombre):
    resultado = coleccion.find_one({"nombre": nombre})
    if resultado:
        print("Producto encontrado:")
        print(resultado)
    else:
        print("Producto no encontrado.")

# Modificar producto
def modificar_producto_mongo(nombre, nuevos_datos):
    resultado = coleccion.update_one(
        {"nombre": nombre},
        {"$set": nuevos_datos}
    )
    if resultado.modified_count:
        print("Producto modificado correctamente.")
    else:
        print("No se modificó ningún producto.")

# Eliminar producto
def eliminar_producto_mongo(nombre):
    resultado = coleccion.delete_one({"nombre": nombre})
    if resultado.deleted_count:
        print("Producto eliminado correctamente.")
    else:
        print("No se encontró ningún producto con ese nombre.")
