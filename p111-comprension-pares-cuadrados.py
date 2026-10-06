# p111-comprension-pares-cuadrados.py
# Programa que genera una lista de números enteros del 1 al n (donde n es ingresado por el usuario). Utilizando comprensión de
# listas, obtiene una nueva lista que contiene los cuadrados únicamente de los números pares. Imprime la lista con
# el rango completo, la lista resultante de cuadrados y la suma de dichos cuadrados.

print("\033c", end="") # Esto limpia la consola en sistemas compatibles

n = int(input("Introduzca el límite n: "))

lista_original = list(range(1, n + 1))

cuadrados_pares = [numero ** 2 for numero in lista_original if numero % 2 == 0]

suma_cuadrados = sum(cuadrados_pares)

print("\n--- Resultados ---")
print(f"Lista original (1 a {n}): {lista_original}")
print(f"Cuadrados de números pares: {cuadrados_pares}")
print(f"Suma de cuadrados: {suma_cuadrados}")