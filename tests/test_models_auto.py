# test_models_auto.py

from sqlalchemy.orm import Session
from catalogo.db import engine
from catalogo.models_auto import Productos

# Crear una sesión usando el mismo motor
session = Session(bind=engine)

# Consultar todos los productos
productos = session.query(Productos).all()

# Mostrar resultados
print("\n=== Productos leídos desde models_auto.py ===")
for p in productos:
    print(f"{p.id} | {p.nombre} | {p.precio} € | stock: {p.stock}")

session.close()
