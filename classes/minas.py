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
        return self.bodega.items()

    def getListaMinas(self):
        return self.listaMinas

    def ingresar(self, cueva):
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
                self.listaMinas.append(padre.getId())
                return False

        if cueva.getId() > padre.getId():

            if self.crearCueva(padre.getDer(), cueva):
                padre.setDer(cueva)
                self.listaMinas.append(padre.getId())
                return False

        return False

    def eliminarCueva():
        pass  # <-- TO DO: Crear el método para eliminar una cueva, teniendo como condición
        #            que debe tener 10 de materiales para poder cerrarse

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
                self.bodega["cMadera"] += padre.getCant()
            elif padre.getTipo() == "Diamante":
                self.bodega["cDiamante"] += padre.getCant()
            elif padre.getTipo() == "Piedra":
                self.bodega["cPiedra"] += padre.getCant()
            elif padre.getTipo() == "Oro":
                self.bodega["cOro"] += padre.getCant()
            elif padre.getTipo() == "Plata":
                self.bodega["cPlata"] += padre.getCant()
            elif padre.getTipo() == "Bronce":
                self.bodega["cBronce"] += padre.getCant()
            print("Cargando camión...", padre.getCant())

        self.iniciarRuta(padre.getIzq(), ruta)
        self.iniciarRuta(padre.getDer(), ruta)

    def comprobarBodega(self):
        if self.bodega["cMadera"] >= 100:
            self.ingresar(cueva())  # <-- Pendiente de probar
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

    def inOrder(self, padre):
        if padre == None:
            return

        self.inOrder(padre.getIzq())
        self.bodega.append(padre.getId())
        print(padre.getId())
        self.inOrder(padre.getDer())

    def preOrder(self, padre):
        if padre == None:
            return

        self.bodega.append(padre.getId())
        self.preOrder(padre.getIzq())
        self.preOrder(padre.getDer())

    def posOrder(self, padre):
        if padre == None:
            return

        self.posOrder(padre.getIzq())
        self.posOrder(padre.getDer())
        self.bodega.append(padre.getId())
