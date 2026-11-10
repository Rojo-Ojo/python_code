# p158-aleatorios.py
# Funcion que genera lista de numeros aleatorios
# Luego genero 2 listas aleatorias usando esa funcion
# Luego obtengo la suma de ambas con otra funcion

print("\033c", end="")  # Limpia la consola (secuencia ANSI, en terminales compatibles)

import random

def generaAleatorios(n: int, min: int, max: int) -> list[int]:
    """Genera una lista de n numeros aleatorios entre min y max."""
    lista = []
    for _ in range(n):
        numero = random. randint(min, max)
        lista.append( numero )
    return lista

def generaAleatorios(n: int, min: int, max: int) -> list[int]:
    lista = []
    for _ in range(n):
        numero = random.randint(min, max)
        lista.append( numero )
    return lista

def sumarListas(lista1: list[int], lista2: list[int]) -> list[int]:
    """Suma los elementos de dos listas y regresa una nueva lista con los resultados."""
    if len(lista1) != len(lista2):
        return 0
    suma = []
    for i in range(len(lista1)):
        suma.append(lista1[i] + lista2[i])
    return suma

# Programa principal.
MAX = 10
lista1 = generaAleatorios(MAX, 1, 10)
lista2 = generaAleatorios(MAX, 50, 100)
lista3 = sumarListas(lista1, lista2)

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")

if lista3 == 0:
    print("Las listas no tienen la misma longitud, no se puede sumar.")
else:
    print(f"Suma de listas: {lista3}")
