
print("=== CAIXA EXPRESSO ===")

produto = {
    "agua": 4.00,
    "suco": 7.00,
    "sanduiche": 12.00,
    " salada" : 15.00,
    "cafe" : 5
    }

total_bruto = 0
pedidos_validos = 0
pedidos_invalidos = 0
numero_tentativas = 4

for i in produto:
    print(f"{i}: R$ {produto[i]:.2f}")
    

    
for i in range(numero_tentativas):
    nome_produto = input("Digite o nome do produto: ")
    if nome_produto in produto:
        quantidade = int(input("Digite a quantidade: "))
        subtotal = produto[nome_produto] * quantidade
        total_bruto += subtotal
        pedidos_validos += 1
    else:
            print("Produto inválido.")
            pedidos_invalidos += 1

print(f"Total bruto: R$ {total_bruto:.2f}")
print(f"Pedidos válidos: {pedidos_validos}")
print(f"Pedidos inválidos: {pedidos_invalidos}")

desconto = 0
if total_bruto >= 50:
    desconto = total_bruto * 0.10
    
total_bruto = total_bruto - desconto
print(f"Total final: R$ {total_bruto:.2f}")

