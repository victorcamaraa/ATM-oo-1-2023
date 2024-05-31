def deletar_usuario(id_usuario):
    with open("Dados.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    # Verificar se o usuário existe e se o saldo é igual a 0
    usuario_encontrado = False
    for i in range(len(linhas)):
        dados = linhas[i].strip().split(',')
        if int(dados[0]) == id_usuario:
            saldo = float(dados[-1])
            usuario_encontrado = True
            if saldo == 0:
                linhas[i] = dados[0] + ",Deletado\n"
            else:
                print("Não é possível deletar o usuário. Saldo não é igual a 0.")
            break

    # Verificar se o usuário foi encontrado
    if not usuario_encontrado:
        print("Usuário não encontrado.")
        return

    with open("Dados.txt", "w") as arquivo:
        arquivo.writelines(linhas)
    if saldo == 0:
        print("Usuário deletado com sucesso.")

