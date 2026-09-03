# p064-verificar-palindromo.py
# Programa que solicita al usuario que ingrese un número entero y determina si es un palíndromo. 
# Un número es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda (ej. 121, 3443).

while True:
    print("\033[2J\033[H", end="")
    print("Programa que solicita al usuario que ingrese un número entero y determina si es un palíndromo."
          "\nUn número es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda (ej. 121, 3443).\n")

    num = int(input("Introduce un número para verificar si es palíndromo: "))
    original = num
    invertido = 0

    while num > 0:
        digito = num % 10
        invertido = invertido * 10 + digito
        num = num // 10

    if original == invertido:
        print(f"El número {original} es un palíndromo.")
    else:
        print(f"El número {original} no es un palíndromo.")
    
    if input("\nDeseas Continuar? (S/N)").upper() == "N" : break
