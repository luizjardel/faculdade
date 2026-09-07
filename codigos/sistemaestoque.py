# Tarefa Faculdade de Python dia 03/09/2026
# Sistema Inteligente de Estoque
estoque = {
    "Arroz": 20,
    "Feijão": 15,
    "Macarrão": 12,
    "Café": 8,
    "Açúcar": 10
}

print("=== Sistema Inteligente de Estoque ===")

print("Quantidade de produtos cadastrados no estoque:", len(estoque))#len para Contar a quantiaade de produtos

produto = input("Digite o nome do Produto: ")

if produto in estoque: ##verificando se o produto está no estoque

    print(f"Produto: {produto} - Quantidade em estoque: {estoque[produto]}")

    resposta = input("Deseja atualizar a quantidade? (S/N): ")

    if resposta.upper() == "S":

        nova_quantidade = int(input("Digite a nova quantidade: "))

        estoque[produto] = nova_quantidade

        print(f"Quantidade do produto {produto} atualizada com sucesso!")

else:

    print(f"Produto: {produto} não encontrado no estoque.")

    resposta = input("Deseja cadastrar o produto? (S/N): ")

    if resposta.upper() == "S":

        quantidade = int(input("Digite a quantidade do novo produto: "))

        estoque[produto] = quantidade

        print(f"Produto: {produto} cadastrado com sucesso!")




print("\nProdutos Cadastrados")
print(estoque.keys())

print("\nQuantidade de Produtos Registrados")
print(estoque.values())

print("\nLog dos Estoques Registrados")

for produto, quantidade in estoque.items():
    print(produto, "->", quantidade, "unidades")



##função para calcular as unidades do sistema de estoque
total_estoque = sum(estoque.values())

print("\nTotal de unidades no estoque:", total_estoque)


maior_quantidade = 0
produto_maior = ""

for produto, quantidade in estoque.items():#verificando qual produto tem mais quantidade 

    if quantidade > maior_quantidade:

        maior_quantidade = quantidade
        produto_maior = produto

print("\nProduto com maior quantidade:", produto_maior)
print("Quantidade:", maior_quantidade)


produto_remover = input("\nDigite o nome do Produto que deseja remover: ")

if produto_remover in estoque:

    del estoque[produto_remover]

    print(f"Produto: {produto_remover} removido do estoque.")

else:

    print("Produto não encontrado")


print("\nSistema do Estoque Atualizado")
print(estoque.keys())

print("\nNova quantidade de Produtos do Sistema:", len(estoque))
##Tempo de conclusão do desafio 1 hora e 40 minutos