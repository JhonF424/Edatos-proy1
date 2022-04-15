import json
import random
from time import sleep
from classes.cueva import *


class minas:
    def __init__(self):
        self.raiz = None
        self.bodega = {
            "cMadera": 0,
            "cDiamante": 0,
            "cPiedra": 0,
            "cOro": 0,
            "cPlata": 0,
            "cBronce": 0,
        }
        self.listaMinas = []

    def getRaiz(self):
        return self.raiz

    def getBodega(self):
        return json.dumps(self.bodega, sort_keys=False, indent=4)

    def getListaMinas(self):
        return self.listaMinas

    def ingresar(self, cueva):

        self.listarCuevas(cueva)

        if cueva.getId() not in self.listaMinas:
            pass
        if self.raiz == None:
            self.raiz = cueva
        else:
            self.crearCueva(self.raiz, cueva)

    def crearCueva(self, padre, cueva):

        if not padre:
            return True

        if cueva.getId() < padre.getId():
            if self.crearCueva(padre.getIzq(), cueva):
                padre.setIzq(cueva)
                return False

        if cueva.getId() > padre.getId():

            if self.crearCueva(padre.getDer(), cueva):
                padre.setDer(cueva)
                return False

        return False

    def eliminarCueva(self, padre):
        pass  # <-- TO DO: Crear el método para eliminar una cueva, teniendo como condición
        #            que debe tener 10 de materiales para poder cerrarse

    def listarCuevas(self, padre):
        if not padre:
            return
        if padre.getId() not in self.listaMinas:
            self.listaMinas.append(padre.getId())

        self.listarCuevas(padre.getIzq())
        self.listarCuevas(padre.getDer())

    def elegirRuta(self):
        return random.choice(self.listaMinas)

    def iniciarRuta(self, padre, ruta):
        if padre == None:
            return

        if padre.getId() == ruta:
            print(
                "La mina",
                ruta,
                "tiene un total de: ",
                padre.getCant(),
                "unidades de",
                padre.getTipo(),
            )

            if padre.getTipo() == "Madera":
                if padre.getCant == 0:
                    self.listaMinas.remove(padre.getId())
                    self.eliminarCueva(padre.getId())

                ext = self.extraerMineral(padre.getCant())
                print("se extraen: ", ext)
                act = padre.getCant()
                self.bodega["cMadera"] += ext
                nC = act - ext
                padre.setCant(nC)

            elif padre.getTipo() == "Diamante":
                if padre.getCant == 0:
                    self.listaMinas.remove(padre.getId())
                    self.eliminarCueva(padre.getId())

                ext = self.extraerMineral(padre.getCant())
                print("se extraen: ", ext)
                act = padre.getCant()
                self.bodega["cDiamante"] += ext
                nC = act - ext
                padre.setCant(nC)

            elif padre.getTipo() == "Piedra":
                if padre.getCant == 0:
                    self.listaMinas.remove(padre.getId())
                    self.eliminarCueva(padre.getId())

                ext = self.extraerMineral(padre.getCant())
                print("se extraen: ", ext)
                act = padre.getCant()
                self.bodega["cPiedra"] += ext
                nC = act - ext
                padre.setCant(nC)

            elif padre.getTipo() == "Oro":
                if padre.getCant == 0:
                    self.listaMinas.remove(padre.getId())
                    self.eliminarCueva(padre.getId())

                ext = self.extraerMineral(padre.getCant())
                print("se extraen: ", ext)
                act = padre.getCant()
                self.bodega["cOro"] += ext
                nC = act - ext
                padre.setCant(nC)

            elif padre.getTipo() == "Plata":
                if padre.getCant == 0:
                    self.listaMinas.remove(padre.getId())
                    self.eliminarCueva(padre.getId())

                ext = self.extraerMineral(padre.getCant())
                print("se extraen: ", ext)
                act = padre.getCant()
                self.bodega["cPlata"] += ext
                nC = act - ext
                padre.setCant(nC)

            elif padre.getTipo() == "Bronce":
                if padre.getCant == 0:
                    self.listaMinas.remove(padre.getId())
                    self.eliminarCueva(padre.getId())

                ext = self.extraerMineral(padre.getCant())
                print("se extraen: ", ext)
                act = padre.getCant()
                self.bodega["cBronce"] += ext
                nC = act - ext
                padre.setCant(nC)

            print("Bodega abastecida, estado actual: \n\n", self.getBodega())

        self.iniciarRuta(padre.getIzq(), ruta)
        self.iniciarRuta(padre.getDer(), ruta)

    def comprobarBodega(self):
        if self.bodega["cMadera"] >= 100:
            self.ingresar(cueva())
        elif self.bodega["cDiamante"] >= 100:
            self.ingresar(cueva())
        elif self.bodega["cPiedra"] >= 100:
            self.ingresar(cueva())
        elif self.bodega["cOro"] >= 100:
            self.ingresar(cueva())
        elif self.bodega["cPlata"] >= 100:
            self.ingresar(cueva())
        elif self.bodega["cBronce"] >= 100:
            self.ingresar(cueva())

    def extraerMineral(self, cant):
        return 20 * cant / 100

    def generarMaterial(self, padre):
        if padre == None:
            return

        act = padre.getCant() + 2
        padre.setCant(act)
        self.generarMaterial(padre.getIzq())
        self.generarMaterial(padre.getDer())
