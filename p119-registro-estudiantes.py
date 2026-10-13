# p119-registro-estudiantes.py
# Crear una lista de diccionarios para almacenar los datos de varios estudiantes,
# nombre, edad, carrera y promedio.

estudiantes = [
    {"nombre": "Juan Perez", "edad": 20, "carrera": "Ingenieria de Sistemas", "promedio": 8.5},
    {"nombre": "Maria Lopez", "edad": 22, "carrera": "Medicina", "promedio": 9.2},
    {"nombre": "Carlos Garcia", "edad": 21, "carrera": "Arquitectura", "promedio": 8.7}
]

print("\033c", end="") # Esto limpia la consola en sistemas compatibles.

# Mostrar los datos de cada estudiante en la lista.
print(f"\nTodos los estudiantes: {estudiantes} - {len(estudiantes)} elementos ")

# Captura de datos de un nuevo estudiante, hasta nombre vacio.
while True:
    nombre = input("Ingrese el nombre del estudiante (o presione Enter para salir): ")
    if nombre == "":
        break
    edad = int(input("Ingrese la edad del estudiante: "))
    carrera = input("Ingrese la carrera del estudiante: ")
    promedio = float(input("Ingrese el promedio del estudiante: "))
    estudiantes. append( {"nombre": nombre, "edad": edad, "carrera": carrera, "promedio": promedio})
    print(f"Estudiante {nombre} agregado correctamente.")

print(f"\nTodos los estudiantes: {estudiantes} - {len(estudiantes)} elementos ")

# Mostrar los datos en forma de tabla.
print("\nDatos de los estudiantes en forma de tabla:")
for k in estudiantes [0].keys():
    print(f"{k:<15}", end=" | ")
print()
for estudiante in estudiantes:
    for v in estudiante. values():
        print(f"{v:<15}", end=" | ")
    print()

# Mostrar los datos en forma de registro.
print("\nDatos de los estudiantes en forma de registro:")
for estudiante in estudiantes:
    for k, v in estudiante. items():
        print(f"{k}: {v}")
    print()

# Calcular la suma y el promedio de los promedios de los estudiantes.
suma_promedios = sum(estudiante["promedio"] for estudiante in estudiantes)
promedio_general = suma_promedios / len(estudiantes)
print(f"\nSuma de los promedios: {suma_promedios}")
print(f"Promedio general de los estudiantes: {promedio_general:.2f}")

# Calcular el promedio de edad de los estudiantes.
suma_edades = sum(estudiante["edad"] for estudiante in estudiantes)
promedio_edad = suma_edades / len(estudiantes)
print(f"\nSuma de las edades: {suma_edades}")
print(f"Promedio de edad de los estudiantes: {promedio_edad:.2f}")
