# p146-numero-mayor.py
# Función que devuelve el numero mayor de tres números.

print("\033c", end="")  # Limpia la consola (secuencia ANSI, en terminales compatibles)

def numero_mayor(a:int, b:int, c:int) -> int:
    """ Devuelve el numero mayor de tres numeros """
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

#mayor = numero_mayor(40, 20, 30)
#print(f'El numero mayor es: {mayor}')

print('Dame tres numeros enteros separados por <enter>')
n1, n2, n3 = int(input()), int(input()), int(input())

print(f'El numero mayor es: {numero_mayor(n1, n2, n3)}')
