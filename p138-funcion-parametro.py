# p138-funcion-parametro.py
# Ejemplo de una función con parámetros.

print("\033c", end="")  # Limpia la consola (secuencia ANSI, en terminales compatibles)

def saluda(nombre:str) -> None:
    print(f'Hola {nombre} bienvenido a python, tu nombre tiene {len(nombre)} caracteres')

saluda('Carlos Castaneda')
saluda('Juan Perez Diaz')
saluda( 'Maria Soto Garcia')
saluda('Carlos Antonio')
