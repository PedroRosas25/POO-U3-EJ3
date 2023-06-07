from persona import Persona
import csv

class ManejadorPersona:
    __listapersonas=[]

    def __init__(self):
        self.__listapersonas=[]

    def cargarpersonas(self):
        nombre=str(input('Ingrese nombre de la persona '))
        direccion=str(input('Ingrese direccion de la persona '))
        dni=str(input('Ingrese DNI de la persona '))
        unapersona=Persona(nombre,direccion,dni)
        self.__listapersonas.append(unapersona)
        return unapersona

    def buscarpersona(self,dnix):
        i=0
        while i<len(self.__listapersonas) and self.__listapersonas[i].getDni()!=dnix:
            i+=1
        if i ==len(self.__listapersonas):
            i=None
        return i              

