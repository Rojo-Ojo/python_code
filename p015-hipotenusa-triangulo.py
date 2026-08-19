# p015-hipotenusa-triangulo.py
# Programa que calcula la longitud de la hipotenusa de un triángulo rectángulo dados sus catetos.

import math

print("\033[2J\033[H", end="")
print("Programa que calcula la longitud de la hipotenusa de un triángulo rectángulo.\n")

cateto1 = float(input("Longitud en centímetros del primer cateto: "))
cateto2 = float(input("Longitud en centímetros del segundo cateto: "))

hipotenusa = math.sqrt( cateto1 * cateto1 + cateto2 * cateto2 )

print(f"\nPara un triángulo rectángulo cuyos catetos miden {cateto1:.2f}cm y {cateto2:.2f}cm,\nsu hipotenusa mide: {hipotenusa:.2f}cm")
