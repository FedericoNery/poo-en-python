class MiClase:
    """
    Este método solamente puede ser llamado si se tiene una instancia de la clase. 
    Una vez que se creó una instancia de la clase, se podrá accesar a los métodos de instancia. 
    Un método de instancia es capaz de crear, obtener y cambiar los atributos de instancia y a su vez de llamar otros métodos de instancia y clase
    """

    def metodo(self):
        return 'metodo de instancia', self


clase = MiClase()
clase.metodo()