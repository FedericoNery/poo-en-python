
class MethodTypes:
    name = "Ragnar"
    
    @classmethod
    def classMethod(cls):
        # Access a class atribute through keyword cls
        cls.name = "Lagertha"
        print(cls.name)



if __name__ == '__main__':
    m = MethodTypes()
    MethodTypes.classMethod()
