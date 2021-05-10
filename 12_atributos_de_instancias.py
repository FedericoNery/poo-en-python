class User:

    def __init__(self, username, password):
        self.username = username
        self._password = password
        """
            Por convencion se usa el guion bajo
            Aunque indicamos que _password es un atributo privado, si ejecutamos el programa deberíamos visualizar la contraseña en consola.
        """
        self.__password = password

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    def get_password(self):
        return self.__password


"""
    Siempre que deseemos evitar que un usuario modifique el estado interno de la instancia, lo cual podría comprometer al objeto, 
    será necesario el uso de variable y métodos privados. 

    User posee el atributo password, como es un dato sensible, lo mejor que podemos hacer es asegurarnos que el atributo 
    no pueda ser modificado ni accedido fuera de la clase.
    Por ello es un excelente candidato a ser un atributo privado.
"""

"""
    Ahora bien... ¿Qué sucede en Python? Python no posee atributos privados, todos los atributos que definamos son públicos, sin embargo,
    los desarrolladores que utilizan este lenguaje, encontraron la forma de replicar esto en Python. 
    Si bien no es lo mismo, nos va a ayudar a desarrollar de forma robusta nuestra API de la clase. 
"""

"""
    Utilizando un doble guión bajo al principio del nombre de un atributo o método, 
    el intérprete de Python RENOMBRA al elemento para evitar colisiones con las subclases (atributos o métodos que poseen el mismo nombre
    en una clase padre y su clase hija que hereda)
    Aunque la idea original era esa, muchos desarrolladores utilizan el doble guión bajo (__) para prevenir accesos no autorizados.
"""

if __name__ == '__main__':
    cody = User('Cody', 'password123')
    #imprime password123
    print(cody._password)

    #Imprime todos los métodos y atributos del objeto cody, en este comando se visualizan los métodos heredados de la super clase object y se visualiza
    #la property _User__password -> llamando o imprimiendo este atributo, nos va a aparecer en pantalla el valor de la password 
    print(dir(cody))
    print(cody.get_password())
    cody._User__password = "vulnere la password GG"
    print(cody.get_password())
    #Si descomentamos la línea de abajo, Python nos arrojará un error por consola
    #print(cody.__password)