"""
	Una clase hereda(de forma predeterminada) los atributos y métodos de su superclase(o clase padre).
	La herencia es transitiva, es decir que una clase puede heredar de otra clase y al mismo tiempo heredar de otra,
	y así seguir hasta llegar a la clase base(Object).
	Las subclases pueden sobreescribir(“pisar”) los métodos y atributos para alterar su funcionamiento predeterminado.
"""

class Punto:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y

	def distancia(self, otro):
		dx = self.x - otro.x
		dy = self.y - otro.y
		return (dx*dx + dy*dy)**0.5

"""
	La función super() proporciona una referencia a la clase base
"""
class Punto3D(Punto):
	def __init__(self, x = 0, y = 0, z = 0):
		super().__init__(x, y)
		self.z = z

"""	def distancia(self, otro):
		dx = self.x - otro.x
		dy = self.y - otro.y
		dz = self.z - otro.z
		return (dx*dx + dy*dy + dz*dz)**0.5"""

if __name__ == "__main__":
	punto = Punto(5,5)
	punto3d = Punto3D(6,6)
	print(punto3d.distancia(punto))