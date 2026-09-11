#Tarefa do Professor de  Python,selecao de candidato  (baseado na LTD dia  10/09/2026)
print("=" * 45)
print(" SELEÇÃO PARA O PROJETO ")
print("=" * 45)

# Dados definidos pela instituição
conhecimentos_exigidos = {
    "python",
    "lógica",
    "git",
    "banco de dados",
    "html"
}
turnos_disponiveis = ("manhã", "tarde")


nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))
curso = input("Qual o seu curso? ")
semestre = int(input("Qual o seu semestre? "))
email = input("Qual o seu email? ")

conhecimentos_str = input("Informe seus conhecimentos separados por vírgula: ")
turnos_str = input("Informe seu(s) turno(s) disponível(is) separados por vírgula (manhã, tarde): ")

trabalha_em_equipe = input("Aceita trabalhar em equipe? (sim/não) ").strip().lower() == "sim"
computador_proprio = input("Possui computador próprio? (sim/não) ").strip().lower() == "sim"


conhecimentos_candidato = {
    c.strip().lower() for c in conhecimentos_str.split(",") if c.strip() != ""
}
turnos_candidato = {
    t.strip().lower() for t in turnos_str.split(",") if t.strip() != ""
}


codigo_inscricao = f"{nome[:3].upper()}-{curso[:3].upper()}-{semestre}"


candidato = {
    "nome": nome,
    "idade": idade,
    "curso": curso,
    "semestre": semestre,
    "email": email,
    "conhecimentos": conhecimentos_candidato,
    "turnos": turnos_candidato,
    "trabalha_em_equipe": trabalha_em_equipe,
    "computador_proprio": computador_proprio,
    "codigo_inscricao": codigo_inscricao
}


conhecimentos_compativeis = candidato["conhecimentos"].intersection(
    conhecimentos_exigidos
)
conhecimentos_faltantes = conhecimentos_exigidos.difference(
    candidato["conhecimentos"]
)
qtd_compativeis = len(conhecimentos_compativeis)

turnos_validos = candidato["turnos"].intersection(set(turnos_disponiveis))


email_valido = "@" in candidato["email"] and "." in candidato["email"]


idade_valida = candidato["idade"] >= 16
conhecimentos_suficientes = qtd_compativeis >= 3
turno_valido = len(turnos_validos) > 0
aceita_equipe = candidato["trabalha_em_equipe"]


if turno_valido:
    pontuacao = len(conhecimentos_compativeis) * 2   
    if "manhã" in turnos_validos:
        pontuacao += 1                                
    if "tarde" in turnos_validos:
        pontuacao += 1                               
    if candidato["trabalha_em_equipe"]:
        pontuacao += 2                                
    if candidato["computador_proprio"]:
        pontuacao += 1                               
else:
    pontuacao = 0


aprovado = (
    idade_valida
    and conhecimentos_suficientes
    and turno_valido
    and aceita_equipe
    and pontuacao >= 7
)


if aprovado:
    classificacao = "APROVADO"
elif pontuacao >= 5:
    classificacao = "BANCO DE TALENTOS"
else:
    classificacao = "NÃO APROVADO"


selo_destaque = pontuacao >= 12 and aprovado


motivos = []
if idade_valida == False:
    motivos.append("Idade mínima de 16 anos não atendida.")
if conhecimentos_suficientes == False:
    motivos.append("Menos de 3 conhecimentos compatíveis.")
if turno_valido == False:
    motivos.append(f"Nenhum turno compatível. Opções: {turnos_disponiveis}.")
if aceita_equipe == False:
    motivos.append("Não aceitou trabalhar em equipe.")
if email_valido == False:
    motivos.append("E-mail inválido (precisa conter '@' e '.').")
if pontuacao < 7:
    motivos.append("Pontuação final abaixo do mínimo para aprovação (7 pontos).")


print()
print("=" * 45)
print(" RESULTADO DA SELEÇÃO")
print("=" * 45)
print(f"Código de inscrição: {candidato['codigo_inscricao']}")
print(f"Nome: {candidato['nome']}")
print(f"Idade: {candidato['idade']}")
print(f"Curso: {candidato['curso']} - {candidato['semestre']}º semestre")
print(f"E-mail: {candidato['email']} ({'válido' if email_valido else 'inválido'})")
print(f"Turnos informados: {candidato['turnos']} (compatíveis: {turnos_validos if turnos_validos else 'nenhum'})")
print(f"Conhecimentos compatíveis ({qtd_compativeis}): {conhecimentos_compativeis if conhecimentos_compativeis else 'nenhum'}")
print(f"Conhecimentos faltantes: {conhecimentos_faltantes if conhecimentos_faltantes else 'nenhum'}")
print(f"Aceita trabalho em equipe: {'sim' if candidato['trabalha_em_equipe'] else 'não'}")
print(f"Possui computador próprio: {'sim' if candidato['computador_proprio'] else 'não'}")
print(f"Pontuação final: {pontuacao} pontos")
print("-" * 45)
print(f"Classificação final: {classificacao}")
if selo_destaque:
    print('Selo especial: "Candidato Destaque" ')
if motivos:
    print("\nMotivos que impactaram o resultado:")
    for motivo in motivos:
        print(f"  - {motivo}")
print("=" * 45)
##tempo de ser feito: 1 hora e 29 minutos com os desafios bonus