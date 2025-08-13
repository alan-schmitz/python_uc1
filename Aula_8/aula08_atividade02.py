def main():
   print("\n\n\tOlá, mundo!\n")

##if __name__ == "__main__":
   ##main()

#def somar_numeros ():
   #n1=float(input("Digite o primeiro numero: "))
   #n2=float(input("Digite o segundo numero: "))
   #Soma = n1 + n2
   #print(Soma)

#somar_numeros()

def soma(a,b):
   somar = a + b
   return somar

def subtraca(d,f):
   sub = d - f
   return sub

def resultado():
    resultado_soma = soma (5,5)
    print(f"soma: {resultado_soma}")
    resultado_subtracao = subtraca (20,5)
    print(f"Subtração: {resultado_subtracao}")

#resultado()


def nuninpar():
   for i in range (1,11,+2):
      print(i)

#nuninpar()