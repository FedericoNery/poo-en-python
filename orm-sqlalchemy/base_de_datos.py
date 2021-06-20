from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class BaseDeDatos:
    __instance = None
    Base = declarative_base()
    Engine = create_engine('sqlite:///productos.sqlite')

    @staticmethod
    def getInstance():
        """ Método estático """
        if BaseDeDatos.__instance == None:
            BaseDeDatos()
        return BaseDeDatos.__instance

    @staticmethod
    def crear_base_de_datos():
        if BaseDeDatos.__instance == None:
            BaseDeDatos()
        BaseDeDatos.Base.metadata.create_all(BaseDeDatos.Engine)

    def __init__(self):
        """ Es público, debería ser privado ver de qué forma encapsular. Virtually private constructor. """
        if BaseDeDatos.__instance != None:
            raise Exception("Esta clase es un singleton!")
        else:
            SessionMaker = sessionmaker(bind=BaseDeDatos.Engine)
            session = SessionMaker()
            #self.session = session
            BaseDeDatos.__instance = session


if __name__ == '__main__':
    session = BaseDeDatos.getInstance()