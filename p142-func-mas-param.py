# p142-func-mas-param.py
# Función que recibe n parámetros y los imprime en pantalla.

print("\033c", end="")  # Limpia la consola (secuencia ANSI, en terminales compatibles)

def saluda(*nombres:str) -> None:
    print(nombres)
    for nombre in nombres:
        print(f'Hola {nombre} bienvenido a python, tu nombre tiene {len(nombre)} caracteres')

def edades(*edaes: int) -> None:
    print(edaes)
    for edad in edaes:
        print(f'Tu edad es: {edad} años')

saluda('Carlos Castaneda', 'Juan', 'Pedro')
edades(25, 30, 35)
