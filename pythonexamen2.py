#!/usr/bin/python

import os
import sys

print "Introduzca su usuario"
usuario=raw_input()

print "Introduzca su clave"
clave=raw_input()

print "Introduzca la base de datos a la que se quiera conectar"
basedatos=raw_input()

os.system("mysql -u" + usuario + " -p" + clave + " " + basedatos)


