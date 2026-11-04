from conta import Conta


class ContaCorrente(Conta):
    def __init__(self, titular, numero, limite):
        super().__init__(titular, numero)
        self.limite = limite