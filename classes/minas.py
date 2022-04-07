import cueva


class minas:
    def __init__(self):
        self.raiz = None
        self.bodega = []

    def getRaiz(self):
        return self.raiz

    def getBodega(self):
        return self.bodega

    def crearCueva():
        pass  # <-- TO DO: Crear el método para crear una nueva cueva, teniendo como condición
        # <--        que deben existir 100 materiales del mismo tipo

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
        print(self.getBodega())  # <-- Con este método vamos a revisar si la bodega tiene
        #     la cantidad específica de cada material

    