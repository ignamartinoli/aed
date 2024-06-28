def porcentaje(parte, total):
    return (parte * 100) // total


def promedio(parte, total):
    resultado = 0
    if total > 0:
        resultado = parte // total
    return resultado


def es_vocal(letra):
    return letra in "aeiou"


def es_letra(letra):
    return 'a' <= letra <= 'z' or 'A' <= letra <= 'Z' or letra == 'ñ' or letra == 'Ñ'


def es_consonante(letra):
    return es_letra(letra) and not es_vocal(letra)


def principal():
    archivo = open('entrada.txt', 'rt')
    texto = archivo.read()
    archivo.close()

    cant_letras_palabra = 0
    contiene_letra_v = False
    contiene_vocal = False
    cant_vocales_palabra = 0
    cant_consonantes_palabra = 0

    cant_palabras = 0
    cant_palabras_con_v_y_vocal = 0
    cant_letras_mas_vocales_que_consonantes = 0
    cant_palabras_mas_vocales_que_consonantes = 0

    for letra in texto:
        if letra != " " and letra != ".":
            cant_letras_palabra += 1

            if letra == "v":
                contiene_letra_v = True

            if es_vocal(letra):
                contiene_vocal = True

            if es_vocal(letra):
                cant_vocales_palabra += 1

            if es_consonante(letra):
                cant_consonantes_palabra += 1
        else:
            cant_palabras += 1

            if contiene_letra_v and contiene_vocal:
                cant_palabras_con_v_y_vocal += 1

            if cant_vocales_palabra > cant_consonantes_palabra:
                cant_letras_mas_vocales_que_consonantes += cant_letras_palabra
                cant_palabras_mas_vocales_que_consonantes += 1

            cant_letras_palabra = 0
            contiene_letra_v = False
            contiene_vocal = False
            cant_vocales_palabra = 0
            cant_consonantes_palabra = 0

    punto_c = porcentaje(cant_palabras_con_v_y_vocal, cant_palabras)
    print(punto_c, "%")
    punto_a = promedio(cant_letras_mas_vocales_que_consonantes, cant_palabras_mas_vocales_que_consonantes)
    print("Promedio:", punto_a)

if __name__ == '__main__':
    principal()