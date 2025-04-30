# mongo_test.py

from pymongo import MongoClient

# Conectar a MongoDB local
client = MongoClient("mongodb://localhost:27017/")

# Acceder a la base de datos "catalogo"
db = client["catalogo"]

# Acceder a la colección "productos"
productos = db["productos"]

# Crear un producto de ejemplo
producto = {
    "nombre": "Té verde",
    "descripcion": "Caja de 20 bolsitas",
    "precio": 3.5,
    "stock": 15
}

# Insertar el producto
resultado = productos.insert_one(producto)
print("Producto insertado con ID:", resultado.inserted_id)
