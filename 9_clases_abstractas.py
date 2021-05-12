from abc import ABC, abstractmethod


"""
Si la clase no hereda de ABC o contiene por lo menos un método abstracto, Python permitirá instancias las clases.
"""

"""
Las subclases tienen que implementar todos los métodos abstractos, en el caso de que falta alguno de ellos Python no permitirá instancias tampoco la clase hija.
"""
class Animal(ABC):

    #def __init__(self, nombre):
    def __init__(self):
        self.nombre = "Nombre"
#        self.nombre = nombre

    @abstractmethod
    def mover(self):
       print("animal")

class Gato(Animal):

    def __init__(self):
        super(Gato, self).__init__()


    #def __init__(self, nombre):
     #   super(Gato, self).__init__(nombre)

    def mover(self):
        super(Gato, self).mover()


#g = Gato("Javier")
g = Gato()
print(g.nombre)
g.mover()
