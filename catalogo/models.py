"""definición del modelo Producto"""


# catalogo/models.py

from sqlalchemy import Column, Integer, String, Float
from catalogo.db import Base

class Producto(Base):
    __tablename__ = 'productos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String)
    precio = Column(Float)
    stock = Column(Integer)

    def __repr__(self):
        return f"<Producto(id={self.id}, nombre='{self.nombre}', precio={self.precio}, stock={self.stock})>"
