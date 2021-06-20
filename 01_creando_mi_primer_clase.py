"""
CLASE: es un modelo, template, del cual pueden instanciarse o crearse objetos
OBJETO: es la instancia creada a partir del modelo o Clase. Es el conjunto de datos (atributos) y comportamientos (métodos)
que intentan modelar aspectos relevantes de entidades útiles para un sistema.
"""

#¿Cómo se escribe una clase?
class MiClase:
  """
    __init__() -> es el MÉTODO constructor de una clase, el primer fragmento de código que se ejecuta cuando se instancia un objeto de una clase.
    Todas las clases que uno cree, va a tener este método ya que hereda de OBJECT.
    Su propósito principal es para inicializar los valores del objeto instanciado, es decir su propio estado. También puede ser usado para realizar
    alguna operación, cálculo o llamada a método o función que el desarrollador quiera utilizar
  """
  def __init__(self, atributo_a, atributo_b):
    # ¿Cómo se define e inicializa un atributo?
    self.atributo_a = atributo_a
    self.atributo_b = atributo_b

  """
    self -> es un parámetro de referencia a la instancia actual de la clase, y es usado para acceder a los atributos del objeto instanciado de la clase.
    Se lo puede llamar de cualquier forma (ponerle otro nombre) pero SIEMPRE TIENE QUE SER EL PRIMER PARÁMETRO
  """

objeto1 = MiClase("Hola", 10)

#Imprime Hola
print(objeto1.atributo_a)
#Imprime 10
print(objeto1.atributo_b)


