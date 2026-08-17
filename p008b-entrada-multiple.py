# p008b-entrada-multiple.py
# Entrada múltiple de valores en una sola linea con map

print("\033[2J\033[H", end="")

# 1. Leer 10 números en la misma línea (separados por espacio)
print("Ingresa 10 números separados por espacios: \n")
v1, v2, v3, v4, v5, v6, v7, v8, v9, v10 = map(float, input().split())

# 2. Sumar la 10 variables
suma = v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8 + v9 + v10

# 3. Mostrar el resultado
print(f"\nLa suma de los 10 valores es: {suma}")