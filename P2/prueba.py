def es_digito(letra):
    return letra in '0123456789'


def es_vocal(letra):
    return letra in 'aeiouAEIOUáéíóúÁÉÍÓÚ'


def es_letra(letra):
    return 'a' <= letra <= 'z' or 'A' <= letra <= 'Z' or letra == 'ñ' or letra == 'Ñ'


def es_consonante(letra):
    return es_letra(letra) and not es_vocal(letra)


def calcular_promedio(cantidad, total):
    promedio = 0
    if total > 0:
        promedio = cantidad // total
    return promedio


def principal():
    archivo = open('entrada.txt', 'rt')
    texto = archivo.read()
    archivo.close()

    cant_letras_palabra = 0
    contiene_a = False
    cant_vocales_adentro_palabra = 0
    contiene_c = False
    empieza_con_vocal = False
    letra_anterior = None
    tercera_o_quinta_letra_digito = False

    cant_palabras_mas_6_letras = 0
    cant_palabras_con_a = 0
    cant_palabras_2_vocales_con_c = 0
    cant_palabras_empieza_vocal_termina_s_tercera_o_quinta_digito = 0

    for letra in texto:
        if letra != ' ' and letra != '.':
            # adentro de palabra
            cant_letras_palabra += 1

            if letra == "a" or letra == "A":
                contiene_a = True

            if es_vocal(letra):
                cant_vocales_adentro_palabra += 1

            if letra == "c" or letra == "C":
                contiene_c = True

            if cant_letras_palabra == 1 and es_vocal(letra):
                empieza_con_vocal = True

            if (cant_letras_palabra == 3 or cant_letras_palabra == 5) and es_digito(letra):
                tercera_o_quinta_letra_digito = True

            letra_anterior = letra
        else:
            # afuera de palabra
            if cant_letras_palabra > 6:
                cant_palabras_mas_6_letras += 1

            if cant_letras_palabra > 4 and contiene_a:
                cant_palabras_con_a += 1

            if cant_vocales_adentro_palabra >= 2 and contiene_c:
                cant_palabras_2_vocales_con_c += 1

            if empieza_con_vocal and letra_anterior.lower() == 's' and tercera_o_quinta_letra_digito:
                cant_palabras_empieza_vocal_termina_s_tercera_o_quinta_digito += 1

            cant_letras_palabra = 0
            contiene_a = False
            cant_vocales_adentro_palabra = 0
            contiene_c = False
            empieza_con_vocal = False
            tercera_o_quinta_letra_digito = False


if __name__ == '__main__':
    principal()