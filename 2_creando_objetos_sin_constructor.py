"""-------------
A partir de haber leido la primer parte, nos pueden surgir dudas como por ejemplo
¿Qué pasa si nosotros no necesitamos atributos en nuestras clases y simplemente lo que queremos usar son métodos de instancia?
En esta parte lo que vamos a verificar es que TODAS las CLASES que creemos, van a heredar de la clase:
- Object

Entonces, que es object -> es la clase base dentro de la jerarquía de clases. Si nosotros creamos muchas clases,
absolutamente TODAS van a heredar los métodos de Object.

EJEMPLO:
    a. Si creo la clase FiguraGeometrica, y FiguraGeometrica tiene clases hijas como Cuadrado, Rectangulo, Circulo, etc.
    b. Cuadrado, Rectangulo y Circulo son hijos de FiguraGeometrica.
    c. FiguraGeometrica es hijo de object.
    d. Por ende, Cuadrado, Rectangulo, Circulo heredan los métodos de object a través de la clase FiguraGeometrica

Cuando creamos una clase, estamos creando un tipo nuevo de Object, permitiendo crear nuevas instancias de nuestra propia clase
Cada instancia de clase puede tener atributos vinculados para mantener su estado y métodos que pueden modificar dicho estado

Resumiendo: cuando nosotros no definamos nuestro constructor, simplemente estaremos utilizando el constructor de object, el cual
ejecutará su fragmento de código definido en su implementación y no creará o generará ningún atributo específico para nuestra clase
-----------------"""
class ClassicSpam:
    pass

class NewSpam(object):
    pass

class Spam():
    pass

"""
La siguiente línea de código verifica que object se encuentre como clase base de las clases ClassicSpam, NewSpam, Spam
Cada forma de escribir estas clases hacia referencia a las viejas formas en las que se escribían las clases en Python 2.x
En Python 2.x si no se aclaraba que una clase heredaba de Object, estas clases no heredarían los métodos de Object
No vamos a dedicarle tiempo a esto, adjunto el link del cual pueden leer que es lo que sucede
Link: https://stackoverflow.com/questions/4015417/why-do-python-classes-inherit-object
Es importante entender que si el código de clases que escribimos en Python 3.x, 
no lo escribimos para que sea compatible con Python 2.x, podemos tener un comportamiento inesperado y no va a funcionar correctamente el 
programa desarrollado
"""

print([object in cls.__bases__ for cls in {Spam, NewSpam, ClassicSpam}])
