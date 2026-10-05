# p099-filtrar-pares.py
# Filtra los números pares de una lista de números introducidos usando compresión de listas.

print("\033c", end="")
print("\033[1;34m" + "Filtrar números pares." + "\033[0m")

cant = int(input("\nIngrese la cantidad de números a introducir: "))
numeros = []

# Se introducen los números en la lita
for i in range(cant):
    num = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(num)

# Se filtran los números pares e impares usando la compresión de listas.
pares = [x for x in numeros if x % 2 == 0]      # Par
impares = [x for x in numeros if x % 2 != 0]    # Impar

print("\nLos números introducidos son:", numeros)
print(f"Los numeros pares son: {pares} - Cantidad: {len(pares)}")
print(f"Los numeros impares son: {impares} - Cantidad: {len(impares) }")
