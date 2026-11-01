##Calculadora Feita para Treinar Logica de Programação ,feito na aula de UML

print("----Calculadora Simples ----")

print(f"Digite o primeiro número:")
num1 =  float(input())

print(f"Digite o segundo número:")
num2 = float(input())

print(f"Escolha a operação desejada:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
opcao = int(input("Digite sua Escolha:"))

if opcao == 1:
    resultado = num1 + num2
    print(f"O Resultado da Adição é: {resultado}")

elif opcao == 2:
    resultado = num1 - num2
    print(f"O Resultado da Subtração é: {resultado}")

elif opcao == 3:
    resultado = num1 * num2
    print(f"O Resultado da Multiplicação é: {resultado}")

elif opcao == 4:
    if num2 != 0:
        resultado = num1 / num2
        print(f"O Resultado da Divisão é: { resultado}")

    else:
        print("Não é possivel dividir por 0")



