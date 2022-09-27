from info import simbolo


def simbolos(palabra):
    lista = list(palabra)
    s_imbolo = []
    for caracter in lista:
        if caracter in simbolo:
            s_imbolo.append(caracter);
    for i in s_imbolo:
        print(i, "Es un simbolo")





