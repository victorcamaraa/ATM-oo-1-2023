import datetime


def registrar_transacao(id_usuario, tipo_transacao, valor, saldo):
    data_atual = datetime.datetime.now()
    data_formatada = data_atual.strftime("%d/%m/%Y %H:%M:%S")
    with open("historico.txt", "a") as arquivo:
        linha = f"{id_usuario},{tipo_transacao},{valor},{data_formatada},{saldo}\n"
        arquivo.write(linha)

def mostrar_historico(id_usuario):
    with open("historico.txt", "r") as arquivo:
        tem = 0
        for linha in arquivo:
            dados = linha.strip().split(",")

            if int(dados[0]) == id_usuario:
                tipo_transacao = dados[1]
                valor = float(dados[2])
                data_hora = dados[3]
                saldo = dados[-1]
                print("\n-------------------")
                print(f"Tipo de transação: {tipo_transacao}")
                print(f"Valor: {valor}")
                print(f"Saldo após a operação: {saldo}")
                print(f"Data e hora: {data_hora}")
                print("---")
                tem = 1

        if tem == 0:
            print('\n---Histórico vazio---')

