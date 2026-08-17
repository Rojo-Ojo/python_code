# p002-area-circulo.py
# Calcular el área de un círculo

import math #Importa la librería de constantes y funciones matemáticas

print("\033[2J\033[H", end="")
print ("Calculando el área de un círculo.\n")

radio = float(input("Dame el radio: "))

#area = math.pi * radio ** 2
area = math.pi * math.pow(radio, 2)

print(f"El círculo de radio {radio}, tiene un área de {area:.2f}")