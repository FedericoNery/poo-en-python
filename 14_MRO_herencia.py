"""
La función super sigue un árbol de ancestros que se conoce como MRO (Method Resolution Order) -> Resolución de ordenes de métodos.
Busca siguiendo el orden (MRO) delegando en la primer clase superior por encima de la clase a la que pertenece hasta encontrar el método que estamos indicando.
Y siguiendo la secuencia de MRO comienza por buscar desde la clase donde se encuentra la invocación (función super) al método, sus padres, los padres de sus padres
y así hasta alcanzar la clase Object, en caso de no encontrarlo antes obviamente.
Podes ir borrando el método de las clases padres de abajo hacia arriba y comprobando cómo interpreta el orden.
Si pruebas cambiar el orden de las clases en
"""

class Shepadoodle (Caniche, Pastor_Aleman):#La clase hereda de las clases hijas de su padre Perros
    def ladrarx(self, veces):
        for cuantas in range(veces):
            super(Shepadoodle, self).ladrar()
#POR:
class Shepadoodle (Pastor_Aleman, Caniche):#La clase hereda de las clases hijas de su padre Perros
    def ladrarx(self, veces):
        for cuantas in range(veces):
            super(Shepadoodle, self).ladrar()


"""
Verás cómo prefiere el método de la clase Pastor_Aleman antes que la de Caniche.
Esto nos está diciendo que el orden de las clases, importa!
La función super nos va a permitir crear subclases que componen a otras determinando el comportamiento según el orden que le demos a las mismas.
"""

"""
También podes ver el MRO usando el atributo __mro__ llamando así Clase.__mro__
"""