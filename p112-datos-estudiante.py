# p112-datos-estudiante.py
# Gestión de datos de estudiante con un diccionario.

print("\033c", end="") # Esto limpia la consola en sistemas compatibles.

estudiante = {
    "nombre": "Juan Pérez",
    "edad": 20,
    "carrera": "Ingeniería de Sistemas",
    "email": "juan.perez@example.com"
}

print(f"Datos del estudiante: {estudiante} - {len(estudiante)} elementos")

# Modificar un dato del estudiante.
estudiante["edad"] = 21
estudiante["email"] = "juanito@gmail.com"
print(f"Datos del estudiante: {estudiante} - {len(estudiante)} elementos")

# Agregar un nuevo dato al estudiante.
estudiante["promedio"] = 8.5
print(f"Datos del estudiante: {estudiante} - {len(estudiante)} elementos")

# Mostrar las llaves del diccionario.
print('\nLas llaves son:')
for key in estudiante. keys():
    print(f" - {key}")

# Mostrar los valores del diccionario.
print('\nLos valores son:')
for value in estudiante.values():
    print(f" - {value}")

# Mostrar las llaves y valores del diccionario.
print('\nLas llaves y valores son:')
for key, value in estudiante.items():
    print(f" - {key}: {value}")
