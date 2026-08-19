# p019-calculo-tiempo.py
# Programa que toma una cantidad de horas como un número entero y muestra los dias, minutos y segundos equivalentes.

import math

print("\033[2J\033[H", end="")
print("Programa que toma una cantidad de horas como un número entero y muestra los dias, minutos y segundos equivalentes.\n")

horas = int(input("Ingresa las horas: "))

dias = horas / 24
minutos = horas * 60
segundos = minutos * 60

print(f"\n{horas} horas equivalen a {dias} dias, {minutos} minutos, {segundos} segundos.\n")
