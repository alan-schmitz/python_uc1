import random

Matriz1=[]
Matriz2=[]

for i in range(10):
    linha=[]
    linha2=[]
    for j in range(10):
        valor = random.randint(1,129)
        valor2 = random.randint(1,122)
        linha.append(valor)
        linha2.append(valor2)
    Matriz1.append(linha)
    Matriz2.append(linha2)

print(f"{Matriz1}")
print(f"{Matriz2}")

soma=[]

for i in range(10):
    linha=[]
    for j in range(10):
        ad = Matriz1[i][j] + Matriz2[i][j]
        linha.append(ad)
    soma.append(linha)
print(f'{soma}')

media = 0
mult = 0
for i in range(10):
    for i in range(10):
        mult = mult + soma[i][j] 
media = mult / 100

print(f'{media}')