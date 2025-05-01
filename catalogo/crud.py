# catalogo/crud.py

from catalogo.db import Session
from catalogo.models import Producto  # Importación directa de Producto

# Crear un producto
def crear_producto(nombre, descripcion, precio, stock):
    session = Session()
    producto = Producto(nombre=nombre, descripcion=descripcion, precio=precio, stock=stock)
    session.add(producto)
    session.commit()
    session.close()
    print(f"Producto '{nombre}' creado correctamente.")

# Listar todos los productos
def listar_productos():
    session = Session()
    productos = session.query(Producto).all()
    session.close()
    return productos

# Buscar producto por ID
def buscar_producto(id):
    session = Session()
    producto = session.query(Producto).filter_by(id=id).first()
    session.close()
    return producto

# Modificar producto
def modificar_producto(id, nuevo_nombre=None, nueva_descripcion=None, nuevo_precio=None, nuevo_stock=None):
    session = Session()
    producto = session.query(Producto).filter_by(id=id).first()
    if producto:
        if nuevo_nombre: producto.nombre = nuevo_nombre
        if nueva_descripcion: producto.descripcion = nueva_descripcion
        if nuevo_precio is not None: producto.precio = nuevo_precio
        if nuevo_stock is not None: producto.stock = nuevo_stock
        session.commit()
        print(f"Producto con ID {id} modificado correctamente.")
    else:
        print(f"No se encontró ningún producto con ID {id}.")
    session.close()

# Eliminar producto
def eliminar_producto(id):
    session = Session()
    producto = session.query(Producto).filter_by(id=id).first()
    if producto:
        session.delete(producto)
        session.commit()
        print(f"Producto con ID {id} eliminado correctamente.")
    else:
        print(f"No se encontró ningún producto con ID {id}.")
    session.close()
