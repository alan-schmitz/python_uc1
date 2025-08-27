alunos = {}

alunos[1] = {"nome": "Maria", "notas": []}
alunos[2] = {"nome": "João", "notas": []}
alunos[3] = {"nome": "Carlos", "notas": []}

alunos[1]["notas"].append(4.0)
alunos[2]["notas"].append(6.5)
alunos[3]["notas"].append(8.0)

alunos[1]["notas"].append(4.0)
alunos[2]["notas"].append(8.0)
alunos[3]["notas"].append(7.5)

alunos[1]["notas"].append(3.0)
alunos[2]["notas"].append(9.5)
alunos[3]["notas"].append(5.0)

alunos[1]["notas"].append(9.0)
alunos[2]["notas"].append(4.5)
alunos[3]["notas"].append(10.0)

for matricula, dados_alunos in alunos.items():
    print(f"Matricula do Aluno........: {matricula}")
    print(f'Nome do Aluno.............: {dados_alunos["nome"]}')
    print(f"Notas do Aluno ...........:")
    for nota in dados_alunos["notas"]:
        print(f"\t\tNota....: {nota}")

    media=sum(dados_alunos["notas"])/len(dados_alunos["notas"])
    #print(f"\t\tmedia.. {media}")

    dados_alunos["media"] = media
    print(f"\t\tmedia.. : {dados_alunos['media']:.2f}")

    if media >= 6:
        dados_alunos["status"]="Aprovado"
    else:
        dados_alunos["status"]="Reprovado"
    print(f"\t\tStatus: {dados_alunos['status']}")

    print("---------------------------------------------------------")