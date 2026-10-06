# p107-listas-aleatorios-suma.py
# Programa que genera 2 listas de 10 números aleatorios cada una. Crea una tercera lista donde el elemento es la suma de
# los correspondientes de las listas A y B, solo si AMBOS elementos son impares; de lo contrario, el elemento de
# la tercera lista será 0. Imprime las 3 listas.

import random

print("\033c", end="") # Esto limpia la consola en sistemas compatibles

lista_a = [random.randint(1, 100) for i in range(10)]
lista_b = [random.randint(1, 100) for i in range(10)]
lista_c = []

lista_c = [lista_a[i] + lista_b[i] if lista_a[i] % 2 != 0 and lista_b[i] % 2 != 0 else 0 for i in range(10)]

print("--- Listas Generadas ---")
print("Lista A:", lista_a)
print("Lista B:", lista_b)
print("\n--- Resultados (Suma solo si A[i] y B[i] son ambos impares) ---")
print("Lista C:", lista_c)
