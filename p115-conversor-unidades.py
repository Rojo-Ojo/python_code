# p115-conversor-unidades.py
# Definir un diccionario conversiones que almacene los
# factores para convertir 'km', 'm', 'cm', y 'mm' a metros.

print("\033c", end="") # Esto limpia la consola en sistemas compatibles.

# Definir el diccionario de conversiones.
conversiones = {
    "km": 1000.0,   # 1 km = 1000 m
    "m": 1.0,       # 1 m = 1 m
    "cm": 0.01,     # 1 cm = 0.01 m
    "mm": 0.001     # 1 mm = 0.001 m
}

# Solicitar al usuario que ingrese la cantidad y la unidad de origen y valida unidad válida.
cantidad = float(input("Ingrese la cantidad a convertir: "))
while True:
    unidad_origen = input("Ingrese la unidad de origen (km, m, cm, mm): "). lower()
    if unidad_origen in conversiones:
        break
    print("Unidad de origen no valida. Intente nuevamente.")

# Mostrar el resultado de la conversión en metros.
metros = cantidad * conversiones [unidad_origen]
print("\nResultado de la conversión:")
print(f"{cantidad} {unidad_origen} son {metros :.2f} metros.")
