# p021-distancia-entre-puntos.py
# Programa que calcula la distancia entre dos puntos en un plano cartesiano.

import math

print("\033[2J\033[H", end="")
print("Programa que calcula la distancia entre dos puntos en un plano cartesiano.\n")

x1, y1 = map(float, input("Ingresa las coordenadas del punto A con este formato \"x,y\": ").split(","))
x2, y2 = map(float, input("Ingresa las coordenadas del punto B con este formato \"x,y\": ").split(","))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"\nLa distancia entre esos puntos es: {distancia:.2f}\n")
