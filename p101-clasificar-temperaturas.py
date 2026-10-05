# p101-clasificar-temperaturas.py
# Clasifica temperaturas en Fría, Templada y Caliente usando compresión de listas.

print("\033c", end="")
print("\033[1;34m" + "Clasificar temperaturas.\n" + "\033[0m")

temp = [15, 22, 30, 10, 25, 18, 35, 28]

clasificacion = [
    "Fría" if t < 20 else
    "Templada" if 20 <= t < 30 else
    "Caliente"
    for t in temp
]

print("Temperaturas: ", temp)
print("Clasificación: ", clasificacion)