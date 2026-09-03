# p059-pares-descendente.py
# Programa que imprime los números pares y su suma total en un rango descendente desde 100 hasta un número n que elija el usuario.

while True:
    print("\033[2J\033[H", end="")
    print("Programa que imprime los números pares y su suma total en un rango descendente desde 100 hasta un número n que elija el usuario.\n")

    num = int(input("Introduce un número límite (menor a 100): "))
    print("Números pares: ", end="")

    sum = 0
    i = 100
    while i >= num:
        if i % 2 == 0:
            print(f"{i}, ", end="")
            sum += i
        i -= 1

    print(f"\nLa suma de los pares es: {sum}")
    if input("\nDeseas Continuar? (S/N)").upper() == "N" : break
