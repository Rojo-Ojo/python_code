# p025-verificar-suma.py
# Dados tres números enteros, verifica si la suma de los dos primeros e igual al tercero.
# 10+20 == 30 (son iguales) 5+8 == 5 (son diferentes)

print("\033[2J\033[H", end="")
print("Dados tres números enteros, verifica si la suma de los dos primeros e igual al tercero.")

n1 = int(input("\nNúmero 1: "))
n2 = int(input("Número 2: "))
n3 = int(input("Número 3: "))

if n1 + n2 == n3 :
    print(f"\n✅ {n1} + {n2} = {n3} Son iguales.")
else :
    print(f"\n❌ {n1} + {n2} = {n3} Son diferentes.")

print("\nFin del programa.")
