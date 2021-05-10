""""
        Pueden ser llamados sin tener una instancia de la clase
        No pueden acceder a ningún otro atributo o llamar a ninguna función dentro de la clase.
        Un método estático puede ser utilizado cuando se tiene una clase pero no necesariamente se tiene una instancia para poder acceder al método. 
        Por ejemplo si se tiene una clase Math y se tiene un método llamado factorial (calcula el factorial de un número dado). 
        Probablemente no se necesite tener una instancia específica para llamar al método, debido a esto se podría decidir hacer este método estático.
"""

class Math:
  @staticmethod
  def factorial(number):
        if number == 0:
            return 1
        else:
            return number * Math.factorial(number - 1)

if __name__ == '__main__':
    #imprime 120
    print(Math.factorial(5))