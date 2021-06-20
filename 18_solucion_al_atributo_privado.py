class User:

    def __init__(self, username, password):
        self.username = username
        self._password = password #por convencion
        self.__password = password

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    def get_password(self):
        return self.__password
"""
aunque indicamos que _password es un atributo privado, si ejecutamos el programa deberíamos visualizar la contraseña en consola.
"""

"""
Siempre que deseemos evitar que un usuario modifique el estado interno de la instancia, lo cual podría comprometer al objeto, 
será necesario el uso de variables y métodos privados. 

User posee el atributo password, y el password al ser un dato sensible,
lo mejor que podemos hacer es asegurarnos que el atributo no pueda ser modificado ni accedido fuera de la clase; 
por ello es un excelente candidato a ser un atributo privado.
"""

if __name__ == '__main__':
    cody = User('Cody', 'password123')
    print(cody._password)
    print(dir(cody))
    print(cody.get_password())
    cody._User__password = "vulnere la password"
    print(cody.get_password())
    #print(cody.__password)