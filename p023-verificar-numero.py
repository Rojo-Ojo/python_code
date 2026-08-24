# p023-verificar-numero.py
# Verificar si un número entero es positivo, negativo o cero.

print("\033[2J\033[H", end="")
print("Verificar si un número entero es positivo, negativo o cero.")

numero = int(input("\nDame un número: "))

if numero > 0 :
    print("El número es POSITIVO 👍")
if numero < 0 :
    print("El número es NEGATIVO 👎")
if numero == 0 :
    print("El número es CERO 🤷‍♂️")

print("\nAquí terminan las decisiones.")
