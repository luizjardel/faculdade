
quantidade_operacoes = int(input())
saldo = 0
saldo_insuficiente = False

for _ in range(quantidade_operacoes):
    operacao = int(input())

    if operacao == 0:
        continue

    saldo += operacao

    if saldo < 0:
        saldo_insuficiente = True
        break

if saldo_insuficiente:
    print("saldo insuficiente")
else:
    print(f"saldo {saldo}")
