def promedio(acumulador, cantidad):
    resultado = 0
    if cantidad > 0:
        resultado = acumulador // cantidad
    return resultado


def principal():
    archivo = open('entrada.txt', 'rt')
    texto = archivo.read()
    archivo.close()

    cant_letras_palabra = 0
    letra_anterior = None
    hay_ki = False

    cant_palabras = 0
    cant_letras_de_palabras_tienen_ki = 0
    cant_palabras_tienen_ki = 0

    for letra in texto:
        if letra != " " and letra != ".":
            cant_letras_palabra += 1

            if letra_anterior == "k" and letra == "i":
                hay_ki = True

            letra_anterior = letra
        else:
            cant_palabras += 1

            if hay_ki:
                cant_letras_de_palabras_tienen_ki += cant_letras_palabra
                cant_palabras_tienen_ki += 1

            cant_letras_palabra = 0
            hay_ki = False

    resultado = promedio(cant_letras_de_palabras_tienen_ki, cant_palabras_tienen_ki)
    print(resultado)


if __name__ == '__main__':
    principal()
