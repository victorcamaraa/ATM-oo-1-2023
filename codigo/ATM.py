import MenuGerente
import MenuCliente
import pagprogamado

while True:
            print("Menu:")
            print("1. Fazer login")
            print("2. Gerente")
            print("3. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                MenuCliente.fazer_login()
            elif opcao == "2":
                MenuGerente.menu_gerente()
            elif opcao == "3":
                break
            else:
                print("Opção inválida. Tente novamente.")


#verifica se existe algum pagamento progamado para hoje ou se passou a data de algum pagamento progamado
pagprogamado.processar_pagamentos()
