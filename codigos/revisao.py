numero_lado = int(input("Digite o numero de lados: "))
tamanho_lado = float(input("Digite o tamanho do lado (pode ser decimal): "))

if numero_lado == 3:
    tipo_triangulo = int(input("Quantos lados sao iguais? "))

    if tipo_triangulo == 3:
        print("Equilatero")
    elif tipo_triangulo == 2:
        print("Isosceles")
    else:
        print("Escaleno")

elif numero_lado == 4:
    lado_iguais = int(input("Quantos lados iguais tem seu quadrilatero? "))

    if lado_iguais == 4:
        print("Sua forma e um quadrado")
    elif lado_iguais == 2:
        print("Sua forma e um retangulo")
    else:
        print("Forma nao reconhecida")

else:
    print("Forma nao reconhecida")