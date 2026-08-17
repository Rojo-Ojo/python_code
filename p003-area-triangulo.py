# p003-area-triangulo.py
# Calcular el área de un triángulo

print("\033[2J\033[H", end="")
print("Calculando el área de un triángulo.\n")

print("Dame la base y la altura del triángulo separados por <Enter>")
base, altura = int(input()), int(input())

area = ( base * altura ) / 2

print(f"El triángulo de base {base} y altura {altura}, tiene un área de {area}")
