class Calculadora():
    def sumar(self, numA, numB):
        return numA + numB
    def restar(self, numA, numB):
        return numA - numB
    def dividir(self, numA, numB):
        return numA // numB
    def multiplicar(self, numA, numB):
        return numA * numB

class CalculadoraNotacionPolaca(Calculadora):

    def resolverCuenta(self, cuenta):
        return 0


class CalculadoraBinaria(Calculadora):

    def convertirADecimal(self, numeroBinario):
        return 0

    def convertirABinario(self, numeroDecimal):
        return 0

    def sumar(self, numA, numB):
        operandoA = self.convertirADecimal(numA)
        operandoB = self.convertirADecimal(numB)
        resultadoEnDecimal = operandoA + operandoB

        return numA + numB
    def restar(self, numA, numB):
        return numA - numB
    def dividir(self, numA, numB):
        return numA // numB
    def multiplicar(self, numA, numB):
        return numA * numB



