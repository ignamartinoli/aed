"""
Desarrolle un programa completo en Python que permita generar una sucesión de 10000 números
enteros aleatorios, usando como semilla del generador al valor 29 (es decir, random.seed(29)). Los valores de cada 
uno de esos 10000 números deben estar entre 1 y 25000 (incluidos ambos - DEBE usar random.randint(1, 
25000) para generar cada uno de estos números). A partir de esa sucesión, el programa debe: 
1. Determinar cuántos de esos números eran mayores o iguales a 1 pero menores que 10000, cuántos eran 
mayores o iguales que 10000 y menores que 20000, y cuántos eran mayores o iguales que 20000. 
2. Determinar cuántos de los números generados eran divisibles por 6. 
3. Determinar el menor entre todos los números generados. 
4. Determinar el promedio entero entre todos los números generados. Aclaración: NO se pide el promedio 
redondeado, sino el promedio truncado, sin decimales.
"""

import random

random.seed(29)

cantidad = 10_000

# Punto 1

mayor_o_igual_a_1_y_menor_a_10000 = 0
mayor_o_igual_a_10000_y_menor_a_20000 = 0
mayor_a_20000 = 0

# Punto 1.1

divisibles_por_5 = 0
divisibles_por_7 = 0
divisibles_por_10 = 0

# Punto 2

divisible_por_6 = 0

# Punto 3

menor = None

# Punto 3.1

menor_par = None

# Punto 3.2

primero = None
segundo = None
menores_al_segundo = 0

# Punto 4

suma = 0

# Punto 4.1

suma_impares = 0
cantidad_impares = 0

# Punto 4.2

cantidad_pares = 0

for i in range(cantidad):
    n = random.randint(1, 25_000)

    # Punto 1

    if 1 <= n < 10_000:
        mayor_o_igual_a_1_y_menor_a_10000 += 1
    elif 10_000 <= n < 20_000:
        mayor_o_igual_a_10000_y_menor_a_20000 += 1
    else:
        mayor_a_20000 += 1

    # Punto 1.1

    """
    Cuantos numeros divisibles por 5, cuantos por 7 y cuantos por 10
    """

    if n % 5 == 0:
        divisibles_por_5 += 1

    if n % 7 == 0:
        divisibles_por_7 += 1

    if n % 10 == 0:
        divisibles_por_10 += 1

    # Punto 2

    if n % 6 == 0:
        divisible_por_6 += 1

    # Punto 3

    if menor is None:
        menor = n
    elif n < menor:
        menor = n

    # Punto 3.1

    """
    Numero menor par
    """

    if n % 2 == 0:
        if menor_par is None:
            menor = n
        elif n < menor_par:
            menor_par = n

    # Punto 3.2

    """
    Numeros menores al segundo numero
    """

    if primero is None:
        primero = n  # 33
    elif segundo is None:
        segundo = n  # 33
        if primero < segundo:
            menores_al_segundo += 1
    elif n < segundo:
        menores_al_segundo += 1

    # Punto 4

    suma += n

    # Punto 4.1

    """
    Promedio de impares
    """

    if n % 2 == 1:
        suma_impares += n
        cantidad_impares += 1

    # Punto 4.2

    """
    Porcentaje de pares
    """

    if n % 2 == 0:
        cantidad_pares += 1

# Punto 4

promedio = 0
if cantidad != 0:
    promedio = suma // cantidad

print("Promedio:", promedio)

# Punto 4.1


promedio_impares = 0
if cantidad_impares != 0:
    promedio_impares = suma_impares // cantidad_impares

print("Promedio:", promedio_impares)

# Punto 4.2

porcentaje = (cantidad_pares * 100) / cantidad
print(porcentaje)
