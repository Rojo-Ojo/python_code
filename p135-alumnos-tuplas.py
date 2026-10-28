# p135-alumnos-tuplas.py
# Modela el siguiente registro escolar como una tupla de alumnos. Cada alumno contiene nombre, carrera y una tupla de calificaciones:
# ● ("Ana", "ISC", (9, 10, 9, 8))
# ● ("Luis", "ISW", (8, 8, 9, 10))
# ● ("Mar", "ISC", (10, 9, 10, 10))
# Instrucciones:
# ● Crear y mostrar la tupla externa con los tres registros. Imprimir cuántos alumnos contiene.
# ● Recorrer los registros mediante desempaquetado y mostrar el nombre, la carrera y el promedio de cada alumno con dos decimales.
# ● Construir y mostrar una nueva tupla con pares (nombre, promedio). Identificar e imprimir el alumno con el promedio más alto.
# ● Consultar las calificaciones usando índices de tuplas anidadas. Para cada alumno, mostrar cuántas veces aparece 10 con count() y la posición de la primera calificación con index().
# ● Ordenar los pares (nombre, promedio) por promedio de menor a mayor usando sorted() y mostrar el resultado como una tupla.
# ● Formar y mostrar una tupla nueva con el nombre "Eva", la carrera "ISC" y las calificaciones (9, 9, 10), sin modificar la tupla original de alumnos.

print("\033c", end="") # Esto limpia la consola en sistemas compatibles.

# Crear y mostrar la tupla de alumnos.
alumnos = (
("Ana", "ISC", (9,10,9,8)),
("Luis", "ISW", (8,8,9,10)),
("Mar", "ISC", (10,9,10,10))
)

print("Registro de alumnos: ", alumnos)
print("Total de alumnos: ", len(alumnos))

# Mostrar el promedio de cada alumno mediante desempaquetado.
for nombre, carrera, calificaciones in alumnos:
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"Nombre: {nombre}, Carrera: {carrera}, Promedio: {promedio:.2f}")

#  Crear pares (nombre, promedio).
promedios = tuple(
    (nombre, sum(calificaciones) / len(calificaciones))
    for nombre, carrera, calificaciones in alumnos
)

print("Pares (nombre, promedio):", promedios)

# Identificar al alumno con el mejor promedio.
mejor_alumno = promedios[0]

for alumno in promedios:
    if alumno[1] > mejor_alumno[1]:
        mejor_alumno = alumno

print(f"Alumno con mejor promedio: {mejor_alumno[0]} con {mejor_alumno[1]}")

# Consultar calificaciones mediante índices, count() e index().
for i in range(len(alumnos)):
    nombre = alumnos[i][0]
    calificaciones = alumnos[i][2]

    conteo_diez = calificaciones.count(10)
    indice_primera = calificaciones.index(calificaciones[0])

    print(
        f"{nombre} -> Conteo de 10s: {conteo_diez}, "
        f"Índice de primera calificación: {indice_primera}"
    )

# Ordenar los pares por promedio de menor a mayor.
ordenados = tuple(sorted(promedios, key=lambda alumno: alumno[1]))
print("Ordenados por promedio:", ordenados)

# Crear una nueva tupla con Eva sin modificar la original.
eva = ("Eva", "ISC", (9, 9, 10))
nuevos_alumnos = alumnos + (eva,)

print("Tupla original intacta:", alumnos)
print("Nueva tupla con Eva:", nuevos_alumnos)
