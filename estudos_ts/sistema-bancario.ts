let saldo: number = 1000;

function sacar(valor: number): number {
    if (valor <= 0) {
        throw new Error("Valor de Saque Inválido");
    }

    if(valor >saldo){
        throw new Error("Saldo insuficiente!");
    }
    //amanha termino
}