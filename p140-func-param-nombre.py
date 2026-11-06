# p140-func-param-nombre.py
# Ejemplo de función con parámetros con nombre.

print("\033c", end="")  # Limpia la consola (secuencia ANSI, en terminales compatibles)

def saluda(apaterno:str, amaterno:str, nombre:str) -> None :
    print(f'Hola {nombre} {apaterno} {amaterno}')

saluda('Castaneda', 'Ramirez', 'Carlos')
saluda(nombre='Carlos', amaterno='Ramirez', apaterno='Castaneda')
# saluda(nombre='Carlos')
