# p126-procesar-diccionario.py
# ● Programa que define dos listas:
#   o nombres = ['Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto']
#   o sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]
# ● Crea un diccionario nómina combinando ambas listas (los nombres son las llaves, los sueldos son los valores).
# ● Muestra el diccionario nómina resultante.
# ● Itera sobre el diccionario y muestra su contenido de cuatro formas:
#   o Mostrando solo las llaves (usando keys()).
#   o Mostrando solo los valores (usando values()).
#   o Iterando por las llaves y accediendo al valor (ej. for llave in dic: ...).
#   o Mostrando la llave y el valor simultáneamente (usando items()).
# ● Calcula y muestra la suma total de los sueldos.
# ● Calcula y muestra el promedio de los sueldos.

print("\033c", end="") # Esto limpia la consola en sistemas compatibles.

nombres = ['Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto']
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]

nomina = dict(zip(nombres, sueldos))
print("Diccionario de nómina:")
print(nomina)

print("\n--- Iterando Llaves (keys) ---")
keys = nomina.keys()
for keys in keys:
    print(keys)

print("\n--- Iterando Valores (values) ---")
values = nomina.values()
for values in values:
    print(values)

print("\n--- Iterando Llave y Valor (accediendo por llave) ---")
for keys in nomina:
    print(f"{keys} -> {nomina[keys]}")

print("\n--- Iterando Llave y Valor (items) ---")
suma = 0
for item in nomina.items():
    print(item)
    suma += item[1]

print("\n--- Cálculos ---")
print(f"Suma total de sueldos: {suma:.2f}")
print(f"Promedio de sueldos: {suma / len(nomina.items()):.2f}")
