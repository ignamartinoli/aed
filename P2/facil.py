# Determinar cuántas palabras tienen la secuencia "in" en la segunda mitad de la palabra
#
# Determinar cuantas palabras incluyen dos o mas veces la expresion que conforma "d" mas una vocal,
# pero de tal forma que la palabra termina de una vocal
#
# Determinar la cantidad de palabras comienzan con un dígito impar,
# pero tales que el resto de sus caracteres son letras en minúsculas.
# Por ejemplo, en el texto: "La clave 1alfaxy puede funcionar en lugar de 1beta9 o en lugar de 9sigmaZ."
# hay solo una palabra que cumple: "1alfaxy"


def es_letra(caracter: str):
    return "A" <= caracter <= "z" or caracter.lower() == "n`"


def es_mayuscula(caracter: str):
    return "A" <= caracter <= "Z" or caracter == "N`"


def es_impar(caracter: str):
    return caracter in "13579"


def es_digito(caracter: str):
    return "0" <= caracter <= "9"


def es_consonante(caracter: str):
    return es_letra(caracter) and not es_vocal(caracter)


def es_vocal(caracter: str):
    return caracter.lower() in "aeiou"


def principal():
    # archivo = open("entrada.txt", "rt")
    texto = "La clave 1alfaxy puede funcionar en lugar de 1beta9 o en lugar de 9sigmaZ."  #  archivo.readline()
    # archivo.close()

    caracter_anterior = ""
    posicion_del_ultimo_in = 0

    cantidad_de_caracteres = 0
    contador_palabras = 0

    contador_d_mas_vocal = 0
    r2 = 0

    comienza_con_digito_impar = False
    hay_mayusculas = False
    hay_digito = False
    r3 = 0

    for caracter in texto:
        if caracter not in " .":
            cantidad_de_caracteres += 1

            # Punto 1
            if (caracter_anterior + caracter).lower() == "in":
                posicion_del_ultimo_in = cantidad_de_caracteres - 1

            # Punto 2
            if caracter_anterior.lower() == "d" and es_vocal(caracter):
                contador_d_mas_vocal += 1

            # punto 3
            if cantidad_de_caracteres == 1 and es_impar(caracter):
                comienza_con_digito_impar = True

            if cantidad_de_caracteres >= 2 and es_mayuscula(caracter):
                hay_mayusculas = True
            if cantidad_de_caracteres >= 2 and es_digito(caracter):
                hay_digito = True

            # punto 4
            if cantidad_de_caracteres in (1, 2) and es_vocal(caracter):
                pass
        else:
            # punto 1
            posicion_de_la_mitad = cantidad_de_caracteres // 2
            if posicion_de_la_mitad > posicion_del_ultimo_in:
                contador_palabras += 1

            # punto 2
            if contador_d_mas_vocal >= 2 and es_vocal(caracter_anterior):
                r2 += 1

            # punto 3
            if comienza_con_digito_impar and not hay_mayusculas and not hay_digito:
                r3 += 1

            cantidad_de_caracteres = 0
            posicion_del_ultimo_in = 0
            contador_d_mas_vocal = 0
            comienza_con_digito_impar = False
            hay_mayusculas = False
            hay_digito = False

        caracter_anterior = caracter

    print(contador_palabras)
    print(r2)


principal()
