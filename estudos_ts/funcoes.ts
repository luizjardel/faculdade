function calcularIdade(anoNascimento: number): number {
    return 2026 - anoNascimento;
}

const idade = calcularIdade(2006);

console.log("Sua idade é:", idade);