# p132-coordenadas.py
# Registro de coordenadas geográficas usando tuplas.

print("\033c", end="") # Esto limpia la consola en sistemas compatibles.

# Definición de tuplas para las coordenadas de dos ciudades.
zacatecas = ("Zacatecas", 22.77, -102.58)
guadalupe = ("Guadalupe", 22.75, -102.52)

# Acceso a los elementos de la tupla usando índices.
print("Coordenadas de Zacatecas:")
print("Tipo: ", type(zacatecas))
print("Ciudad: ", zacatecas [0])
print("Latitud: ", zacatecas [1])
print("Longitud: ", zacatecas [2])

# Acceso a los elementos de la tupla usando desempaquetado.
ciudad, latitud, longitud = guadalupe
print("\nCoordenadas de Guadalupe:")
print("Tipo: ", type(guadalupe))
print("Ciudad: ", ciudad)
print("Latitud : ", latitud)
print("Longitud: ", longitud)

# Iteración sobre una lista de tuplas para mostrar las coordenadas de ambas ciudades.
for lugar in [zacatecas, guadalupe]:
    print("\nCoordenadas de", lugar [0])
    print("Latitud : ", lugar [1])
    print("Longitud: ", lugar [2])

# Desempaquetado ignora el primer elemento (nombre de la ciudad) y obtiene las coordenadas.
_, lat1, lon1 = zacatecas
_, lat2, lon2 = guadalupe

# Cálculo del punto medio entre las dos coordenadas.
centro =((lat1+ lat2) / 2, (lon1 + lon2) / 2)
print("\nPunto medio ", centro)

# Verificar pertenenecia.
print("\nZacatecas pertenece a la tupla: ",
"Zacatecas" in zacatecas)

# Crear otra tupla con datos extra.
ampliada = zacatecas + ("México",)

print("\nTupla original: ", zacatecas)
print("Tupla ampliada: ", ampliada)