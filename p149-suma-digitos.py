# p149-suma-digitos.py
# Función que regresa la suma los dígitos de un número entero.

print("\033c", end="")  # Limpia la consola (secuencia ANSI, en terminales compatibles)

def suma_digitos(n:int) -> int:
    """ Regresa la suma de los dígitos de un número entero. """
    suma = 0
    while n > 0:
        digito = n % 10 # toma el digto mas a la derecha
        suma += digito
        n //= 10 # elimina el digito mas a la derecha
    return suma

def main() -> None:
    print('Dame un numero entero: ')
    n = int(input())
    print(f'La suma de los digitos de {n} es: {suma_digitos(n)}')

if __name__ == "__main__":
    main()
