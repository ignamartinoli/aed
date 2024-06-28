"""
Determinar el promedio entero de letras por palabras de las
palabras que contiene al menos una vez el ultimo caracter
de la primera palabra del texto (sin incluirla).

Prueba: "la palabra fue aceptada por el programa en un tiempo record."
Resultado: 7
"""


def promedio(cantidad, total):
    resultado = 0
    if total > 0:
        resultado = cantidad // total
    return resultado


def principal():
    archivo = open('entrada.txt', 'rt')
    texto = archivo.read()
    archivo.close()

    cant_letras = 0
    ultima_letra_primera_palabra = None
    contiene_ultima_letra_primera_palabra = False

    letra_anterior = None
    cantidad_palabras_condicion = 0
    cantidad_letras_de_palabras_condicion = 0

    for letra in texto:
        if letra != " " and letra != ".":
            cant_letras += 1

            if letra == ultima_letra_primera_palabra:
                contiene_ultima_letra_primera_palabra = True

            letra_anterior = letra
        else:
            if ultima_letra_primera_palabra is None:
                ultima_letra_primera_palabra = letra_anterior

            if contiene_ultima_letra_primera_palabra:
                cantidad_palabras_condicion += 1
                cantidad_letras_de_palabras_condicion += cant_letras

            contiene_ultima_letra_primera_palabra = False
            cant_letras = 0

    resultado = promedio(cantidad_letras_de_palabras_condicion, cantidad_palabras_condicion)
    print(resultado)


if __name__ == '__main__':
    principal()
