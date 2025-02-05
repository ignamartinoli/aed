cadena = 'Vivo en america.'  # input("Ingrese una cadena: ")

cantidad_palabras_empiezan_terminan_igual = 0

# NO TE OLVIDES DE RESETEAR
contador = 0
primera_letra_de_palabra = None
caracter_anterior = None

for caracter in cadena:
    if caracter == ' ' or caracter == '.':
        # Afuera de una palabra
        if primera_letra_de_palabra == caracter_anterior:
            cantidad_palabras_empiezan_terminan_igual += 1

        # RESET
        contador = 0
        primera_letra_de_palabra = None
    else:
        # Adentro de una palabra
        contador += 1

        if contador == 1:
            primera_letra_de_palabra = caracter

    caracter_anterior = caracter

print(cantidad_palabras_empiezan_terminan_igual)
