# p109-lista-impares.py
# Programa que lee un entero n. Llena una lista con los primeros n números impares.
# Calcula e imprime:
# ● La suma y el promedio de los números.
# ● Los números que son divisibles entre 3 y su suma.
# ● Pedir un elemento a buscar en la lista original e indicar si está y en qué posición (índice).

print("\033c", end="") # Esto limpia la consola en sistemas compatibles

divisibles_3 = []

n = int(input("Introduzca la cantidad de números impares (n): "))

numeros = []

for i in range(n):
    numeros.append(2 * i + 1)

suma = sum(numeros)
promedio = suma / n

for numero in numeros:
    if numero % 3 == 0:
        divisibles_3.append(numero)

suma_divisibles_3 = sum(divisibles_3)

print("\n--- Generación de Lista ---")
print(f"Lista de los primeros 6 números impares: {numeros}")
print("\n--- Cálculos ---")
print(f"Suma de los números: {suma}")
print(f"Promedio de los números: {promedio}")
print("\n--- Divisibles entre 3 ---")
print(f"Números divisibles entre 3: {divisibles_3}")
print(f"Suma de los números divisibles entre 3: {suma_divisibles_3}")
print("\n--- Búsqueda ---")

buscar = int(input("Introduzca elemento a buscar: "))

if buscar in numeros:
    posicion = numeros.index(buscar)
    print(f"Result: El elemento {buscar} está en la lista en la posición (índice) {posicion}.")
else:
    print(f"El número {buscar} no está en la lista.")
