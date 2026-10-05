# p098-cuadrados-lista.py
# Genera cuadrados usando compresión de listas.

# Borrar la pantalla
print("\033c", end="")
print("\033[1;34m" + "Cuadrados de 1 a n usando compresión de listas." + "\033[0m")
n = int(input("\nIngrese el valor de n: "))

numeros = list(range(1, n+1))
cuadrados = [x ** 2 for x in numeros]   # Compresión de listas para calcular los cuadrados.

print("Los números del 1 al", n, "son:", numeros)
print("Los cuadrados del 1 al", n, "son:", cuadrados)
