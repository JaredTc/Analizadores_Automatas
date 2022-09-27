
#Llamar Funciones de las clases ()
import re

from conjuntos import conjuntos
from operadorAritmetico import opAritmetico
from palabraReservada import palabra_reservada
from relacional import relacional
from simbolos import simbolos

var  = input('----------Ingresa algo---------- \n');

palabras = var.split(" ");

for palabra in palabras:
    palabra_reservada(palabra);
    opAritmetico(palabra);
    simbolos(palabra);
    relacional(palabra);
    conjuntos(palabra)
    

