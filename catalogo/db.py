"""conexion a la base de datos"""
# catalogo/db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///catalogo.db", echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
