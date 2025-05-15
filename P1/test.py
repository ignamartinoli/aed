import random

random.seed(47)
N = 13_000

# TODO: determine la cantidad de numeros que son menores al segundo numero que salio
primer_numero = None
segundo_numero = None
cantidad_numeros_menores_que_el_segundo = 0

for i in range(N):
    x = random.randint(1, 33_000)

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

print("Q 1:", cantidad_numeros_menores_que_el_segundo)