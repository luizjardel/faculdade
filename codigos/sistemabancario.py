import streamlit as st
if "ContaBancaria" not in st.session_state:
    st.session_state.ContaBancaria = {
        "numero_conta": 0,
        "titular": "",
        "saldo": 0.0,
    }

if "conta_criada" not in st.session_state:
    st.session_state.conta_criada = False

ContaBancaria = st.session_state.ContaBancaria

st.title("🏦 Bem Vindo ao Sistema Bancário")

if not st.session_state.conta_criada:
    Criar_conta = st.text_input("Deseja criar uma conta bancária? (Sim/Não): ")

    if Criar_conta.lower() == "sim":
        ContaBancaria["numero_conta"] = st.text_input("Digite o número da conta: ")
        ContaBancaria["titular"] = st.text_input("Digite o nome do titular: ")
        ContaBancaria["saldo"] = st.number_input("Digite o saldo inicial: ", step=0.01)

        if st.button("Confirmar criação da conta"):
            st.session_state.conta_criada = True
            st.rerun()

else:
    st.write("Conta criada com sucesso!")
    st.write("Número da conta:", ContaBancaria["numero_conta"])
    st.write("Titular:", ContaBancaria["titular"])
    st.write("Saldo atual:", ContaBancaria["saldo"])

    st.write("=== Operações Bancárias ===")
    opcao = st.selectbox(
        "Escolha uma opção:",
        ("1. Consultar saldo", "2. Depositar", "3. Sacar", "4. Sair"),
        key="opcao_operacao",  
    )

    if opcao == "1. Consultar saldo":
        st.write("Saldo atual:", ContaBancaria["saldo"])

    elif opcao == "2. Depositar":
        valor_deposito = st.number_input(
            "Digite o valor a ser depositado: ", step=0.01, key="valor_deposito"
        )
        
        if st.button("Confirmar depósito"):
            ContaBancaria["saldo"] += valor_deposito
            st.success("Depósito realizado com sucesso!")
            st.write("Novo saldo:", ContaBancaria["saldo"])

    elif opcao == "3. Sacar":
        valor_saque = st.number_input(
            "Digite o valor a ser sacado: ", step=0.01, key="valor_saque"
        )
        if st.button("Confirmar saque"):
            if valor_saque <= ContaBancaria["saldo"]:
                ContaBancaria["saldo"] -= valor_saque
                st.success("Saque realizado com sucesso!")
                st.write("Novo saldo:", ContaBancaria["saldo"])
            else:
                st.error("Saldo insuficiente para realizar o saque.")

    elif opcao == "4. Sair":
        st.write("Saindo do sistema bancário.")
        if st.button("Encerrar conta"):
            st.session_state.conta_criada = False
            st.session_state.ContaBancaria = {
                "numero_conta": 0,
                "titular": "",
                "saldo": 0.0,
            }
            st.rerun()

# Sistema Bancario em Python com base na Documentação do Python, atividade
# que fiz com meu amigo, cada um fez sua parte de uma maneira diferente
# Biblioteca utilizada : StreamLit
# para baixar a biblioteca, utilize o comando: pip install streamlit
# Para rodar o código, siga está ordem no terminal: cd codigos, streamlit run sistemabancaro.py