"""
Un decorador es una función Python que permite agregar funcionalidad a otra función, pero sin modificarla, mediante un wrapper (envoltorio).
También, esto es llamado meta-programación, por que parte del programa trata de modificar a otro al momento de compilar.
Para llamar un decorador se utiliza el signo de arroba (@).
"""
class Decorador:
    def __init__(self, funcion):
        print("__init__")
        funcion()

    def __call__(self):
        print("__call__")

def Funcion():
    print("Funcion()")

print("Inicio")
decorador = Decorador(Funcion)
Decorador()
print("Fin")


"""
Python proporciona soporte para envolver una función en un decorador mediante el símbolo @.
"""

class DecoradorB:
    def __init__(self, funcion):
        print("__init__")
        funcion()

    def __call__(self):
        print("__call__")

@DecoradorB
def Funcion():
    print("Funcion()")

print("Inicio")
Funcion()
print("Fin")

