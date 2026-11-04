class Conta:
    def __init__(self, titular, numero):
        self.titular = titular
        self.numero = numero
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        print("Depósito realizado!")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("Saque realizado!")
        else:
            print("Saldo insuficiente!")

    def consultar_saldo(self):
        print(f"Saldo: R$ {self.saldo:.2f}")