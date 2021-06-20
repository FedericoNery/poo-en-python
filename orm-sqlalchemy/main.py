from consultas import retornarProductoConIdentificador, retornarCantidadDeProductosEnBase,retornarProductosDeValorMenorAUno,retornarTodosLosProductos,retornarProductoAplicandoFiltroDeBúsqueda
from base_de_datos import BaseDeDatos
from producto import Producto
from tipo_producto import TipoProducto

def ejecutarConsultas():
    session = BaseDeDatos.getInstance()
    print(retornarProductoConIdentificador(session, 1))
    print(retornarTodosLosProductos(session))
    print(retornarCantidadDeProductosEnBase(session))
    print(retornarProductoAplicandoFiltroDeBúsqueda(session))

    print(retornarProductosDeValorMenorAUno(session))

def crearBaseDeDatos():
    BaseDeDatos.crear_base_de_datos()

def seedearTipoProducto():
    session = BaseDeDatos.getInstance()
    almacen = TipoProducto("Almacen")
    session.add(almacen)
    print(almacen.id)
    bebida = TipoProducto("Bebida")
    session.add(bebida)
    print(bebida.id)
    session.commit()



def seedearProductos():
    session = BaseDeDatos.getInstance()
    arroz = Producto('Arroz', 1.25, 1)
    session.add(arroz)
    print(arroz.id)
    agua = Producto('Agua', 0.3, 2)
    session.add(agua)
    session.commit()
    print(agua.id)

if __name__ == '__main__':
    crearBaseDeDatos()
    seedearTipoProducto()
    seedearProductos()
    ejecutarConsultas()