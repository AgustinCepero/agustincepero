#!/usr/bin/python

import sys
import os

print "Introduzca su usuario"
usuario = raw_input()
print "Introduzca su clave"
clave = raw_input()
print "Introduzca la base de datos a la que quiera acceder"
basedatos = raw_input()
print "Nombre del archivo en el que quiere crear la copia de seguridad"
nombre=raw_input()
cadena = "mysql -u " + usuario + " -p" + clave + " " + basedatos + ' | gzip > ' + nombre +  '.sql.gz'
print cadena
os.system (cadena)
