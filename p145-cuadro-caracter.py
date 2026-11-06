# p145-cuadro-caracter.py
# Imprime un cuadro de caracteres.

print("\033c", end="")  # Limpia la consola (secuencia ANSI, en terminales compatibles)

def cuadro_caracter(caracter:str, ancho:int, alto:int) -> None:
    """ Imprime un cuadro de caracteres """
    for i in range(alto):
        for j in range(ancho) :
            print(caracter, end='')
        print()

# cuadro_caracter('*', 10, 5)
caracter = input('Dame un caracter: ')
ancho = int(input('Dame el ancho: '))
alto = int(input('Dame el alto: '))
cuadro_caracter(caracter, ancho, alto)
