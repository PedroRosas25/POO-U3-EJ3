from manejaTalleres import ManejadorTalleres as MT
from manejaPersonas import ManejadorPersona as MP
from manejaInscripciones import ManejadorInscripciones as MI
from menu import Menu

if __name__ == '__main__':
    mt=MT()
    mt.cargartalleres()
    menu=Menu()
    menu.opciones(mt)
    