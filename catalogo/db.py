# catalogo/db.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Ruta de la base de datos (ajustado para que esté en el directorio actual)
ruta_db = os.path.join(os.getcwd(), 'catalogo.db')  # Ajusta la ruta si lo necesitas
engine = create_engine(f"sqlite:///{ruta_db}", echo=True)

# Crear la sesión
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Evitar importación circular: Importamos Producto después de definir Base
from catalogo.models import Producto  # Importación aquí para evitar la circularidad

# Crear las tablas
Base.metadata.create_all(engine)
