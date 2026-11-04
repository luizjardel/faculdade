class Banco:
    def __init__(self):
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)
        print("Conta adicionada!")

    def listar_contas(self):
        for conta in self.contas:
            print(f"Conta: {conta.numero}")
            print(f"Titular: {conta.titular.nome}")
            print(f"Saldo: R$ {conta.saldo:.2f}")