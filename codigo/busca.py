def busca(id_usuario):
    with open("Dados.txt", "r") as arquivo:
        linhas = arquivo.readlines()

        for linha in linhas:
            usuario = linha.strip().split(",")
            if int(usuario[0]) == id_usuario:
                if usuario[1] == 'Deletado':
                    print('Usuario de ID: '+ usuario[0] + ' Foi deletado')
                    break
                else:
                    print("ID:", usuario[0])
                    print("Nome:", usuario[1])

                    if len(usuario[2]) == 18:
                        print('Tipo: Empresa')
                        print("CNPJ:", usuario[2])

                    if len(usuario[2]) == 14:
                        print('tipo: Pessoa Fisica')
                        print("CPF:", usuario[2])

                    print("Endereço:", usuario[3])
                    print("Telefone:", usuario[4])
                    print("Senha:", usuario[5])
                    print("Conta criada em", usuario[6])
                    print("Saldo: R$", usuario[-1])
                    break
        else:
            print("Usuário não encontrado.\n")

def nome(id_receptor):
    with open("Dados.txt", "r") as arquivo:
        linhas = arquivo.readlines()

        for linha in linhas:
            usuario = linha.strip().split(",")
            if int(usuario[0]) == id_receptor:
                if usuario[1] == 'Deletado':
                    print('Usuario de ID: '+ usuario[0] + ' Foi deletado')
                    break
                else:
                    return usuario[1]

def cpf(id_receptor):
    with open("Dados.txt", "r") as arquivo:
        linhas = arquivo.readlines()

        for linha in linhas:
            usuario = linha.strip().split(",")
            if int(usuario[0]) == id_receptor:
                    return usuario[2]



def saldo(id_receptor):
    with open("Dados.txt", "r") as arquivo:
        linhas = arquivo.readlines()

        for linha in linhas:
            usuario = linha.strip().split(",")
            if int(usuario[0]) == id_receptor:
                if usuario[1] == 'Deletado':
                    print('Usuario de ID: '+ usuario[0] + ' Foi deletado')
                    break
                else:
                    return usuario[-1]


def existe(id_receptor):
    with open("dados.txt", "r") as arquivo:
        for linha in arquivo:
            usuario = linha.strip()
            if usuario.startswith(str(id_receptor)):
                return True
    return False


