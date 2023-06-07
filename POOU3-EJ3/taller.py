from inscripcion import Inscripcion
class Taller:
    __idTaller:int
    __nombre:str
    __vacantes:int
    __montoInscripcion:int
    def __init__(self,idTaller,nombre,vacantes,montoInscripcion):
        self.__idTaller=idTaller
        self.__nombre=nombre
        self.__vacantes=vacantes
        self.__montoInscripcion=montoInscripcion  

    def getVacantes(self):
        return self.__vacantes
    def getIdtaller(self):
        return self.__idTaller
    def getNombre(self):
        return self.__nombre
    def getMontoinscripcion(self):
        return self.__montoInscripcion

    
    def actualizarvacante(self):
        if self.__vacantes!=0:
            self.__vacantes-=1
        return self.__vacantes

        

    def __str__(self):
        return '{} {} {} {}'.format(self.__idTaller,self.__nombre,self.__vacantes,self.__montoInscripcion)