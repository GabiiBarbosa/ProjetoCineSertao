import validacoes

def cadastrar_filme(dicioFilmes):
    while True:
        codigoFilme = validacoes.validar_campo('Insira um código de identificação para o filme: ')
        if codigoFilme in dicioFilmes:
            print('Código já cadastrado, insira outro código.')
        else:
            break

    while True:
        nomeDoFilme = validacoes.validar_campo('Insira o nome do filme: ')
        nomeexistente = False
        for filme in dicioFilmes:
            if dicioFilmes[filme][0] == nomeDoFilme:
                nomeexistente = True
                break
        if nomeexistente:
            print('Filme já cadastrado, insira outro nome.')
        else:
            break
    sinopseDoFilme = validacoes.validar_campo('Insira a sinopse do filme: ')
    generoDoFilme = validacoes.validar_campo('Insira o gênero do filme: ')
    duracaoDoFilme = validacoes.validar_campo('Insira a duração do filme: ')

    while True:
        salaDoFilme = int(validacoes.validar_campo('Insira a sala do filme: '))
        salaocupada = False
        for filme in dicioFilmes:
            if dicioFilmes[filme][4] == salaDoFilme:
                salaocupada = True
                break
        if salaocupada:
            print('Sala ocupada, insira uma nova sala.')
        else:
            break

    capacidadeDoFilme = 100
    horarioDoFilme = validacoes.validar_campo('Insira o horário do filme: ')
    valorDoFilme = float(validacoes.validar_valor('Insira o valor do ingresso: R$ '))

    dicioFilmes[codigoFilme] = [nomeDoFilme, sinopseDoFilme, generoDoFilme, duracaoDoFilme,
                                salaDoFilme, capacidadeDoFilme, horarioDoFilme, valorDoFilme, 0]

    print('\nFilme cadastrado com sucesso!')

def buscar_filmes(dicioFilmes):
    busca = input('Digite o nome do filme: ')
    busca = busca.upper()
    encontrado = False

    for codigoFilme, filme in dicioFilmes():
        nomeFilme = filme[0].upper()

        if busca in nomeFilme:
            print(f'\nCódigo: {codigoFilme} - Nome: {filme[0]}')
            encontrado = True

    if not encontrado:
        print('Filme não encontrado!')

    return encontrado

def atualizar_filme(dicioFilmes):
    codigo_filme = validacoes.validar_campo('Digite o código do filme a ser atualizado: ')

    if codigo_filme not in dicioFilmes:
        print('Filme não encontrado.')
        return

    campos_validos = ['nome', 'sinopse', 'genero', 'duracao', 'sala', 'capacidade', 'horario', 'valor']
    campo = validacoes.validar_campo('Digite o campo a ser atualizado (nome, sinopse, genero, duracao, sala, horario, valor): ')

    if campo not in campos_validos:
        print('Campo inválido.')
        return

    novo_valor = validacoes.validar_campo('Digite o novo conteúdo: ')

    if campo == 'nome':
        for filme_cod, filme_nome in dicioFilmes.items():
            if novo_valor == filme_nome:
                print('O nome do filme já está em uso.')
                return
    elif campo == 'sala':
        for filme_cod, filme_sala in dicioFilmes.items():
            if novo_valor == filme_sala[4]:
                print('A sala do filme já está em uso.')
                return
    if campo == 'valor':
        for filme_id, filme_info in dicioFilmes.items():
            novo_valor = float(novo_valor)

    dicioFilmes[codigo_filme][campos_validos[campo]] = novo_valor
    print(f'{campo} do filme atualizado com sucesso.')

def remover_filme(dicioFilmes, filmesExcluidos):
    if filmesExcluidos in dicioFilmes:
        dicioFilmes.pop(filmesExcluidos)
        print('\nFilme removido com sucesso.')
    else:
        print('\nFilme não encontrado.')

def mostrar_filmes(dicioFilmes):
    filmes_disponiveis = len(dicioFilmes) > 0
    if not filmes_disponiveis:
        print('Não há filmes disponíveis no momento.\n')
    else:
        print('Esses são os filmes disponíveis:')
        for x in dicioFilmes:
            print(f'\n{dicioFilmes[x][0]}')
            print(f'Sinopse: {dicioFilmes[x][1]}')
            print(f'Gênero: {dicioFilmes[x][2]}')
            print(f'Duração: {dicioFilmes[x][3]}')
            print(f'Sala: {dicioFilmes[x][4]}')
            print(f'Quantidade de cadeiras: {dicioFilmes[x][5]}')
            print(f'Horário: {dicioFilmes[x][6]}')
            print(f'Valor: {dicioFilmes[x][7]}')

import matplotlib.pyplot as mpl
def grafico_filmes_mais_assistidos(dicioFilmes):
    filmes = []
    ingressos_vendidos = []

    for filme in dicioFilmes.values():
        filmes.append(filme[0])
        if len(filme) < 9:
            ingressos_vendidos.append(0)
        else:
            ingressos_vendidos.append(filme[8])

    mpl.figure(figsize=(10, 5))
    mpl.bar(filmes, ingressos_vendidos, color='skyblue')
    mpl.xlabel('Filmes')
    mpl.ylabel('Ingressos Vendidos')
    mpl.title('Filmes Mais Assistidos')
    mpl.xticks(rotation=45, ha='right')
    mpl.tight_layout()
    mpl.show()