# p016-tercer-angulo.py
# Programa que determina el tercer ángulo de un triángulo.

print("\033[2J\033[H", end="")
print("Programa que determina el tercer ángulo de un triángulo.\n")

angulo1 = float(input("Valor en grados del primer ángulo: "))
angulo2 = float(input("Valor en grados del segundo ángulo: "))

angulo3 = 180 - (angulo1 + angulo2)

print(f"El tercer ángulo del triángulo es: {angulo3:.2f}°")
