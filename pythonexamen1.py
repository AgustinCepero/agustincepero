#!/usr/bin/python

import sys
import os

print "Introduzca su usuario"
usuario = raw_input()
print "Introduzca su clave"
clave = raw_input()
print "Introduzca la base de datos a la que quiera acceder"
basedatos = raw_input()
cadena = "mysql -u " + usuario + " -p" + clave + " " + basedatos
print cadena
os.system (cadena)
