# p095-registro-estudiantes.py
# Planteamiento del problema: Registro de estudiantes para evento
# . Se está organizando un evento y necesitas registrar a los asistentes.
# . El programa debe permitir al usuario introducir el nombre y la edad de cada persona.
# . El registro termina cuando se introduce un * como nombre.
# · Al finalizar, el sistema debe mostrar dos informes:
# · una lista de todos los asistentes que son mayores de edad (18 años o más).
# . y el nombre y la edad de la persona con mayor edad para entregarle un reconocimiento.

print("\033c", end="") # Esto limpia la consola en sistemas compatibles
nombres = []
edades = []

while True:
    nombre = input("Ingrese el nombre del asistente (o '*' para terminar): ")
    if nombre == "*":
        break
    try:
        edad = int(input(f"Ingrese la edad de {nombre}: ") )
        if edad < 0:
            print("Edad inválida. Debe ser un número positivo.")
            continue
        nombres. append (nombre)
        edades. append (edad)
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero para la edad.")

print()

if nombres:
    # Filtrar asistentes mayores de edad
    for i in range(len(edades)):
        if edades [i] >= 18:
            print(f"{nombres [i]} es mayor de edad con {edades [i]} años.")
    # Encontrar la persona con mayor edad
    max_edad = max (edades)
    indice_max_edad = edades. index(max_edad)
    print(f"La persona con mayor edad es {nombres [indice_max_edad]} con {edades [indice_max_edad] } años.")
    