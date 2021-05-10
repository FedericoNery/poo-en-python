

def factorialNormal(num):
    resultado = 1
    contador = num
    while contador > 0:
        resultado = contador * resultado
        contador = contador - 1
    return resultado

def factorialRecursivo(num):
    if(num == 0):
        return 1
    return num * factorialRecursivo(num -1)

if __name__ == '__main__':
    print(factorialNormal(5))
    print(factorialNormal(4))
    print(factorialNormal(3))
    print(factorialRecursivo(5))