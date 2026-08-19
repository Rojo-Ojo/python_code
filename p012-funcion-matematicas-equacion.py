# p012-funcion-matematicas-equacion.py 
# Ejemplifica el uso de funcions matemáticas dentro de math.
# Evaluar la función f(x, y) = 3x2 + √(x2 + y2) + e^(ln(x))

import math as mt

print("\033[2J\033[H", end="")
print("Funciones de math. \n")

x = int(input("x = "))
y = int(input("y = "))

fxy = 3 * mt.pow(x,2) + mt.sqrt( mt.pow(x,2) + mt.pow(y,2) ) + mt.exp( mt.log(x) )
fxy2 = 3 * x**2 + mt.sqrt( x**2 + y**2 ) + mt.exp( mt.log(x) )

print(f"El resultado es: {fxy:.2f}")
print(f"El resultado es: {fxy2:.2f}")
