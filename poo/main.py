from cliente import Cliente
from conta import Conta
from banco import Banco
from conta_corrente import ContaCorrente

banco = Banco()

cliente1 = Cliente("Jardel", "123.456.789-00")
cliente2 = Cliente("Maria", "987.654.321-00")

conta1 = Conta(cliente1, 1001)
conta2 = ContaCorrente(cliente2, 1002, 500)

banco.adicionar_conta(conta1)
banco.adicionar_conta(conta2)

conta1.depositar(500)
conta1.sacar(100)

conta2.depositar(1000)

print("\n--- LISTAGEM DE CONTAS ---")
banco.listar_contas()