import numpy as np
from inscripcion import Inscripcion
from manejaInscripciones import ManejadorInscripciones
from manejaPersonas import ManejadorPersona
from taller import Taller
import csv
class ManejadorTalleres:
    __listaTalleres:list
    __incremento:int
    __cantidad:int
    __dimension:3
    __mp=ManejadorPersona()
    __mi=ManejadorInscripciones()
    def __init__(self,dimension=3,incremento=1) -> None:
        self.__listaTalleres=np.empty(dimension,dtype=Taller)
        self.__cantidad=0
        self.__dimension=dimension
        self.__incremento=incremento
    def agregarTaller(self,taller):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__listaTalleres.resize(self.__dimension)
        self.__listaTalleres[self.__cantidad]=taller
        self.__cantidad+=1
        
    def cargartalleres(self):
        archivo=open('talleres.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            idtaller=int(fila[0])
            nombre=str(fila[1])
            vacantes=int(fila[2])
            monto=int(fila[3])
            untaller=Taller(idtaller,nombre,vacantes,monto)
            self.agregarTaller(untaller)


    def inscribirpersona(self):
        self.mostrar()
        idt=int(input('Ingrese id de taller al que se inscribe '))
        if self.__listaTalleres[idt-1].getVacantes()>0:
            self.__listaTalleres[idt-1].actualizarvacante()
            persona=self.__mp.cargarpersonas()
            inscripcion=Inscripcion(persona,self.__listaTalleres[idt-1])
            ManejadorInscripciones.agregarInscriptos(self.__mi,inscripcion)

    def consultarinscripcion(self):
        dnix=str(input('Ingrese DNI de la persona a buscar '))
        band=self.__mp.buscarpersona(dnix)
        if band==None:
            print('No se encontro la persona ingresada ')
        else:
            self.__mi.buscartaller(dnix)    

    def consultarinscriptos(self):
        idx=int(input('Ingrese id del taller a buscar '))
        self.__mi.buscarinscripcion(idx)        

    def registrarpago(self):
        dnix=str(input('Ingrese DNI del cliente a registrar pago '))
        band=self.__mp.buscarpersona(dnix)
        if band==None:
            print('Personas no existente ')
        else:
            self.__mi.registrarpago(dnix)      

    def guardarinscripciones(self):
        self.__mi.guardarinscripciones()       

    def mostrar(self):
        for i in range(len(self.__listaTalleres)):
            print('{}'.format(self.__listaTalleres[i]))
            