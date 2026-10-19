# p131-conjunto-numeros.py
# Dadas las siguientes tres listas de números:
# ● Lista 1: 50, 60, 70, 80, 90, 100, 200
# ● Lista 2: 60, 90, 100, 300, 400, 500
# ● Lista 3: 10, 20, 60, 90, 70, 100, 600, 700
# 1. Crear y mostrar los conjuntos A, B y C a partir de las listas.
# 2. Calcular y mostrar los resultados de las siguientes operaciones:
#   o Unión (A | B)
#   o Unión (B | C)
#   o Diferencia (A - C)
#   o Diferencia Simétrica (B ^ C)
#   o Intersección (B & C)
# 3. Verificar y mostrar el resultado (Verdadero/Falso) de las siguientes preguntas:
#   o ¿Es A subconjunto de B?
#   o ¿Es C subconjunto de A?
#   o ¿Está el número 100 en A?
#   o ¿Está el número 60 en A, B y C?
#   o ¿No está el número 900 en C?

print("\033c", end="") # Esto limpia la consola en sistemas compatibles.

lista_1 = [50, 60, 70, 80, 90, 100, 200]
lista_2 = [60, 90, 100, 300, 400, 500]
lista_3 = [10, 20, 60, 90, 70, 100, 600, 700]

A = set(lista_1)
B = set(lista_2)
C = set(lista_3)

print(f"Conjunto A basado en Lista 1: {A}")
print(f"Conjunto B basado en Lista 2: {B}")
print(f"Conjunto C basado en Lista 3: {C}")

print(f"\nUnión (A | B): {A | B}")
print(f"Unión (B | C): {B | C}")
print(f"Diferencia (A - C): {A - C}")
print(f"Diferencia Simétrica (B ^ C): {B ^ C}")
print(f"Intersección (B & C): {B & C}")

print(f"\n¿Es A subconjunto de B? {A.issubset(B)}")
print(f"¿Es C subconjunto de A? {C.issubset(A)}")
print(f"¿Está el número 100 en A? {100 in A}")
print(f"¿Está el número 60 en A, B y C? {60 in A and 60 in B and 60 in C}")
print(f"¿No está el número 900 en C? {900 not in C}")
