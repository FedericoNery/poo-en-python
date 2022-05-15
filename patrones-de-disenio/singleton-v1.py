"""
Este patrón la creación de un solo objeto o una instancia a una clase en particular.
Tipo de patrón creacional
Provee un punto de acceso global a la instancia creada
"""
class Singleton:
   __instance = None
   @staticmethod
   def getInstance():
      """ Método estático """
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance
   def __init__(self):
      """ Debería ser un constructor privado esto (cumpliría "esa función"). """
      if Singleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Singleton.__instance = self
s = Singleton()
print(s)

s = Singleton.getInstance()
print(s)

s = Singleton.getInstance()
print(s)

"""
Cuando ejecutemos este código, la dirección de memoria del objeto va a ser la misma.
De esa forma corroboramos que este código funciona correctamente
"""
# https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm