class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self.__pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self.__pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Introduzca la contraseña: ")
            if password == "sw0rdf1sh":
                self.__pineapple_allowed = value
            else:
                raise ValueError("Alerta! Intruso!")


pizza = Pizza(["chesse", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)