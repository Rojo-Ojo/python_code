# p100-normalizar-nombres.py
# De una lista de nombres con espacios y mayúsculas, se normalizan los nombres a minúsculas ysin espacios al inicio o final.

print("\033c", end="")
print("\033[1;34m" + "Normalizar nombres.\n" + "\033[0m")

nombres = [" Juan ", " Maria", "Pedro ", "Ana", " Luis "]

# Se normalizan los nombres usando compresión de listas
nombres_normalizados = [nombre.strip(). lower() for nombre in nombres]

print("Nombres originales:", nombres)
print("Nombres normalizados:", nombres_normalizados)
