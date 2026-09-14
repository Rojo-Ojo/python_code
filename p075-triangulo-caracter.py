# p075-triangulo-caracter.py
# Dibuja un cuadro del caracter deseado.

print("\033[2J\033[H", end="")
print("Dibuja un cuadro del caracter deseado.\n")

r = int(input("De cuánto por cuanto r x r? "))
c = input("Caracter: ")

for i in range(1,r+1):
    for j in range(1,i+1):
        print(c, end="")
    print()
