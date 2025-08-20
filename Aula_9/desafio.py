import random
numeros = []
for i in range (100):
    numeros.append(random.randint(1,200))
print(f'{numeros}')

media = sum=(numeros) / len(numeros)

print (f'media: {media}')

maior = []

for valor in numeros:
    if valor > media:
        maior.append(valor)
print(f'maior:  {maior}')
