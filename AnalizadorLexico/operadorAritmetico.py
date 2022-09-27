from info import aritmetico


def opAritmetico(palabra):
    lista = list(palabra)
    operadores_aritmetico = []
    for caracter in lista:
        if caracter in aritmetico:
            operadores_aritmetico.append(caracter);
    for i in operadores_aritmetico:
        print(i, "Operador Aritmetico")


