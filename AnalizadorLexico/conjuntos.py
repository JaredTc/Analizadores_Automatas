import re


def conjuntos(var):
    conjunto = re.findall("[0-9]+",var)
    for con in conjunto:
        if re.search("[0-9]+", con):
            print(con,"Numeros")
