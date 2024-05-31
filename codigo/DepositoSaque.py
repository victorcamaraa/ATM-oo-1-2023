import historico
def sacar_saldo(id_usuario):
    valor_saque = 0
    while valor_saque <= 0:
        valor_saque = input("Digite o valor a ser sacado: ")
        if not valor_saque.isdigit() or float(valor_saque) == 0:
            valor_saque = 0
            print("Valor inválido")
            continue

        valor_saque = float(valor_saque)
        with open("Dados.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        for i, linha in enumerate(linhas):
            dados = linha.strip().split(",")
            id_arquivo = int(dados[0])
            if id_arquivo == id_usuario:
                saldo = float(dados[-1])
                if saldo >= valor_saque:
                    saldo -= valor_saque
                    linhas[i] = linha.rstrip()[:-len(dados[-1])] + str(saldo) + "\n"
                    historico.registrar_transacao(id_usuario, "Saque", valor_saque, saldo)
                    print("Saque realizado com sucesso!")
                    print("Novo saldo = R$", saldo)
                else:
                    print("Saldo insuficiente para o saque. Saldo atual = R$", saldo)

        with open("Dados.txt", "w") as arquivo:
            arquivo.writelines(linhas)

import historico

def depositar_saldo(id_usuario):
    valor_deposito = 0
    while valor_deposito <= 0:
        valor_deposito = input("Digite o valor a ser depositado: ")
        if not valor_deposito.isdigit() or float(valor_deposito) == 0:
            valor_deposito = 0
            print("Valor inválido")
            continue

        valor_deposito = float(valor_deposito)
        with open("Dados.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        for i, linha in enumerate(linhas):
            dados = linha.strip().split(",")
            id_arquivo = int(dados[0])
            if id_arquivo == id_usuario:
                saldo = float(dados[7])
                saldo += valor_deposito
                linhas[i] = linha.rstrip()[:-len(dados[7])] + str(saldo) + "\n"
                historico.registrar_transacao(id_usuario, "Deposito", valor_deposito, saldo)
                print("Depósito realizado com sucesso.")
                print("Novo saldo é de: R$", saldo)

        with open("Dados.txt", "w") as arquivo:
            arquivo.writelines(linhas)
