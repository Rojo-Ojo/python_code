# p058-impares-ascendente.py
# Programa que imprime los números impares y su suma total en un rango ascendente desde 1 hasta un número n que elija el usuario.

while True:
    print("\033[2J\033[H", end="")
    print("Programa que imprime los números impares y su suma total en un rango ascendente desde 1 hasta un número n que elija el usuario.\n")

    num = int(input("Introduce el número límite: "))
    print("Números impares: ", end="")

    sum = 0
    i = 1
    while i <= num:
        if i % 2 != 0:
            print(f"{i}, ", end="")
            sum += i
        i += 1

    print(f"\nLa suma de los impares es: {sum}")
    if input("\nDeseas Continuar? (S/N)").upper() == "N" : break
