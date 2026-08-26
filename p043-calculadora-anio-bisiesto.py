# p043-calculadora-anio-bisiesto.py 
# Programa que determina si un año, ingresado por el usuario, es bisiesto. 
# Un año es bisiesto si cumple una de las siguientes condiciones:
#   1. Es divisible por 4, pero no es divisible por 100.
#   2. Es divisible por 400.
#   El programa debe indicar claramente si el año es bisiesto o no.

print("\033[2J\033[H", end="")
print("Programa que determina si un año, ingresado por el usuario, es bisiesto.\n")

anno = int(input("Año: "))

if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0) :
    print(f"El año {anno} es bisiesto.\n")
else:
    print(f"El año {anno} no es bisiesto.\n")
