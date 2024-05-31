import  datetime
import busca
import modifica
import historico
def cliente_solicitar(id_usuario):
        with open("Dados.txt", "r") as arquivo:
            linhas = arquivo.readlines()

            for linha in linhas:
                usuario = linha.strip().split(",")
                if int(usuario[0]) == id_usuario:
                    if len(usuario[2]) == 18:

                        pedido = float(input('quanto deseja solicitar?'))
                        prazo = int(input('Em quantos meses pretende pagar?'))
                        parcela = (pedido * 1.01**prazo / prazo)
                        situacao = 0
                        hoje = datetime.datetime.now()
                        data = hoje.strftime("%d/%m/%Y %H:%M:%S")

                        print('\n\n_______________')
                        print('o valor será pago em '+str(prazo)+' parcelas de {:.2f} \n(juros a 1% A.M.)'.format(parcela))
                        r = input('Confirmar? [1] SIM [2] NAO')

                        print('_______________\n\n')
                        if r == '1':
                            escreve = f'{id()},{id_usuario},{pedido},{parcela:.2f},{prazo},{situacao},{data}\n'
                            print('solicitação feita com sucesso, aguardando confirmação do gerente')
                            with open("Solicitações.txt", "a") as arquivo:
                                arquivo.write(escreve)

                        else:
                            return

                    elif len(usuario[2]) == 14:

                        pedido = float(input('quanto deseja solicitar?'))
                        prazo = int(input('Em quantos meses pretende pagar?'))
                        parcela = (pedido * 1.015**prazo / prazo)
                        situacao = 0
                        hoje = datetime.datetime.now()
                        data = hoje.strftime("%d/%m/%Y %H:%M:%S")

                        print('\n\n_______________')
                        print('o valor será pago em '+str(prazo)+' parcelas de {:.2f} \n(juros a 1,5% A.M.)'.format(parcela))
                        r = input('Confirmar? [1] SIM [2] NAO')

                        print('_______________\n\n')
                        if r == '1':
                            escreve = f'{id()},{id_usuario},{pedido},{parcela:.2f},{prazo},{situacao},{data}\n'
                            print('solicitação feita com sucesso, aguardando confirmação do gerente')
                            with open("Solicitações.txt", "a") as arquivo:
                                arquivo.write(escreve)

                        else:
                            return
def gerente_solicitar():
    with open("Solicitações.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        print('Solicitações de:')
        tem = 0
        for linha in linhas:
            usuario = linha.strip().split(",")
            if len(usuario) >= 6 and usuario[5] == '0':
                if len(busca.cpf(int(usuario[1]))) == 18:
                    tipo = 'empresa'
                elif len(busca.cpf(int(usuario[1]))) == 14:
                    tipo = 'pessoa fisica'

                tem = 1
                print('--------------------------')
                print(tipo)
                print(f'Nome do solicitante: {busca.nome(int(usuario[1]))}')
                print(f'ID da solicitação: {usuario[0]}')
                print(f'Data da solicitação: {usuario[6]}')
                print('--------------------------')
        if tem == 0:
            print('----------------------')
            print('Não há solicitações')
            print('----------------------')
            return

        id = int(input('Digite o ID da solicitação ou 0 para voltar: '))

    with open("Solicitações.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            usuario = linha.strip().split(",")
            if len(usuario) >= 6 and int(usuario[0]) == id and usuario[5] == '0':
                print(f'\nNome do solicitante: {busca.nome(int(usuario[1]))}')
                print('tipo: '+tipo)
                print(f'Valor solicitado: R${usuario[2]}')
                print(f'Em {usuario[4]} prestações mensais de R${usuario[3]}, totalizando com juros R$ {float(usuario[3]) * float(usuario[4]):.2f}')
                if tipo == 'empresa':
                    print('(juros a 1% ao mês)')
                else:
                    print('(juros de 1,5% ao mês)')
                aprova = input('\n[1] Aprovar | [2] Recusar: ')

                if aprova == '1':
                    modifica.saldonovo(int(usuario[1]), float(usuario[2]))
                    modifica.att_solicitação(id, aprova)
                    print('----------------------')
                    print('Pedido aprovado')
                    print('----------------------')

                    historico.registrar_transacao(usuario[1], 'Crédito do banco', usuario[2], busca.saldo(int(usuario[1])))
                elif aprova == '2':
                    modifica.att_solicitação(id, aprova)
                    print('----------------------')
                    print('Pedido recusado')
                    print('----------------------')

        if id == 0:
            return



def id():
    linha = 0
    with open("Solicitações.txt", "r") as dados:
        for i in dados:
            linha = linha + 1
        return linha + 1
#cliente_solicitar(2)
#gerente_solicitar()
