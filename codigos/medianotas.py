print("====Media de Notas====")
def calcular_media(notas):
    media = sum(notas) /len(notas)
    return media
    def classificar_media(media,frequencia):
        if frequencia < 75:
            return "Reprovado por Falta"
            elif media >= 7:
                return "Aprovado"
                elif media >= 5:
                    return "Recuperação"
                    else:
                        return "Reprovado por notas"
                        def demais_casos(Reprovado)
