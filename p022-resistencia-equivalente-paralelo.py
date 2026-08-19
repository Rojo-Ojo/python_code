# p022-resistencia-equivalente-paralelo.py
# Programa que calcula la resistencia total o equivalente de un circuito con cuatro resistencias en paralelo.

print("\033[2J\033[H", end="")

print("Ingresa los valores de cuatro resistencias (ohm) separados por un espacio: ")
R1, R2, R3, R4 = map(float, input().split())

RT = 1 / ((1/R1) + (1/R2) + (1/R3) + (1/R4))

print(f"\nLa resistencia total de las resistencias en paralelo es: {RT:.2f} \u03A9\n")
