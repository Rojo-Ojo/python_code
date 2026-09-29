# p090-iterar-lista.py
# Iterar sobre una lista.
# 1 por elemento, 2 por indice, 3 por elemento sumando 2, 4, por indice sumando 10, 5 con enumerate.

nums = [2,4,6,8,10, 12, 14, 16]

print("\033[2J\033[H", end="") # Limpiar pantalla
print(f'Iterar sobre una lista: {nums} | Longitud: {len(nums)}')

# Iterar por elemento
print('\nIterar por elemento:')
for num in nums:
    print(num, end=' ')

# Iterar por índice
print('\nIterar por indice:')
for i in range(len(nums)):
    print(f'Índice {i}: {nums[i]}')

# Iterar por elemento sumando 2
print('\nIterar por elemento sumando 2:')
for num in nums:
    print(num + 2, end=' ')

# Iterar por indice sumando 10
print('\nIterar por indice sumando 10:')
for i in range(len(nums)):
    print(f'Índice {i}: {nums [i] + 10}')

# Iterar con enumerate
print('\nIterar con enumerate:')
for i, num in enumerate(nums) :
    print(f'Índice {i}: {num}')

# Elevar al cuadrado cada elemento y guardar el resultado en la lista original

original = nums.copy()
print('\nElevar al cuadrado cada elemento:')
print(f'Lista original: {original}')
for i in range(len(nums)):
    nums[i] = nums[i] ** 2
print(f'Lista con los elementos al cuadrado: {nums}')
