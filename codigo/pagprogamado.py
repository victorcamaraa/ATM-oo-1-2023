import datetime
from datetime import datetime, timedelta,date
import busca
import modifica
import historico

# Função para realizar o pagamento programado
def registro(id_usuario, id_receptor, data_programada, data_recebimento, valor):
    with open("programados.txt", "a") as arquivo:
        arquivo.write(f"{id_usuario},{id_receptor},{data_programada},{data_recebimento},{valor}\n")

import datetime

import datetime

def obter_data_valida():
    while True:
        data_str = input('Digite a data no formato DD/MM/AAAA: ')
        try:
            dia, mes, ano = map(int, data_str.split('/'))
            data = datetime.date(ano, mes, dia)
            data_atual = datetime.date.today()
            if data < data_atual:
                print('A data deve ser igual ou posterior à data atual.')
            else:
                return data
        except ValueError:
            print('Data inválida. Certifique-se de digitar no formato correto (DD/MM/AAAA).')

def pagar(id_usuario):
    id_receptor = int(input('Digite o ID do usuário que deseja pagar ou 0 para voltar: '))
    if id_receptor == id_usuario:
        print('Não é possível programar um pagamento para si mesmo.')
        return
    if not busca.existe(id_receptor):
        print('Usuário não encontrado.')
        return
    else:
        while True:
            print('Usuário selecionado: ' + busca.nome(id_receptor))
            valor = int(input('\nDigite a quantia que deseja pagar ou 0 para voltar: '))
            if valor == 0:
                return
            data_recebimento = obter_data_valida()
            data_programada = datetime.date.today().strftime("%d/%m/%Y")
            registro(id_usuario, id_receptor, data_programada, data_recebimento, valor)
            print('\n----- Pagamento agendado com sucesso -----\n')
            break


def somar_meses(data, num_meses):
    data_resultante = data + datetime.timedelta(days=num_meses * 30)
    return data_resultante

def criar_parcelas(id_usuario,prazo,parcela):
    feito = 0
    for i in range(prazo):
        hoje = datetime.datetime.now()
        data_programada = hoje.strftime("%d/%m/%Y")
        data_recebimento = somar_meses(hoje,feito).strftime("%d/%m/%Y")
        registro(id_usuario, 0, data_programada, data_recebimento, parcela)
        feito = feito + 1





# Função para realizar pagamentos programados
def converter_data_para_int(data):
    data_formatada = datetime.strptime(data, "%d/%m/%Y")
    data_referencia = datetime(2000, 1, 1)
    diferenca = (data_formatada - data_referencia).days
    return diferenca


def converter_data_para_int(data):
    data_formatada = datetime.datetime.strptime(data, "%Y-%m-%d")
    data_referencia = datetime.datetime(2023, 6, 14)
    diferenca = (data_formatada - data_referencia).days
    return diferenca

def processar_pagamentos():
    with open("programados.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    for linha in linhas:
        dados = linha.strip().split(",")
        id_pagador = int(dados[0])
        id_receptor = int(dados[1])
        data_pagamento = dados[3]
        valor = float(dados[-1])
        data_atual_int = converter_data_para_int(datetime.date.today().strftime("%Y-%m-%d"))

        data_pagamento_int = converter_data_para_int(data_pagamento)

        if data_pagamento_int <= data_atual_int:
            pagou = float( 0 - valor)
            modifica.saldonovo(id_pagador, pagou)
            modifica.saldonovo(id_receptor, valor)
            #print(f"Pagamento processado: ID Pagador: {id_pagador}, ID Receptor: {id_receptor}, Valor: {valor}")
            saldo_pagador = busca.saldo(id_pagador)
            saldo_receptor = busca.saldo(id_receptor)
            historico.registrar_transacao(id_pagador,'pagamento progamado',pagou,saldo_pagador)
            historico.registrar_transacao(id_receptor, 'pagamento progamado', valor, saldo_receptor)

    # Apagar as linhas do arquivo programados.txt correspondentes aos pagamentos processados
    with open("programados.txt", "w") as arquivo:
        for linha in linhas:
            dados = linha.strip().split(",")
            data_pagamento = dados[3]
            data_pagamento_int = converter_data_para_int(data_pagamento)
            if data_pagamento_int > data_atual_int:
                arquivo.write(linha)





#relaizar o pagamento e atualiar o saldo
def atualizar_saldo(id_usuario, novo_saldo):
    with open("Dados.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    # Lista para armazenar as linhas atualizadas
    linhas_atualizadas = []

    for linha in linhas:
        usuario = linha.strip().split(",")
        if int(usuario[0]) == id_usuario:
                # Atualiza o saldo do usuário
                usuario[6] = str(novo_saldo)

        # Adiciona a linha atualizada à lista
        linhas_atualizadas.append(','.join(usuario))

    # Escreve as linhas atualizadas no arquivo
    with open("Dados.txt", "w") as arquivo:
        arquivo.writelines(linhas_atualizadas)

#criar_parcelas(1,12,30)
#pagar(2)
