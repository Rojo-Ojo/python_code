# p084-triangulo-invertido-numeros.py
# Programa que solicita al usuario un número entero n que determinará la altura de un triángulo numérico invertido. 
# El programa imprime n renglones. El primer renglón contendrá los números de 1 a n, el segundo de 1 a n-1, y así
# sucesivamente hasta que el último renglón contenga solo el número 1.

print("\033[2J\033[H", end="")
print("Programa que solicita al usuario un número entero n que determinará la altura de un triángulo numérico invertido.\n" 
      "El programa imprime n renglones. El primer renglón contendrá los números de 1 a n, el segundo de 1 a n-1, y así\n"
      "sucesivamente hasta que el último renglón contenga solo el número 1.\n")

num = int(input("Dame un número: "))
cont = num
digit = 1

for i in range(1, num+1):
    for j in range(1, cont+1):
        print(digit, end=" ")
        digit += 1
    print()
    digit = 1
    cont -= 1
