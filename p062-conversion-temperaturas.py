# p062-conversion-temperaturas.py
# Programa que permite al usuario introducir una temperatura inicial y una final en grados Celsius. 
# El programa muestra la conversión a grados Fahrenheit para cada grado en ese rango, incrementando de uno en uno.

while True:
    print("\033[2J\033[H", end="")
    print("Programa que permite al usuario introducir una temperatura inicial y una final en grados Celsius."
          "\nEl programa muestra la conversión a grados Fahrenheit para cada grado en ese rango, incrementando de uno en uno.\n")

    temp_inicial = int(input("Introduce la temperatura inicial en °C: "))
    temp_final = int(input("Introduce la temperatura final en °C: "))
    print("-" * 40)

    while temp_inicial <= temp_final:
        print(f"{temp_inicial}°C = {( temp_inicial * 9/5) + 32}°F")
        temp_inicial += 1
        
    if input("\nDeseas Continuar? (S/N)").upper() == "N" : break
