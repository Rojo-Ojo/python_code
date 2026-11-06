# p139-funcion-parametros.py
# Ejemplo de función con varios parámetros.

print("\033c", end="")  # Limpia la consola (secuencia ANSI, en terminales compatibles)

def saluda(apaterno:str, nombre:str) -> None :
    print(f'Hola {nombre} {apaterno}')

saluda('Castaneda', 'Carlos')
# saluda('Carlos Castaneda')
# saluda('Castaneda', 'Ramirez', 'Carlos')
