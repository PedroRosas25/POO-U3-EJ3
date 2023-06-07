class Menu:
    __opcion=0

    def __init__(self):
        self.__opcion=0

    def opciones(self,mt):
        while self.__opcion!=6:
            print("||---Menu de Opciones---||")
            print("1) Inscribir una persona en un taller")
            print("2) Consultar inscripcion ")
            print("3) Consultar inscriptos a un taller")
            print("4) Registrar pago ")
            print("5) Guardar inscripciones ")
            print("6) Salir")
            self.__opcion=int(input('Ingrese opcion '))
            if self.__opcion==1:
                mt.inscribirpersona()
            elif self.__opcion==2:
                mt.consultarinscripcion()
            elif self.__opcion==3:
                mt.consultarinscriptos()
            elif self.__opcion==4:
                mt.registrarpago()
            elif self.__opcion==5:
                mt.guardarinscripciones()    
            elif self.__opcion==6:
                print('FIN')
            else:
                print('Opcion no valida ')       