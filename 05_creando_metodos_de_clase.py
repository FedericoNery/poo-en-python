class MiClase:
    """
    Este método comparte una característica con el método estático, dicha característica es que este método puede ser llamado sin crear una instancia de la clase. 
    La diferencia recae en la capacidad de acceder otros métodos y atributos de la clase. 
    Sin embargo este tipo de métodos no tienen accesos a atributos de instancia ya que ninguna instancia fue creada para poder utilizarlos 
    """
    @classmethod
    def metodo_de_clase(cls):
        return 'metodo de clase', cls