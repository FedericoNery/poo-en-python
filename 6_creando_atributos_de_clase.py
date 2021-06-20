
class MethodTypes:
    name = "Ragnar"
    
    @classmethod
    def classMethod(cls):
        # Accede al atributo de clase a través de la palabra reservada cls
        cls.name = "Lagertha"
        print(cls.name)



if __name__ == '__main__':
    m = MethodTypes()
    MethodTypes.classMethod()
