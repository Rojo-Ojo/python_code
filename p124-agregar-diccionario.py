# p124-agregar-diccionario.py
# ● Programa que crea un diccionario llamado ventas con los siguientes datos: Juan: 1550, Jose: 2600, Maria: 2220.
# ● Muestra el diccionario.
# ● Agrega los siguientes vendedores y sus ventas al diccionario:
#   o Rocio: 2500 (usando []).
#   o Mateo: 1567 (usando []).
#   o Andrea: 9567 (usando update()).
#   o Miguel: 1234 (usando update()).
# ● Muestra el diccionario actualizado.

print("\033c", end="") # Esto limpia la consola en sistemas compatibles.

ventas = {
    "Juan"  : 1550, 
    "Jose"  : 2600, 
    "Maria" : 2220
}

print("Ventas iniciales:")
print(ventas)

ventas["Rocio"] = 2500
ventas["Mateo"] = 1567
ventas.update({"Andrea" : 9567})
ventas.update({"Miguel" : 1234})

print("\nVentas actualizadas:")
print(ventas)
