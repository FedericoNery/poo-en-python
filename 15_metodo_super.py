class Perro:
    def ladrar(self):
        print("GUAU GUAU")

    def grunir(self):
        print("GR GR")


class Caniche(Perro):
    def ladrar(self):
        print("guau guau")

    def grunir(self):
        print("gñi gñi")


class PastorAleman(Perro):
    def ladrar(self):
        print("GuaUUU GuaUUU")

    def grunir(self):
        print("Agrf agrf")


class Shepadoodle(Caniche, PastorAleman):
    def ladrarx(self, veces):
        for cuantas in range(veces):
            super(Shepadoodle, self).ladrar()


Tommy = PastorAleman()
Piny = Caniche()
Cuchele = Shepadoodle()
Cuchele.ladrarx(5)
Cuchele.ladrar()
Cuchele.grunir()
# Imprime guau guau guau (5 veces) porque heredo el ladrido de la clase padre CANICHE
# Pero si eliminamos o renombramos el método ladrar de CANICHE que imprimiria?
# Imprimiria el ladrido del Pastor_Aleman
# Y  si borramos ambos? Imprimirá el ladrido de Perros!

"""
    Vimos que los métodos de las clases padres pueden heredarse con la función super. 
    Ahora muy importante saber que para heredar los atributos de una clase tenemos que llamar a los constructores de las mismas
    especificandolas por su nombre(en herencia múltiple). Cuando heredemos de una sola clase, bastara con llamar al método super().__init__ que es 
    equivalente a ClasePadre.__init__
    Y si cambiamos el nombre u orden de la clase deberemos especificarlo!
"""