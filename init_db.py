# init_db.py

from catalogo.db import Base, engine
from catalogo.models import Producto

# Crear las tablas en la base de datos si no existen
Base.metadata.create_all(engine)

print("Base de datos inicializada correctamente.")
