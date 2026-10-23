print("SISTEMA DE LOGIN")

email_correto = "luizjardel@gmail.com"
senha_correta = "1234"

while True:
    email = input("Digite seu email:")
    senha = input("Digite sua senha:")

    if email == email_correto and senha == senha_correta:
        print("Login realizado")
        break
    else:
        print("Email ou senha incorretos,tente novamente")

    ## GGWP




