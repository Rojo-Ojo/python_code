# p143-funcion-retorno.py
# Función que regresa un valor.

print("\033c", end="")  # Limpia la consola (secuencia ANSI, en terminales compatibles)

def suma(a:int, b:int) -> int:
    return a + b

""" res = suma(10,20)
print(res) """

print('Dame dos numeros enteros separados por <enter>')
n1, n2 = int(input()), int(input())
print(f'La suma de {n1} + {n2} es: {suma(n1,n2)}')
