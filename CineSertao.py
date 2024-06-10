# Dupla: Gabrielle e Jordanna
# Dicionários e listas iniciais
import filmes
import ingressos
import menus
import rendimentos
import validacoes
usuarios = {}
dicioFilmes = {}
filmesExcluidos = []
loginCliente = []

print('Seja bem-vindo(a) ao CINE Sertão!')
while True:
    menus.menu_principal()
    valor = validacoes.validar_campo('\nDigite a opção desejada: ')

    if valor == '1':
        print('--------------------------------------')
        print('Faça login para continuar.\n')
        loginNome = validacoes.validar_campo('Insira seu usuário: ')
        email = validacoes.validar_campo('Insira seu email: ')
        senha = validacoes.validar_campo('Insira sua senha: ')

        if validacoes.login_usuario(usuarios, loginNome, email, senha) and usuarios[loginNome][2] == '1':
            print('\nLogin concluído.')

            while True:
                menus.menu_adm()
                op = input('\nDigite a opção desejada: ')
                if op == '0':
                    break

                elif op == '1':
                    print('--------------------------------------')
                    filmes.cadastrar_filme(dicioFilmes)

                elif op == '2':
                    print('--------------------------------------')
                    filmes.buscar_filmes(dicioFilmes)

                elif op == '3':
                    print('--------------------------------------')
                    filmes.buscar_filmes(dicioFilmes)
                    filmes.atualizar_filme(dicioFilmes)

                elif op == '4':
                    print('--------------------------------------')
                    filmes.buscar_filmes(dicioFilmes)
                    filmesExcluidos = validacoes.validar_campo('\nDigite o código do filme a ser removido: ')
                    filmes.remover_filme(dicioFilmes, filmesExcluidos)

                elif op == '5':
                    print('--------------------------------------')
                    filmes.mostrar_filmes(dicioFilmes)

                elif op == '6':
                    print('------------------------------------')
                    rendimentos.ver_rendimento_do_dia(dicioFilmes)

                elif op == '7':
                    print('------------------------------------')
                    rendimentos.ingressos_vendidos_total(dicioFilmes)

                elif op == '8':
                    print('------------------------------------')
                    rendimentos.ingressos_vendidos_por_filme(dicioFilmes)

                elif op == '9':
                    print('------------------------------------')
                    rendimentos.relatorio_de_desempenho(dicioFilmes)

        else:
            print('\nUsuário ou senha inválidos ou não cadastrados como Administrador.')

    elif valor == '2':
        print('--------------------------------------')
        print('Faça login para continuar.\n')
        loginNome = validacoes.validar_campo('Insira seu usuário: ')
        email = validacoes.validar_campo('Insira seu email: ')
        senha = validacoes.validar_campo('Insira sua senha: ')

        if validacoes.login_usuario(usuarios, loginNome, email, senha) and usuarios[loginNome][2] == '2':
            print('\nLogin concluído.')
            while True:
                menus.menu_cliente()
                op = validacoes.validar_campo('\nDigite a opção desejada: ')
                if op == '0':
                    break
                elif op == '1':
                    print('--------------------------------------')
                    ingressos.alimentos()
                elif op == '2':
                    print('------------------------------------')
                    filmes.mostrar_filmes(dicioFilmes)
                elif op == '3':
                    print('------------------------------------')
                    ingressos.ver_ingressos_cliente(loginNome)
                elif op == '4':
                    print('------------------------------------')
                    filmes.grafico_filmes_mais_assistidos(dicioFilmes)

        else:
            print('\nUsuário ou senha inválidos ou não cadastrados como Cliente.')

    elif valor == '3':  # Cadastrar usuário
        validacoes.cadastrar_user(usuarios)

    elif valor == '4':  # Sair do sistema
        print('--------------------------------------')
        print('Saindo do sistema.')
        break

    else:
        print('--------------------------------------')
        print('Opção inválida.')
