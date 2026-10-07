# p114-nombres-edades.py
# Censo de nombres y edades en un diccionario, hasta <Enter> vacío.

print("\033c", end="") # Esto limpia la consola en sistemas compatibles.

# Crear un diccionario para almacenar los nombres y edades.
censo = {}

# Solicitar al usuario que ingrese nombres y edades hasta que ingrese un nombre vacío.
while True:
    nombre = input("Ingrese un nombre (o presione <Enter> para salir): ")
    if nombre == "":
        break
    censo [nombre] = int(input(f"Ingrese la edad de {nombre}: "))

# Mostrar el censo de nombres y edades
print(f"\nCenso de nombres y edades: {censo} - {len(censo)} elementos")

# Resumen del censo.
print('\nResumen del censo:')
for nombre, edad in censo.items():
    print(f"- {nombre}: {edad} años")

suma_edades = sum(censo.values()) # Sumar todas las edades.
promedio_edades = suma_edades / len(censo) if censo else 0 # Promedio de edades, evitando división por cero.
print(f"\nSuma de edades: {suma_edades} años")
print(f"Promedio de edades: {promedio_edades: .2f} años")
