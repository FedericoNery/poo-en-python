from producto import Producto

def retornarProductoConIdentificador(session, identificador):
    #identificador
    ob = session.query(Producto).get(identificador)
    return ob

def retornarTodosLosProductos(session):
    productos = session.query(Producto).all()
    return productos

def retornarCantidadDeProductosEnBase(session):
    num_productos = session.query(Producto).count()
    return num_productos

def retornarProductoAplicandoFiltroDeBúsqueda(session):
    agua = session.query(Producto).filter_by(nombre='Agua').first()
    return agua

def retornarProductosDeValorMenorAUno(session):
    menos_de_1 = session.query(Producto).filter(Producto.precio < 1).all()
    return menos_de_1