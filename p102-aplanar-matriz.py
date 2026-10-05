# p102-aplanar-matriz.py
# Aplana una matriz de 2 dimensiones a una lista de 1 dimensión usando compresión de listas.

print("\033c", end="")
print("\033[1;34m" + "Aplanar matriz.\n" + "\033[0m")

matriz = [[1, 2, 3], [-4, 5, 6], [-7, 8, 9]]

# Se aplana la matriz usando compresión de listas.
aplanada = [elemento for fila in matriz for elemento in fila]
positivos = [elemento for fila in matriz for elemento in fila if elemento > 0]
negativos = [elemento for fila in matriz for elemento in fila if elemento < 0]

print("Matriz original:", matriz)
print("Matriz aplanada:", aplanada)
print("Elementos positivos:", positivos)
print("Elementos negativos:", negativos)