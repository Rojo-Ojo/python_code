# p082-cuadro-hueco-caracter.py
# Programa que solicita al usuario que ingrese el tamaño del lado de un cuadrado y el carácter con el que se dibujará. 
# Luego, imprime en la consola un "cuadrado hueco", donde el carácter solo se utiliza para dibujar el contorno del mismo.

print("\033[2J\033[H", end="")
print("Programa que solicita al usuario que ingrese el tamaño del lado de un cuadrado y el carácter con el que se dibujará.\n" 
      "Luego, imprime en la consola un \"cuadrado hueco\", donde el carácter solo se utiliza para dibujar el contorno del mismo.\n")

lado = int(input("¿De qué tamaño será el lado del cuadrado? "))
caracter = input("¿Qué carácter quieres usar? ")

for i in range(1, lado+1):
    if i == 1 or i == lado:
            for j in range(1, lado+1):
                  print(caracter + " ", end="")
            print()
    else:
            print(caracter, end="")
            for k in range(1, lado+3):
                  print(" ", end="")
            print(caracter)
