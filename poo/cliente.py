class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")