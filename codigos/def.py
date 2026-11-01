
def calcular_media(notas):
    return sum(notas) / len(notas)


def classificar(media, frequencia):
    if frequencia < 75:
        return "reprovado por falta"
    elif media >= 7:
        return "aprovado"
    elif media >= 5:
        return "recuperacao"
    else:
        return "reprovado por nota"


alunos = []
situacoes = set()

while len(alunos) < 3:
    print("\nCadastro", len(alunos) + 1, "de 3")
    nome = input("Nome completo: ")
    nota1 = float(input("Nota 1 (0 a 10): "))
    nota2 = float(input("Nota 2 (0 a 10): "))
    frequencia = int(input("Frequência (0 a 100): "))

    notas = (nota1, nota2)
    media = calcular_media(notas)
    situacao = classificar(media, frequencia)

    aluno = {
        "nome": nome,
        "notas": notas,
        "frequencia": frequencia,
        "media": media,
        "situacao": situacao
    }

    alunos.append(aluno)
    situacoes.add(situacao)


print("\n========== Resumo da Turma ==========")
qtd_aprovados = 0
soma_medias = 0

for indice in range(len(alunos)):
    aluno = alunos[indice]
    primeiro_nome = aluno["nome"].split()[0]

    print(f"{primeiro_nome}: média {aluno['media']:.1f} | "
        f"frequência {aluno['frequencia']}% | {aluno['situacao']}")

    soma_medias += aluno["media"]

    if aluno["situacao"] == "aprovado":
        qtd_aprovados += 1


media_turma = soma_medias / len(alunos)

print("----------------------------------------")
print("Total de alunos:", len(alunos))
print("Aprovados:", qtd_aprovados)
print(f"Média da turma: {media_turma:.1f}")
print("Situações distintas:", situacoes)
