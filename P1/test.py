import random

random.seed(47)
N = 13_000

# TODO: determine la cantidad de numeros que son menores al segundo numero que salio
primer_numero = None
segundo_numero = None
cantidad_numeros_menores_que_el_segundo = 0

cantidad_negativos = 0

"""
Indicar el mayor entre todos los números comienzan con el dígito 1, es decir 1234 comienza
con 1 y 2345 no comienza con 1.
"""
mayor_que_comienza_con_1 = None

cantidad_negativos_pares = 0
cantidad_0 = 0
cantidad_positivos_impares = 0

# TODO: Determinar mayor que sea positivo e impar y su ultimo digito no sea 1
mayor_positivo_impar_sin_ultimo_digito_1 = None

for i in range(N):
    x = random.randint(-30_000, 30_000)

    if x <= 0:
        cantidad_negativos += 1

    if i == 0:
        # TODO: estoy en la primera vuelta
        primer_numero = x
    if i == 1:
        # TODO: estoy en la segunda vuelta
        segundo_numero = x
        if primer_numero < segundo_numero:
            cantidad_numeros_menores_que_el_segundo += 1
    if i >= 2:
        # TODO: estoy en las restantes vueltas
        if x < segundo_numero:
            cantidad_numeros_menores_que_el_segundo += 1

    if str(x)[0] == '1':
        if mayor_que_comienza_con_1 is None or x > mayor_que_comienza_con_1:
            mayor_que_comienza_con_1 = x

    if x < 0 and x % 2 == 0:
        cantidad_negativos_pares += 1
    if x == 0:
        cantidad_0 += 1
    if x > 0 and x % 2 != 0:
        cantidad_positivos_impares += 1

    if (x > 0) and (x % 2 != 0) and (x % 10 != 1):
        if mayor_positivo_impar_sin_ultimo_digito_1 is None:
            mayor_positivo_impar_sin_ultimo_digito_1 = x
        elif x > mayor_positivo_impar_sin_ultimo_digito_1:
            mayor_positivo_impar_sin_ultimo_digito_1 = x

    if x < 0:
        primer = str(x)[1]
    else:
        primer = str(x)[0]

    if x % 100 == 23:
        print()

print("Q 1:", cantidad_numeros_menores_que_el_segundo)