def es_vocal(caracter):
    return caracter in 'aeiouAEIOU'


cadena = 'Tengo treintaytres anios.'  # input("Ingrese una cadena: ")

cantidad_palabras_empiezan_terminan_igual = 0
cantidad_palabras_con_tr_y_vocal_primeras_3 = 0

# NO TE OLVIDES DE RESETEAR
contador = 0
primera_letra_de_palabra = None
caracter_anterior = ''
contiene_tr = False
incluye_vocal_en_primeras_tres = False

for caracter in cadena:
    if caracter in ' .':
        # Afuera de una palabra
        if primera_letra_de_palabra == caracter_anterior:
            cantidad_palabras_empiezan_terminan_igual += 1

        if contiene_tr and incluye_vocal_en_primeras_tres:
            cantidad_palabras_con_tr_y_vocal_primeras_3 += 1

        # RESET
        contador = 0
        primera_letra_de_palabra = None
        contiene_tr = False
        incluye_vocal_en_primeras_tres = False
    else:
        # Adentro de una palabra
        contador += 1

        if contador == 1:
            primera_letra_de_palabra = caracter

        if (caracter_anterior + caracter) == 'tr':
            contiene_tr = True

        if contador <= 3 and es_vocal(caracter):
            incluye_vocal_en_primeras_tres = True

    caracter_anterior = caracter

print(cantidad_palabras_empiezan_terminan_igual)
print(cantidad_palabras_con_tr_y_vocal_primeras_3)
