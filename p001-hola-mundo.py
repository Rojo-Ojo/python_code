# p001-hola-mundo.py
# Lee datos y envía un saludo

print("\033[2J\033[H", end="")
print("Leyendo datos y enviando un saludo.\n")

# Leer datos
nombre = input("Dame tu nombre: ")
edad = int(input("Dame tu edad: "))
peso = float(input("Dame tu peso: "))

print(f"\n{nombre} bienvenido a Python, tu edad es {edad}, tu peso es {peso}.")

print(nombre + " bienvenido a Python, tu edad es " + str(edad) + ", tu peso es " + str(peso) + ".")
