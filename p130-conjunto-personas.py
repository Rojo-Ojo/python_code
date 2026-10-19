# p130-conjunto-personas.py
# Dadas las siguientes dos listas de nombres:
# ● Lista 1: Juan, Maria, Pedro, Jose, Rocio
# ● Lista 2: Pedro, Juan, Pablo, Mateo, Esther
# 1. Crear y mostrar los conjuntos A (basado en la Lista 1) y B (basado en la Lista 2).
# 2. Calcular y mostrar los resultados de las siguientes operaciones:
#   o Unión (A | B)
#   o Intersección (A & B)
#   o Diferencia (A - B)
#   o Diferencia Simétrica (A ^ B)
# 3. Verificar y mostrar el resultado (Verdadero/Falso) de las siguientes afirmaciones:
#   o ¿Es {Pablo, Mateo} un subconjunto de B?
#   o ¿Es A un superconjunto de {Reynaldo, Angelica}?
#   o ¿Está "Pedro" en el conjunto A?
#   o ¿No está "Lilia" en el conjunto B?

print("\033c", end="") # Esto limpia la consola en sistemas compatibles.

lista_1 = ["Juan", "Maria", "Pedro", "Jose", "Rocio"]
lista_2 = ["Pedro", "Juan", "Pablo", "Mateo", "Esther"]

A = set(lista_1)
B = set(lista_2)

print(f"Conjunto A basado en Lista 1: {A}")
print(f"Conjunto B basado en Lista 2: {B}")

print(f"\nUnión (A | B): {A | B}")
print(f"Intersección (A & B): {A & B}")
print(f"Diferencia (A - B): {A - B}")
print(f"Diferencia Simétrica (A ^ B): {A ^ B}")

C = {"Pablo", "Mateo"}
D = {"Reynaldo", "Angelica"}

print(f"\n¿Es {{Pablo, Mateo}} un subconjunto de B? {C.issubset(B)}")
print(f"¿Es A un superconjunto de {{Reynaldo, Angelica}}? {A.issuperset(D)}")
print(f"¿Está \"Pedro\" en el conjunto A? {"Pedro" in A}")
print(f"¿No está \"Lilia\" en el conjunto B? {"Lilia" not in B}")
