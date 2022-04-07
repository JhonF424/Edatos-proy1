class cueva():
    def __init__(self, tipo, cantidad, id):
       self.tipo = tipo,
       self.cantidad = cantidad,
       self.id = id
       
       
    def getTipo(self):
        return self.tipo
    
    def setTipo(self, tipo):
        self.tipo = tipo
        
    def getCant(self):
        return self.cantidad
    
    def setCant(self, cant):
        self.cantidad = cant
        
    def getId(self):  # <-- Necesitamos un ID por cada cueva, para poder asignar un camión
                      #     que se dirija a buscar esa cueva, siendo una ruta específica
        return self.id
    
    def setId(self, id):
        self.id = id
        
        
    def generarMineral(self):
        # Pendiente: Establecer el tiempo
        # cada 10 segundos...
        
        self.cantidad += 2
        
         