class Animal():

    def hablar(self):
        print("Habla el animal")

    @classmethod
    def escucharMascota(cls, animal):
        animal.hablar()

class Gato(Animal):
    def __init__(self):
        super().__init__()

    def hablar(self):
        print("MIAU")

    @classmethod
    def escucharMascota(cls):
        raise AttributeError("No se puede escuchar mascota desde la misma subclase")

class Perro(Animal):
    def __init__(self):
        super().__init__()

    def hablar(self):
        print("GUAU")

    @classmethod
    def escucharMascota(cls):
        raise AttributeError("No se puede escuchar mascota desde la misma subclase")


if __name__ == '__main__':
    g = Gato()
    p = Perro()
    # Polimorfismo -> consiste en llamar a un método o función del cual se pueden obtener distintos resultados según la clase del objeto que se le pasa por parámetro
    #Un ejemplo de polimorfismo es cuando usamos la estructura for(elemento in lista), en la lista o array podemos tener [1,"Hola", 1.5, True]
    #y la sentencia for va a recorrer ese array.
    #Otro ejemplo de polimorfismo es la función print -> ya que a distintos tipos de datos, arroja distintos resultados
    Animal.escucharMascota(g)
    Animal.escucharMascota(p)

    #Lanza excepción cuando se ejecuta el método desde la clase hija
    #Gato.escucharMascota()
    #Perro.escucharMascota()
