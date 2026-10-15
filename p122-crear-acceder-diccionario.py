# p122-crear-acceder-diccionario.py
# ● Programa que crea un diccionario llamado dias usando llaves numéricas para los días de la semana.
# ● Muestra el diccionario completo.
# ● Accede y muestra los siguientes valores específicos:
#   o El valor de la llave 1 (usando []).
#   o El valor de la llave 7 (usando []).
#   o El valor de la llave 5 (usando get()).
#   o El valor de la llave 7 (usando get()).
# ● Vuelve a mostrar el diccionario completo.

print("\033c", end="") # Esto limpia la consola en sistemas compatibles.

dias = {
    1: 'Lunes', 
    2: 'Martes', 
    3: 'Miércoles', 
    4: 'Jueves', 
    5: 'Viernes', 
    6: 'Sábado', 
    7: 'Domingo'
}

print("Diccionario inicial:")
print(dias)

print("\nAccediendo a elementos:")
print(f"Llave 1 (con []): {dias[1]}")
print(f"Llave 7 (con []): {dias[7]}")
print(f"Llave 5 (con get()): {dias.get(5)}")
print(f"Llave 7 (con get()): {dias.get(7)}")

print("\nDiccionario final:")
print(dias)
