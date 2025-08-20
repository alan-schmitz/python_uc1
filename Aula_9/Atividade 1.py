vetor = [10, 20, 30, 40, 50]
##print("Vetor:", vetor)

##print(f"dato da 4a posicao", {vetor[3]})

#for elemento in vetor :
 #   print(f"Valor de Elemento", {elemento})

#for i in range (5):
  #  print(f"{i}")
   # print(f"{vetor[i]}")

#for f in range (5):
 #   print(f'O valor da {f+1} a posicao e {vetor[f]}')

#indice = 1
#for elemento in vetor:
#    print(f'O Valor do Indice {indice} {elemento}')
 #   indice =  indice + 1

import random
numero = random.randint(1,187)
print(numero)


numeros = []
for i in range (20):
    numeros.append(random.randint(1,187))
print(f'{numeros}')

## prinsipais funcoes 

soma=sum(numeros) # somar 
maior=max(numeros) # mair valor 
menor=min(numeros) # menor Valor 
gt_elementos=len(numeros) # quantidade de elemtos 
menia=soma/gt_elementos   # media dos elementos 

print(f'A soma dos elementos e: {soma:0}') # acrecenta espaço antes do numero 
print(f'O maior Valor e: {maior:09}') #:09 acresenta 0 ante do numero
print(f'O menor Valor e: {menor}')
print(f'A quantidade de elementos e: {gt_elementos}')
print(f'A media dos elementos e: {menia:0}') #formata casa desimal 


#numeracao = [1,2,3,4,5,6,7,8,9,10]
#par = {}
#impar = {}
#for v in numeracao:
 #   if v % 2 == 0:
  #      par.append(v)
 #   else:
 #       impar.append(v)   
#print(f'numeros pares: \n\t {par}')
#print(f'numeros impares: \n\t {impar}')
#print(f"Qt numeros Pares: \n{len par}")
#print(f"Qt numeros Pares: \n{len impar}")  