def principal():
    # archivo = open("entrada.txt", "rt")
    texto = "tarde o temprano tantos tipos pierden."  #  archivo.readline()
    # archivo.close()

    caracter_anterior = ""

    contador_de_palabras = 0

    cantidad_de_letras = 0
    empieza_con_ta = False
    hay_una_m = False

    longitud_de_mayor_palabra = None
    posicion_palabra_mayor = None

    for caracter in texto:
        if caracter not in " .":
            cantidad_de_letras += 1

            if (
                cantidad_de_letras == 2
                and (caracter_anterior + caracter).lower() == "ta"
            ):
                empieza_con_ta = True

            if caracter.lower() == "m":
                hay_una_m = True
        else:
            contador_de_palabras += 1

            if empieza_con_ta and not hay_una_m:
                if posicion_palabra_mayor is None:
                    longitud_de_mayor_palabra = cantidad_de_letras
                    posicion_palabra_mayor = contador_de_palabras
                elif longitud_de_mayor_palabra < cantidad_de_letras:
                    longitud_de_mayor_palabra = cantidad_de_letras
                    posicion_palabra_mayor = contador_de_palabras

            cantidad_de_letras = 0
            empieza_con_ta = False
            hay_una_m = False

        caracter_anterior = caracter

    print(posicion_palabra_mayor)


principal()
