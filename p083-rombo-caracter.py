# p083-rombo-caracter.py
# Programa que solicita al usuario un número entero impar n que representará la altura y el ancho máximo de un rombo. 
# El programa dibuja el rombo utilizando el carácter que el usuario elija.

print("\033[2J\033[H", end="")
print("Programa que solicita al usuario un número entero impar n que representará la altura y el ancho máximo de un rombo.\n" 
      "El programa dibuja el rombo utilizando el carácter que el usuario elija.\n")

altura = int(input("Dame un número impar para la altura: "))
c = input("¿Qué carácter quieres usar? ")

espacios = caracteres = 0

for i in range(1,altura-1):
    espacios = altura - i
    caracteres = 2 * i - 1
    for e in range(espacios):
        print(" ", end="")
    for j in range(caracteres):
        print(c, end="")
    print()

for i in range(altura-3,0,-1):
    espacios = altura - i
    caracteres = 2 * i - 1
    for e in range(espacios):
        print(" ", end="")
    for j in range(caracteres):
        print(c, end="")
    print()
