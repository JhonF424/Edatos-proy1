from classes.cueva import *


class minas:
    def __init__(self):
        self.raiz = None
        self.bodega = []
        self.cuenta = 0

    def getRaiz(self):
        return self.raiz

    def getBodega(self):
        return self.bodega

    def getCuenta(self):
        return self.cuenta

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
                return False

        if cueva.getId() > padre.getId():

            if self.crearCueva(padre.getDer(), cueva):
                padre.setDer(cueva)
                return False

        return False

    def eliminarCueva():
        pass  # <-- TO DO: Crear el método para eliminar una cueva, teniendo como condición
        #            que debe tener 10 de materiales para poder cerrarse

    def iniciarRuta(self, padre, buscar):
        if padre == None:
            return

        if padre.getId() == buscar:
            self.bodega.append(padre.getCant())  # <-- OJO, solo es de prueba

        self.extraerMaterial(padre.getIzq())
        self.extraerMaterial(padre.getDer())

    def comprobarBodega(self):
        #     la cantidad específica de cada material
        if self.cuenta % 2 == 0:
            self.crearCueva()

    def inOrder(self, padre):
        if padre == None:
            return

        self.inOrder(padre.getIzq())
        self.bodega.append(padre.getId())
        self.inOrder(padre.getDer())
