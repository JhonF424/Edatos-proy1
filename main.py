import functools
import random
from time import sleep
from classes.minas import *
from classes.cueva import *
from classes.camion import *

M = minas()

M.ingresar(cueva())
M.ingresar(cueva())
M.ingresar(cueva())


M.inOrder(M.getRaiz())
print(M.getBodega())
