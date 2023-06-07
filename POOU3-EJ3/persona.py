class Persona:
    __nombre:str
    __direccion:str
    __dni:str
    def __init__(self,nombre,direccion,dni):
        self.__nombre=nombre
        self.__direccion=direccion
        self.__dni=dni

    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion
    def getDni(self):
        return self.__dni

    def __str__(self):
        return '%s %s %s'%(self.__nombre,self.__direccion,self.__dni)