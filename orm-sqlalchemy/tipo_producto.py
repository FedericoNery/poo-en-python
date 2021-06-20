from sqlalchemy import Column, Integer, String
from base_de_datos import BaseDeDatos

class TipoProducto(BaseDeDatos.Base):
    __tablename__ = 'tipo_producto'
    id = Column(Integer, primary_key=True)
    nombre_tipo = Column(String, nullable=False)
    def __init__(self, nombre_tipo):
        self.nombre_tipo = nombre_tipo

    def __repr__(self):
        return f'TipoProducto({self.nombre_tipo})'
    def __str__(self):
        return self.nombre_tipo