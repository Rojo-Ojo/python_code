# p011-operadores-asignacion.py
# Ejemplificar el uso de operadores de asignación.

print("\033[2J\033[H", end="")
print("Operadores de asignación en Python. \n")

x = float(input("Valor de x: "))

x += 5
print(f"Sumar 5 a x: {x}")
x -= 3
print(f"Restar 3 a x: {x}")
x *= 2
print(f"Multiplicar x por 2: {x}")
x /= 4
print(f"Dividir x entre 4: {x}")
x %= 4
print(f"Modulo 4 de x: {x}")
x **= 2
print(f"X elevada al cuadrado: {x}")
x //= 4
print(f"Dividir x entre 4 entero: {x}")


