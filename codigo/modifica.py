import registro

def modificar(id_usuario, campo):

    with open("Dados.txt", "r") as arquivo:
        linhas = arquivo.readlines()


    for i in range(len(linhas)):
        usuario = linhas[i].strip().split(',')
        if int(usuario[0]) == id_usuario:

            if campo == 1: #nome
                usuario[1] = registro.nome()
            elif campo == 2: #cpf
                usuario[2] = registro.cpf()
            elif campo == 3: #endereco
                usuario[3] = input('Novo endereço:\n')
            elif campo == 4: #telefone
                usuario[4] = registro.telefone()
            elif campo == 5:#senha
                usuario[5] = registro.senha()
            elif campo == 6:#saldo
                usuario[6] = modsaldo()

            # Atualizar a linha do usuário no arquivo
            linhas[i] = ','.join(usuario) + '\n'
            print('Alterado com sucesso\n')
            break

    # Salvar as alterações no arquivo
    with open("Dados.txt", "w") as arquivo:
        arquivo.writelines(linhas)

def modsaldo():
        while True:
            saldo = input("Digite o novo saldo: ")
            if saldo.isdigit():
                return saldo
            else:
                print('somente valores numericos inteiros')

def saldonovo(id_usuario, credito):
    with open("Dados.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    for i in range(len(linhas)):
        usuario = linhas[i].strip().split(',')
        if int(usuario[0]) == id_usuario:
            usuario[7] = str(float(usuario[7]) + float(credito))

        linhas[i] = ','.join(usuario) + '\n'

    with open("Dados.txt", "w") as arquivo:
        arquivo.writelines(linhas)

def att_solicitação(id_solicitacao, aprova):
    with open("Solicitações.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    for i in range(len(linhas)):
        soli = linhas[i].strip().split(',')
        if soli and soli[0] and int(soli[0]) == id_solicitacao:
            if aprova == '1':
                soli[-2] = '1'
            elif aprova == '2':
                soli[-2] = '2'

            else:
                print('Inválido')

            linhas[i] = ','.join(soli) + '\n'

    with open("Solicitações.txt", "w") as arquivo:
        arquivo.writelines(linhas)




