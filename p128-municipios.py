# p128-municipios.py
# Gestion de un padron municipal usando conjuntos

municipios = {"Zacatecas", "Guadalupe", "Fresnillo", "Jerez", "Sombrerete", "Fresnillo"}

print("\033c", end="") # Esto limpia la consola en sistemas compatibles.

print("Padrón de municipios")
print("---------------------")
print("Municipios registrados:")
print(type(municipios))
for municipio in municipios:
    print(municipio)
# Consultar si un municipio esta registrado
print("\nEstá Zacatecas dentro de los Municipios registrados? ", "Zacatecas" in municipios)

# Altas al padron de municipios
print("\nAgregando un municipio al padrón")
municipios.add("Calera")
print(f"Municipios registrados: {municipios} - {len(municipios)}")

# Agregar varios municipios al padrón
print("\nAgregando varios municipios al padrón")
otros = {"Concepción del Oro", "Jalpa", "Villanueva"}
municipios.update(otros)
print(f"Municipios registrados: {municipios} - {len(municipios)}")

# Eliminar un municipio del padron con remove
print("\nEliminando un municipio del padrón")
municipios.remove("Jerez")
print(f"Municipios registrados: {municipios} - {len(municipios)}")

# Eliminar un municipio del padron con discard
print("\nEliminando un municipio del padrón")
municipios.discard("Sombrerete")
print(f"Municipios registrados: {municipios} - {len(municipios)}")

# Eliminar un municipio del padron con pop
print("\nEliminando un municipio del padrón")
municipio_eliminado = municipios.pop()
print(f"Municipio eliminado: {municipio_eliminado}")
print(f"Municipios registrados: {municipios} - {len(municipios)}")

# Eliminar todos los municipios del padrón
print("\nEliminando todos los municipios del padrón")
municipios.clear()
print(f"Municipios registrados: {municipios} - {len(municipios)}")
