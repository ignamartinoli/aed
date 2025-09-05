"""
Desarrolle un programa completo en Python que permita generar una sucesión de 5000
números enteros aleatorios, usando como semilla del generador el número 76.
Los valores de cada uno de esos 5000 número deben estar entre 1 y 65000
(incluidos ambos). A partir de esa sucesión el programa debe:
1 - Determinar la cantidad de números pares que sean múltiplos de 6
2 - Determinar la cantidad de números son mayores del primer número de la serie,
    no incluir dicho número
3 - Determinar la cantidad de números que perteneces al segundo millar de números
4 - Determinar el porcentaje que representan la cantidad de números del punto 2
    respecto del total de números procesados
5 - Determinar el promedio de los numeros del punto 2
"""

import random

random.seed(76)
N = 5_000

cantidad_pares_y_multiplos_6 = 0

primer_numero = None
cantidad_mayores_al_primero = 0

cantidad_en_segundo_millar = 0

porcentaje = 0

suma_numeros_pares_y_multiplos_6 = 0

for i in range(N):
    x = random.randint(1, 65_000)

    if (x % 2 == 0) and (x % 6 == 0):
        suma_numeros_pares_y_multiplos_6 += x
        cantidad_pares_y_multiplos_6 += 1

    if i == 0:
        primer_numero = x
    elif x > primer_numero:
        cantidad_mayores_al_primero += 1

    if 2_000 <= x <= 2_999:
        cantidad_en_segundo_millar += 1

if N != 0:
    porcentaje = (cantidad_mayores_al_primero * 100) // N

prom = 0
if cantidad_pares_y_multiplos_6 != 0:
    prom = suma_numeros_pares_y_multiplos_6 // cantidad_pares_y_multiplos_6