
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from base_de_datos import BaseDeDatos

class Producto(BaseDeDatos.Base):
    __tablename__ = 'producto'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float)
    tipo_producto = Column(Integer, ForeignKey('tipo_producto.id'))
    def __init__(self, nombre, precio, tipo_producto):
        self.nombre = nombre
        self.precio = precio
        self.tipo_producto = tipo_producto
    def __repr__(self):
        return f'Producto({self.nombre}, {self.precio})'
    def __str__(self):
        return self.nombre