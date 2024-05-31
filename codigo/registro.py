import  datetime
def registrar_usuario():
    data_atual = datetime.datetime.now()
    data_formatada = data_atual.strftime("%d/%m/%Y")

    id = pega_id()
    saldo = int(0)
    usuario = {
        "id": id,
        "nome": nome(),
        "cpf": cpf(),
        "endereco": endereco(),
        "telefone": telefone(),
        "senha": senha(),
        "saldo": saldo,
    }

    linha = f"{usuario['id']},{usuario['nome']},{usuario['cpf']},{usuario['endereco']},{usuario['telefone']},{usuario['senha']},{data_formatada},{usuario['saldo']}\n"
    with open("Dados.txt", "a") as arquivo:
        arquivo.write(linha)

    print("Usuário registrado com sucesso!")
    print('ID do usuario:', id)

def nome():
    nome = input("Digite o nome: ")
    nome = nome.strip()
    nome = nome.title()
    return nome

def pega_id():
    linha = 0
    with open("Dados.txt", "r") as dados:
        for i in dados:
            linha = linha + 1
        return linha + 1
def endereco():
    endereco = input("Digite o endereço: ")
    return endereco



def validar_cpf(cpf):
    # Removendo caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verificando o tamanho do CPF
    if len(cpf) != 11:
        return False

    # Verificando se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False

    # Calculando o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0

    # Calculando o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0

    # Verificando se os dígitos verificadores são iguais aos do CPF
    if digito1 == int(cpf[9]) and digito2 == int(cpf[10]):

        return True
    else:
        return False


def validar_cnpj(cnpj):
    # Removendo caracteres não numéricos do CNPJ
    cnpj = ''.join(filter(str.isdigit, cnpj))

    # Verificando o tamanho do CNPJ
    if len(cnpj) != 14:
        return False

    # Calculando o primeiro dígito verificador
    soma = sum(int(cnpj[i]) * (5 - i if i < 4 else 13 - i) for i in range(12))
    digito1 = (soma % 11)
    digito1 = 0 if digito1 < 2 else 11 - digito1

    # Calculando o segundo dígito verificador
    soma = sum(int(cnpj[i]) * (6 - i if i < 5 else 14 - i) for i in range(13))
    digito2 = (soma % 11)
    digito2 = 0 if digito2 < 2 else 11 - digito2

    # Verificando se os dígitos verificadores são iguais aos do CNPJ
    if digito1 == int(cnpj[12]) and digito2 == int(cnpj[13]):
        return True
    else:
        return False


def cpf():
    while True:

        cpf = input('Digite o cpf/cnpj (somente digitos): ')
        if validar_cpf(cpf) or validar_cnpj(cpf):
            if len(cpf) == 11:
                cpf = cpf[0:3]+'.'+cpf[3:6]+'.'+cpf[6:9]+'-'+cpf[9:]
                return cpf
            elif len(cpf) == 14:
                cpf = cpf[0:2] + '.'+cpf[2:5]+'.'+cpf[5:8]+'/'+cpf[8:12]+'-'+cpf[12:]
                return cpf
        else:
            print('CPF/CNPJ invalido')

def telefone():
    while True:
        tel = input('digite o telefone: ')
        if tel.isdigit() and len(tel) == 11:
            fone = tel[0:2] + '-'+ tel[2:7]+'-'+tel[7:]
            return fone
        else:
            print('Formato invalido, digite o telefone com o ddd e somente digitos numericos\n ex: 11940028922')




def senha():
    while True:
        senha = input("Digite a senha de até 6 dígitos numéricos: ")
        if senha.isdigit() and len(senha) == 6:
            return senha
        else:
            print("A SENHA DEVE CONTER 6 DIGITOS NUMERICOS. Tente novamente.")
#registrar_usuario()