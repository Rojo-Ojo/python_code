# p018-area-volumen-cilindro.py
# Programa que calcula el área y volumen de un cilindro.

import math

print("\033[2J\033[H", end="")
print("Programa que calcula el área y volumen de un cilindro.\n")

radio = float(input("Ingresa el radio (R) en centímetros: "))
print(f"\033[FIngresa el radio (R) en centímetros: {radio}cm")
altura = float(input("Ingresa la altura (h) en centímetros: "))
print(f"\033[FIngresa la altura (h) en centímetros: {altura}cm")

area = 2 * math.pi * radio * (radio + altura)
volumen = math.pi * radio**2 * altura

print(f"\nEl cilindro tiene un área de {area:.2f}cm\u00b2 y un volumen de {volumen:.2f}cm\u00b3")
