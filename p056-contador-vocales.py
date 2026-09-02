# p056-contador-vocales.py
# Dada una frase, cuenta vocales, consonantes y otros.

print("\033[2J\033[H", end="")
print("Dada una frase, cuenta vocales, consonantes y otros.\n")

frase = input("Introduce una frase: ")
print(f"\nLa frase a analizar es: \"{frase}\" y tiene {len(frase)} caracteres.")
frase = frase.lower()

i = vocal = consonante = otro = 0
while i < len(frase):
    c = frase[i]
    #print(c, end="")
    if "a" <= c <= "z":
        if c in "aeiou":
            vocal += 1
        else:
            consonante += 1
    else:
        otro += 1
    i += 1

print(f"\nVocales: {vocal}\nConsonantes: {consonante}\nOtros: {otro}")
