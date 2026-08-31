# p051-adivina-numero.py
# Permite adivinar un número generado al azar entre 1 y 50.

import random

print("\033[2J\033[H", end="")
print("Permite adivinar un número generado al azar entre 1 y 50.\n")

print("He pensado un número entre 1 y 50, adivina cuál es: ")

ns = random.randint(1,50)
ci = 0

while True:
    intento = int(input("Cuál es: "))
    ci += 1
    if intento < ns :
        print("Demasiado bajo, intenta con un número más alto.")
    elif intento > ns :
        print("Demasiado alto, intenta con un número más bajo.")
    else:
        print(f"Felicidades, adivinaste el número en {ci} intentos.")
        print(f"El número era: {ns}")
        break

print("\nTerminamos Gracias.")
