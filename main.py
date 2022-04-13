from time import sleep
from classes.minas import *
from classes.cueva import *
from classes.camion import *

M = minas()

M.ingresar(cueva())
M.ingresar(cueva())
M.ingresar(cueva())
M.ingresar(cueva())

print("Se generaron las siguientes minas: ", M.getListaMinas())
# M.iniciarRuta(M.getRaiz())
# print(M.getBodega())
ruta = M.elegirRuta()
print("Ruta seleccionada:", ruta)
M.iniciarRuta(M.getRaiz(), ruta)
print(M.getBodega())