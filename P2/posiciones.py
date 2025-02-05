cadena = 'Vivo en america.'  # input("Ingrese una cadena: ")

cantidad_palabras_empiezan_terminan_igual = 0

# NO TE OLVIDES DE RESETEAR
contador = 0
primera_letra_de_palabra = None

for caracter in cadena:
    if caracter == ' ' or caracter == '.':
        # Afuera de una palabra
        # RESET
        contador = 0
        primera_letra_de_palabra = None
    else:
        # Adentro de una palabra
        contador += 1

        if contador == 1:
            primera_letra_de_palabra = caracter

print()
