"""
La herencia múltiple consiste en heredar atributos y métodos de múltiples clases padres.
Es decir, heredamos de cada clase sus respectivos métodos y atributos, los cuales vamos a tener
disponibles para utilizar en nuestra clase creada
"""
class Telefono:
    def __init__(self, numero):
        self.numero = numero

    def llamar(self):
        print('llamando')

    def colgar(self):
        print('colgando')

class Camara:
    def __init__(self, mpx):
        self.mpx = mpx

    def fotografiar(self):
        print('tomando foto')

class ReproductorDeMusica:
    def __init__(self, capacidad):
        self.capacidad = capacidad

    def reproducirMusica(self):
        print('reproduciendo música')

class Celular(Telefono, Camara, ReproductorDeMusica):
    def __init__(self, numero, mpx, capacidad):
        Telefono.__init__(self, numero)
        Camara.__init__(self, mpx)
        ReproductorDeMusica.__init__(self, capacidad)

if __name__ == "__main__":
    celular = Celular("1512345678", 12, 8)
    celular.llamar()
    celular.colgar()
    celular.fotografiar()
    celular.reproducirMusica()


