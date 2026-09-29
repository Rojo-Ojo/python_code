# p091-lista-de-gastos.py
# Desarrolla una aplicación que almacene gastos en una lista y permita al usuario
# manipularla a través de un menú que se mostrará continuamente hasta que decida salir.

gastos = []

while True:
    print('\033[H\033[2J')  # Limpiar pantalla
    print('Aplicación de gastos')
    print('1. Ver gastos')
    print('2. Agregar gasto')
    print('3. Modificar gasto')
    print('4. Eliminar gasto')
    print('5. Ver total')
    print('6. Salir')
    opcion = input('Elige una opción: ')

    if opcion == '1':
        if len(gastos) == 0:
            print('No hay gastos registrados.')
        else:
            print('Gastos actuales:')
            for indice in range(len(gastos)):
                print(f'{indice + 1}. {gastos[indice]:.2f}')
            print('Operación exitosa: gastos mostrados.')

    elif opcion == '2':
        try:
            gasto = float(input('Ingresa el monto del gasto: '))
        except ValueError:
            print('Error: el monto debe ser un número.')
        else:
            gastos.append(gasto)
            print(f'Operación exitosa: gasto de {gasto:.2f} agregado.')

    elif opcion == '3':
        try:
            indice = int(input('Ingresa el número del gasto a modificar: ')) - 1
        except ValueError:
            print('Error: el número de gasto debe ser un entero.')
        else:
            if indice < 0 or indice >= len(gastos):
                print('Error: gasto no encontrado.')
            else:
                try:
                    nuevo_gasto = float(input('Ingresa el nuevo monto del gasto: '))
                except ValueError:
                    print('Error: el monto debe ser un número.')
                else:
                    gastos[indice] = nuevo_gasto
                    print(f'Operación exitosa: gasto modificado a {nuevo_gasto:.2f}.')

    elif opcion == '4':
        try:
            indice = int(input('Ingresa el número del gasto a eliminar: ')) - 1
        except ValueError:
            print('Error: el número de gasto debe ser un entero.')
        else:
            if indice < 0 or indice >= len(gastos):
                print('Error: gasto no encontrado.')
            else:
                gasto_eliminado = gastos.pop(indice)
                print(f'Operación exitosa: gasto de {gasto_eliminado:.2f} eliminado.')

    elif opcion == '5':
        if len(gastos) == 0:
            print('No hay gastos registrados.')
        else:
            total = sum(gastos)
            print(f'Total de gastos: {total:.2f}')

    elif opcion == '6':
        print('Saliendo de la aplicación...')
        break

    else:
        print('Error: opción no válida.')

    input('\nPresiona Enter para continuar...')