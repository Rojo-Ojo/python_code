# p006-conversor-temperatura.py
# Convertir una temperatura dada en grados Celcius a grados Fahrenheit

print("\033[2J\033[H", end="")
print("Convertir una temperatura dada en grados Celcius a grados Fahrenheit,\n")

# f = ( float(input("Grados Celcius: ")) * 9/5) + 32

c = float(input("Grados Celcius: "))
f = (c * 9 / 5) + 32

print(f"La temperatura de {c} grados centigrados equivale a {f} grados fahrenheit.")