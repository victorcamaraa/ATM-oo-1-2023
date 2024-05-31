import DepositoSaque
import historico
import pagprogamado
import solicitar

def fazer_login():
    login = 0
    id_usuario = int(input("Digite o ID do usuário: "))
    senha = input("Digite a senha: ")

    with open("Dados.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    for linha in linhas:
        dados = linha.strip().split(",")
        id_arquivo = int(dados[0])
        senha_arquivo = dados[-3]
        if id_arquivo == id_usuario and senha_arquivo == senha:
                login = 1
                print("Login realizado com sucesso!\n---Bem vindo---\n"+ dados[1]+'\nId: '+dados[0])
                print('saldo dispinivel = R$ '+ dados[-1])
                print('---------------------------')
                while True:

                    print('1. realizar saque')
                    print('2. realizar deposito')
                    print('3. realizar pagamento progamado')
                    print('4. verificar historico')
                    print('5. solicitar credito')
                    print('6. Sair')

                    opcao_cliente = (input('Escolha uma opção'))

                    if opcao_cliente == '1':
                        DepositoSaque.sacar_saldo(id_usuario)
                        print('---------------------------')

                    elif opcao_cliente == '2':
                        DepositoSaque.depositar_saldo(id_usuario)
                        print('---------------------------')

                    elif opcao_cliente == '3':
                        pagprogamado.pagar(id_usuario)

                    elif opcao_cliente == '4':
                        historico.mostrar_historico(id_usuario)
                        print('---------------------------')

                    elif opcao_cliente == '5':
                        solicitar.cliente_solicitar(id_usuario)

                    elif opcao_cliente == '6':
                        break





    if login == 0:
        print('Login ou senha invalido')