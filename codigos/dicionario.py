##Tarefa de casa dia 27/08/2026
##Professor Abrãoo
aluno = {
    "nome": "Jardel",
    "idade": 20,
    "curso": "Análise e Desenvolvimento de Sistemas",
    "semestre": "4",
    "email": "luizjardel13@gmail.com"
    
}
print(f"{aluno['nome']}")
print(f"{aluno['idade']}")
print(f"{aluno['curso']}")
print(f"{aluno['semestre']}")
print (type(aluno))

aluno["semestre"] = "5"
print(aluno)

aluno["nota"] = 7.0

print(f"{aluno['nome']}")
print(f"{aluno['curso']}")
print(f"{aluno['nota']}")