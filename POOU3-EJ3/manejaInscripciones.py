import numpy as np
import csv

class ManejadorInscripciones:
    #__listainscripciones:list
    #__incremento:int
    #__cantidad:int
    #__dimension:int
    __listainscripciones=[]

    def __init__(self):
        self.__listainscripciones=[]

    def agregarInscriptos(self,inscripto):
        self.__listainscripciones.append(inscripto)    

    def buscartaller(self,dnix):
        i=0
        while i<len(self.__listainscripciones) and self.__listainscripciones[i].getPersonaDni()!=dnix:
            i+=1
        if i ==len(self.__listainscripciones):
            return None
        else:
            self.__listainscripciones[i].mostrartaller()    

    def buscarinscripcion(self,idx):
        for i in range(len(self.__listainscripciones)):
            if self.__listainscripciones[i].getTallerId()==idx:
                print(self.__listainscripciones[i].getPersona())    

    def registrarpago(self,dnix):
        i=0
        while i<len(self.__listainscripciones) and self.__listainscripciones[i].getPersonaDni()!=dnix:
            i+=1
        if i==len(self.__listainscripciones):
            return None
        else:
            self.__listainscripciones[i].cambiarpago()
            print('Se registro el pago ')     

    def guardarinscripciones(self):
        archivo=open('inscripciones.csv','w')
        writer=csv.writer(archivo)
        for ins in self.__listainscripciones:
            dni=ins.getPersonaDni()
            idt=ins.getTallerId()
            fecha=ins.getFecha()
            pago=ins.getPago()
            nuevafila=[dni,idt,fecha,pago]
            writer.writerow(nuevafila)
        archivo.close()    

    #def __init__(self,dimension,incremento=1) -> None:
        #self.__listainscripciones=np.empty(dimension,dtype=Inscripcion)
        #self.__cantidad=0
        #self.__dimension=dimension
        #self.__incremento=incremento

    #def agregarInscripcion(self,inscripcion):
        #if self.__cantidad==self.__dimension:
         #self.__dimension+=self.__incremento
          #self.__listainscripciones.resize(self.__dimension)
        #self.__listainscripciones[self.__cantidad]=inscripcion
        #self.__cantidad+=1    

    
