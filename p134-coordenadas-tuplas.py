# p134-coordenadas-tuplas.py
# Representa mediante tuplas las coordenadas de las siguientes ciudades:
# ● Zacatecas: nombre, latitud 22.77 y longitud -102.58
# ● Guadalupe: nombre, latitud 22.75 y longitud -102.52
# Instrucciones:
# ● Crear y mostrar las tuplas de Zacatecas y Guadalupe. Imprimir su tipo y consultar el nombre, la latitud y la longitud usando índices positivos y negativos.
# ● Desempaquetar cada tupla en variables e imprimir las coordenadas con el formato nombre: (latitud, longitud).
# ● Recorrer ambas ubicaciones con un ciclo y mostrar para cada una el nombre y la tupla de coordenadas obtenida con slicing.
# ● Calcular e imprimir el punto medio aproximado entre las dos ubicaciones usando las latitudes y longitudes.
# ● Crear una nueva tupla para Zacatecas que incluya el código "ZAC". Mostrar la tupla nueva y comprobar que la original no cambió.
# ● Verificar si "Zacatecas" pertenece a su tupla. En un comentario, indicar qué ocurriría si se intentara reemplazar directamente uno de sus elementos.

print("\033c", end="") # Esto limpia la consola en sistemas compatibles.

# Definición de tuplas para las coordenadas de dos ciudades.
zacatecas = ("Zacatecas", 22.77, -102.58)
guadalupe = ("Guadalupe", 22.75, -102.52)

# Mostrar el contenido de cada tupla y su tipo de dato. 
print(f"Tupla Zacatecas: {zacatecas}, Tipo: {type(zacatecas)}")
print(f"Tupla Guadalupe: {guadalupe}, Tipo: {type(guadalupe)}")

# Acceso a los elementos de la tupla Zacatecas mediante índices positivos y negativos.
print("Acceso por índices (Zacatecas):")
print(f"  Positivos -> Nombre: {zacatecas [0]}, Latitud: {zacatecas [1]}, Longitud: {zacatecas [2]}")
print(f"  Negativos -> Nombre: {zacatecas [-3]}, Latitud: {zacatecas [-2]}, Longitud: {zacatecas [-1]}")

# Desempaquetado de tuplas.
ciudad, latitud, longitud = zacatecas
print(f"{ciudad}: ({latitud}, {longitud})")
ciudad, latitud, longitud = guadalupe
print(f"{ciudad}: ({latitud}, {longitud})")

# Recorrer y desempaquetar tuplas.
for lugar in [zacatecas, guadalupe]:
    print(f"Ubicación: {lugar [0]}, Coordenadas: {lugar [-2:]}")

_, lat1, lon1 = zacatecas
_, lat2, lon2 = guadalupe

# Cálculo de centro entre dos puntos.
centro =((lat1+ lat2) / 2, (lon1 + lon2) / 2)
print(f"Punto medio aproximado: ({', '.join(f'{x:.2f}' for x in centro)})")

# Creación de tupla ampliada.
ampliada = zacatecas + ("ZAC",)
print("Nueva tupla Zacatecas: ", ampliada)
print("Original sin cambios: ", zacatecas)

# Verificación de pertenencia a la tupla.
print(f"{zacatecas[0]} pertenece a la tupla: {"Zacatecas" in zacatecas}")
print("# Nota: Intentar modificar un elemento directamente arroja TypeError (las tuplas son inmutables).")
