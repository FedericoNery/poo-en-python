"""
A diferencia de las variables, si nosotros comparamos dos instancias de objetos, con sus respectivos atributos de igual valor
que el otro objeto, el resultado nos va a dar False.
¿Por qué? Porque los objetos instanciados son únicos, como cuando nace una persona, cada uno tiene una única huella dactilar.
Cada objeto es único y se guarda en una posición de memoria distinta.
Entonces...¿Cómo puedo verificar, si alguna vez lo requiero, que dos objetos sean iguales verificando solo los atributos?

Para eso, vamos a definir nuestro método __eq__ (sobreescritura de métodos) para poder comparar los objetos solamente por sus atributos
"""

"""
Para probar lo mencionado anteriormente pueden descomentar y comentar el método __eq__
"""

class Futbolista():
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    #def __eq__(self, other):
    #    return self.nombre == other.nombre and self.apellido == other.apellido and self.edad == other.edad

if __name__ == '__main__':
    cadenaA = "Hola"
    cadenaB = "Hola"

    print(cadenaA == cadenaB)

    numA = 1
    numB = 1

    print(numA == numB)

    futbolista1 = Futbolista("Lionel", "Messi", 34)
    futbolista2 = Futbolista("Lionel", "Messi", 34)

    print(futbolista1)
    print(futbolista2)
    print(futbolista1 == futbolista2)