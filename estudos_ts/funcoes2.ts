
function somar(numero1: number, numero2: number): number {
    return numero1 + numero2;
}

function subtrair(numero1: number, numero2: number): number {
    return numero1 - numero2;
}

function multiplicacao(numero1: number, numero2: number): number {
    return numero1 * numero2;
}

function dividir(numero1: number, numero2: number): number {
    if (numero2 === 0) {
        throw new Error("Impossível dividir por zero!");
    } else {
        return numero1 / numero2;
    }
}
const resultadoSoma = somar(10, 20);
const resultadoSubtracao = subtrair(20, 10);
const resultadoMultiplicacao = multiplicacao(10, 20);
const resultadoDivisao = dividir(10, 20);


console.log("Soma:", resultadoSoma);
console.log("Subtração:", resultadoSubtracao);
console.log("Multiplicação:", resultadoMultiplicacao);
console.log("Divisão:", resultadoDivisao);
