# p020-numero-suerte.py
# Programa que solicita al usuario su año de nacimiento como un número entero de cuatro dígitos y calcula su número de la suerte.

print("\033[2J\033[H", end="")
print("Programa que solicita al usuario su año de nacimiento como un número entero de cuatro dígitos y calcula su número de la suerte.\n")

dNac = int(input("Ingresa tu año de nacimiento: "))

digito1, digito2, digito3, digito4 = map(int, str(dNac))
numSuerte = digito1 + digito2 + digito3 + digito4

print(f"\nDigitos individuales: {digito1}, {digito2}, {digito3}, {digito4}")
print(f"\nTu número de la suerte es: {numSuerte}\n")
