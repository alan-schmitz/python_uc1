lisPessoas=[]
for i in range(2):
    pessoa = {}
    pessoa["nome"] =  input("Digite Nome: ")
    pessoa["idade"] =  int(input("Digite idade: "))
    pessoa["cidade"] =  input("Digite cidade: ")
    pessoa["email"] =  input("Digite Email: ")

    lisPessoas.append(pessoa)

print(f"{lisPessoas}")
print(lisPessoas[0]["nome"])
lisPessoas[0]["cel"]="024 99887-6554433"

print(lisPessoas[0])
print(lisPessoas[1])
