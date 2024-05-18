"""
Desarrolle un programa completo en Python que permita generar una sucesión de  13000 números 
enteros aleatorios, usando como semilla del generador al valor 47 (es decir, random.seed(47)). Los valores de cada 
uno de esos 13000 números deben estar entre 1 y 33000 (incluidos ambos - DEBE usar random.randint(1, 
33000) para generar cada uno de estos números). A partir de esa sucesión, el programa debe: 
1. Determinar cuántos eran mayores o iguales a 1 pero menores a 15000 y además eran divisibles por 4; 
cuántos eran mayores o iguales a 15000 pero menores que 22000 pero además eran pares, y cuántos eran 
mayores o iguales a 22000 pero además eran divisibles por 7. 
2. Determinar la suma de todos los números generados que estén entre 4000 y 11000 (incluídos ambos). 
3. Determinar el menor entre todos los números generados cuyos últimos dos dígitos sean iguales a 23 (es 
decir, aquellos cuyo resto al dividir por 100 es igual a 23). 
4. Determinar el porcentaje entero que la cantidad de números entre 4000 y 11000 (incluidos ambos) 
representa sobre la cantidad total de números. Observación: en el cálculo de este porcentaje, haga primero 
la multiplicación que corresponda, y luego la división.
"""

import random

random.seed(47)

cantidad = 13_000

# Punto 1

cantidad_primer_intervalo = 0
cantidad_segundo_intervalo = 0
cantidad_tercer_intervalo = 0

# Punto 2

suma_rango = 0

# Punto 3

menor = None

# Punto 3.1

menor_empieza_con_7 = None

# Punto 3.2

menor_anteultimo_8 = None

for i in range(cantidad):
    n = random.randint(1, 33_000)

    # Punto 1

    if n >= 1 and n < 15_000 and n % 4 == 0:
        cantidad_primer_intervalo += 1
    elif n >= 15_000 and n < 22_000 and n % 2 == 0:
        cantidad_segundo_intervalo += 1
    elif n >= 22_000 and n % 7 == 0:
        cantidad_tercer_intervalo += 1

    # Punto 2

    if 4_000 <= n <= 11_000:
        suma_rango += n

    # Punto 3

    if n % 100 == 23:
        if menor is None:
            menor = n
        elif n < menor:
            menor = n

    # Punto 3.1

    """
    Menor numero que empieza con 7
    """

    if str(n)[-1] == '7':
        if menor_empieza_con_7 is None:
            menor_empieza_con_7 = n
        elif n < menor_empieza_con_7:
            menor_empieza_con_7 = n

    # Punto 3.2

    """
    Anteultimo es 8
    """

    if len(str(n)) > 1:
        if str(n % 100)[0] == '8':
            if menor_anteultimo_8 is None:
                menor_anteultimo_8 = n
            elif n < menor_anteultimo_8:
                menor_anteultimo_8 = n
