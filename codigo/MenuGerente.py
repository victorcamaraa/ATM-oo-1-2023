import registro
import busca
import modifica
import deleta
import historico
import solicitar

def menu_gerente():
    senha_gerente = input("Digite a senha do gerente: ")

    if senha_gerente == "123456":
        while True:
            print("\nMenu do Gerente:")
            print("1. Registrar novo usuário")
            print('2. Buscar/modificar dados de usuario')
            print("3. Apagar usuário")
            print("4. Solicitações de credito")
            print('5. Voltar')

            opcao_gerente = input("Escolha uma opção: ")

            if opcao_gerente == "1":
                registro.registrar_usuario()
            elif opcao_gerente == "2":
                id_usuario = int(input('Digite o ID de quem deseja buscar'))
                if busca.existe(id_usuario) and busca.nome(id_usuario) != 'Deletado' :
                    print('-------------------------------------\n')
                    busca.busca(id_usuario)
                    print('-------------------------------------\n')
                    opcao_busca = (input('[1] alterar dados [2] imprimir historico [3] Voltar'))
                else:
                    print('Usuario não encontrado')
                    return

                if opcao_busca == '1':
                    campo = int(input("Digite o campo a ser alterado \n1. nome\n2. cpf\n3. endereco\n4. telefone\n5. senha\n6. saldo\n"))
                    modifica.modificar(id_usuario,campo)

                elif opcao_busca == '2':
                    historico.mostrar_historico(id_usuario)

                elif opcao_busca == '3':
                    break


            elif opcao_gerente == "3":
                id_usuario = int(input('digite o ID de quem deseja deletar: '))
                print('-------------------------------------\n')
                busca.busca(id_usuario)
                print('-------------------------------------\n')

                opcao_busca = int(input('[1] deletar [2] voltar'))

                if opcao_busca == 1:
                    deleta.deletar_usuario(id_usuario)
                else:
                    pass

            elif opcao_gerente == '4':
                solicitar.gerente_solicitar()


            elif opcao_gerente == "5":
                return
            else:
                print("Opção inválida. Tente novamente.")
    else:
        print("Senha invalida")

