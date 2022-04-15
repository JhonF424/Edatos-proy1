from time import sleep
from classes.minas import *
from classes.cueva import *
from classes.camion import *

M = minas()

M.ingresar(cueva())
M.ingresar(cueva())
M.ingresar(cueva())
M.ingresar(cueva())

while True:
    print("Listado de minas abiertas: ", M.getListaMinas())
    M.generarMaterial(M.getRaiz())
    M.comprobarBodega()

    sleep(5)  # <-- 30 Segundos

    ruta = M.elegirRuta()
    print("Ruta seleccionada:", ruta)
    M.iniciarRuta(M.getRaiz(), ruta)
    print()
    print()