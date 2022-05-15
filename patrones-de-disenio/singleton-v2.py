"""

Ejemplos de uso: Muchos desarrolladores consideran el patrón Singleton un antipatrón. Por este motivo, su uso está en declive en el código Python.

Identificación: El patrón Singleton se puede reconocer por un método de creación estático, que devuelve el mismo objeto guardado en caché.

Singleton ingenuo
Es muy fácil implementar un Singleton descuidado.
Tan solo necesitas esconder el constructor e implementar un método de creación estático.
La misma clase se comporta de forma incorrecta en un entorno multihilo.
Los múltiples hilos pueden llamar al método de creación de forma simultánea y obtener varias instancias de la clase Singleton.
"""

class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """

        # ...


if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")


# https://refactoring.guru/es/design-patterns/singleton/python/example#example-0