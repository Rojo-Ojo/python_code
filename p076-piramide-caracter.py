# p076-piramide-caracter.py
# Imprime pirámide de caracteres.

print("\033[2J\033[H", end="")
print("Imprime pirámide de caracteres.\n")

altura = 31
c = "*"
espacios = caracteres = 0

for i in range(1,altura+1):
    espacios = altura - i
    caracteres = 2 * i - 1
    for e in range(espacios):
        print(" ", end="")
    for j in range(caracteres):
        print(c, end="")
    print()
