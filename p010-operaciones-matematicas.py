# p010-operaciones-matematicas.py 
# Demuestra el uso de los operadores aritméticos.

print("\033[2J\033[H", end="")
print("-" * 50)
print("Demuestra el uso de los operadores aritméticos. \n")
print("-" * 50)

x = float(input("Valor de x: "))
y = float(input("Valor de y: "))

suma = x + y
resta = x - y
multi = x * y
divi = x / y
modu = x % y
pot = x ** y
dive = x // y

print("\nResultado de las operaciones realizadas.\n")
print("=" * 50)
print(f"Números: {x} , {y}")
print(f"Suma: {suma:>10.2f}")
print(f"Resta: {resta:>10.2f}")
print(f"Multiplicación: {multi:>10.2f}")
print(f"División: {divi:>10.2f}")
print(f"Módulo: {modu:>10.2f}")
print(f"Potencia: {pot:>10.2f}")
print(f"División Entera: {dive:>10.2f}")

print("=" * 50)
