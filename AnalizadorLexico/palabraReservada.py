from info import palabrareservada


def palabra_reservada(palabra):
    if palabra in palabrareservada:
        print(palabra, "Es una palabra Reservada")
