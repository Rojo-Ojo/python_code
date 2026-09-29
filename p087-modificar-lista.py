# p087-modificar-lista.py
# Modificar los elementos de una lista.

print("\033[2J\033[H", end="") # Limpiar pantalla
print('Modificar los elementos de una lista')

califs = [10, 9, 8.5, 6.5, 9.8, 7, 5, 6.2, 9.5]

print('\nLongitud y contenido de las calificaciones:')
print(f'Longitud: {len(califs)}')
print(f'Contenido: {califs}')

print('\nModificación de elementos: 0 y 1')
califs[0] = 7
califs[1] = 7
print(f'Contenido actualizado: {califs}')

print('\nModificación de elemento en el rango de 2 a 5 (sin incluir el 5)')
califs [2:5] = [9, 9, 9]
print(f'Contenido actualizado: {califs}')