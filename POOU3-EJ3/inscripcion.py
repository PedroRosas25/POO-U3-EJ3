class Inscripcion:
    __fecha='25/06/2023'
    __pago:bool
    __persona:object
    __taller:object
    def __init__(self,persona,taller):
        self.__pago=False
        self.__persona=persona
        self.__taller=taller

    def agregartaller(self,taller):
        self.__taller=taller

    def agregarpersona(self,persona):
        self.__persona=persona

    @classmethod
    def getFecha(cls):
        return cls.__fecha
    def getPago(self):
        return self.__pago
    def getTaller(self):
        return self.__taller
    def getPersona(self):
        return self.__persona    
    def getPersonaDni(self):
        return self.__persona.getDni()
    def getTallerId(self):
        return self.__taller.getIdtaller()


    def mostrartaller(self):
        print('Taller:{} Monto que debe:{} de la persona ingresada'.format(self.__taller.getNombre(),self.__taller.getMontoinscripcion()))

    def cambiarpago(self):
        self.__pago=True      

    def __str__(self) -> str:
        cadena='Fecha de inscripción: %s Pago: %s'%(self.__fecha,self.__pago)
        cadena+=str(self.__persona)
        cadena+=str(self.__taller)
        return cadena
