# p042-precio-entrada-cine.py
# Programa para la taquilla de un cine que determina el precio de una entrada según la edad del cliente.

print("\033[2J\033[H", end="")
print("Programa para la taquilla de un cine que determina el precio de una entrada según la edad del cliente.\n")

edad = int(input("Edad del cliente: "))

if edad >= 0 and edad < 5 :
    print("¡La entrada es gratuita!\n")
elif edad >= 5 and edad <= 12 :
    print("El precio de la entrada es $5.\n")
elif edad >= 13 and edad <= 64 :
    print("El precio de la entrada es $10.\n")
elif edad >= 65 and edad <= 150:
    print("El precio de la entrada es $7.\n")
else:
    print("En este cine no se permite el ingreso de fantasmas.\n")
