# p147-estacion-año.py
# Función que regresa la estación del año según el numero del mes.

print("\033c", end="")  # Limpia la consola (secuencia ANSI, en terminales compatibles)

def estacion_año(mes: int) -> str:
    """ Devuelve la estacion del año segun el numero del mes """
    meses = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio',
             7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}
    if mes in [12, 1, 2]:
        return meses [mes] + ' y es Invierno'
    elif mes in [3, 4, 5]:
        return meses [mes] + ' y es Primavera'
    elif mes in [6, 7, 8]:
        return meses [mes] + ' y es Verano'
    elif mes in [9, 10, 11]:
        return meses [mes] + ' y es Otoño'

input = int(input('Dame el número del mes (1-12): '))
print(f'Corresponde a : {estacion_año(input)}')
