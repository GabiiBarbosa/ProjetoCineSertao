
def validar_campo(texto):
    campo = input(texto)
    while len(campo) == 0:
        campo = input(texto)
    return campo

def cadastrar_user(usuarios):
    print('--------------------------------------')
    print('            CADASTRAMENTO             ')
    print('--------------------------------------')
    user = input('Digite seu nome de usuário: ')
    if user in usuarios:
        print('\nCadastro já existente!')
        return False

    email = validar_campo('Digite seu email: ')
    senha = validar_campo('Digite sua senha: ')
    perfil = ''
    while perfil != '1' and perfil != '2':
        perfil = validar_campo('Digite [1] para cadastrar-se Administrador ou [2] para cadastrar-se Cliente: ')
        if perfil != '1' and perfil != '2':
            print('Opção inválida. Por favor, insira 1 para Administrador ou 2 para Cliente.\n')
    usuarios[user] = [email, senha, perfil]
    print('\nCadastro realizado com sucesso!')

def login_usuario(usuarios, user, email, senha):
    return user in usuarios and usuarios[user][0] == email and usuarios[user][1] == senha
