import random

# from classes.minas import *


class cueva:
    def __init__(self):
        tipos = ["Madera", "Diamante", "Piedra", "Oro", "Plata", "Bronce"]
        tipoA = random.choice(tipos)
        self.tipo = (
            tipoA  # <-- Se genera un mina de cualquiera de los tipos de la lista
        )
        cant = random.randint(100, 300)  # <--
        self.cantidad = cant
        # Usamos la función random para generar datos aleatorios
        # Se deben crear dos variables, ya que la función retorna una tupla
        idI = random.randint(0, 999)  # <--
        self.id = idI
        self.izq = None
        self.der = None
        self.padre = None

    def getIzq(self):
        return self.izq

    def getDer(self):
        return self.der

    def setIzq(self, izq):
        self.izq = izq

    def setDer(self, der):
        self.der = der

    def getTipo(self):
        return self.tipo

    def getCant(self):
        return self.cantidad

    def setCant(self, nCant):
        self.cantidad = nCant

    def getId(self):
        return self.id

    def esNodoHoja(self):
        return not (self.izq or self.der)

    def esNodoRaiz(self):
        return not self.padre

    def esIzq(self):
        if self.padre:
            return self.getIzq() == self.padre.getIzq()

    def esDer(self):
        if self.padre:
            return self.getDer() == self.padre.getDer()

    def getPadre(self):
        return self.padre

    def setPadre(self, Padre):
        self.padre = Padre
