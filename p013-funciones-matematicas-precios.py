# p013-funciones-matematicas-precios.py
# Demostrar el uso de funciones matemáticas de redondeo.

import math as mt

print("\033[2J\033[H", end="")
print("Funciones de redondeo. \n")

precio = 15.49234

print(f"Precio Original ${precio:.2F}")
print(f"Arriba          $ {mt.ceil(precio):.2f}")
print(f"Abajo           $ {mt.floor(precio):.2f}")
print(f"Truncar         $ {mt.trunc(precio):.2f}")
print(f"Automático      $ {round(precio):.2f}")
print(f"Automático dec  $ {round(precio,3)}")
