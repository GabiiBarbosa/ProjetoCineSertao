import filmes
import menus
import validacoes
dicioFilmes = {}
ingressosVendidosPorCliente = {}

def comprar_ingresso(dicioFilmes, loginNome):
    if not filmes.buscar_filmes(dicioFilmes):
        return
    while True:
        codigoFilme = validacoes.validar_campo('\nDigite o código do filme: ')
        if codigoFilme in dicioFilmes:
            break
        else:
            print('Filme não encontrado.')
            return

    while True:
        cliente = validacoes.validar_campo('\nDigite seu nome de usuário: ')
        if cliente == loginNome:
            break
        else:
            print('Nome de usuário inválido. Insira o mesmo nome utilizado para login.')


    filme = dicioFilmes[codigoFilme]
    capacidade_disponivel = filme[5]

    if capacidade_disponivel > 0:
        qtde = int(validacoes.validar_campo('\nDigite a quantidade de ingressos: '))

        if capacidade_disponivel >= qtde:
            valor_total = filme[7] * qtde
            pagamento(valor_total)
            filme[5] -= qtde
            filme[8] += qtde
            if cliente not in ingressosVendidosPorCliente:
                ingressosVendidosPorCliente[cliente] = []
            ingressosVendidosPorCliente[cliente].append((codigoFilme, qtde))
            return True
        else:
            print('Não há ingressos suficientes disponíveis.')
    else:
        print('Não há ingressos disponíveis para este filme.')
    return False

def ver_ingressos_cliente(cliente, dicioFilmes):
    if cliente in ingressosVendidosPorCliente:
        print(f'Ingressos comprados por {cliente}:')
        arquivo = open(f'{cliente}_ingressos.txt', 'w')
        for codigoFilme, qtde in ingressosVendidosPorCliente[cliente]:
            nome_filme = dicioFilmes[codigoFilme][0]
            preco_unitario = dicioFilmes[codigoFilme][7]
            total = preco_unitario * qtde
            ingresso = f'\nFilme: {nome_filme}, Quantidade: {qtde}, Total: R${total}'
            print(ingresso)
            arquivo.write(ingresso)
        arquivo.close()
    else:
        print('Nenhum ingresso comprado.')

def alimentos(dicioFilmes, loginNome):
    if not comprar_ingresso(dicioFilmes, loginNome):
        return
    while True:
        pip = input('\nGostaria de comprar pipoca ou refrigerante? [sim/não]: ')
        if pip == 'sim':
            menus.menu_comida()
            op = input('\nDigite a opção desejada: ')

            if op == '1':
                qtde = int(input('Digite a quantidade que deseja comprar: '))
                valor_total = qtde * 10.0
                pagamento(valor_total)
                break
            elif op == '2':
                qtde = int(input('Digite a quantidade que deseja comprar: '))
                valor_total = qtde * 10.0
                pagamento(valor_total)
                break
            elif op == '3':
                qtde = int(input('Digite a quantidade que deseja comprar: '))
                valor_total = qtde * 7.0
                pagamento(valor_total)
                break
            elif op == '4':
                qtde = int(input('Digite a quantidade que deseja comprar: '))
                valor_total = qtde * 15.0
                pagamento(valor_total)
                break
            else:
                print('Opção Inválida.')
        elif pip == 'nao' or pip == 'não':
            print('\nTenha um ótimo filme.')
            break
        else:
            print('Opção Inválida.')

def pagamento(valor_total):
    while True:
        menus.menu_pagamento()
        op_pagamento = input('\nDigite a opção desejada: ')

        if op_pagamento == '1':
            print(f'Pagamento de R${valor_total} realizado via PIX.')
            break
        elif op_pagamento == '2':
            print(f'Pagamento de R${valor_total} realizado via cartão de crédito.')
            break
        elif op_pagamento == '3':
            print(f'Pagamento de R${valor_total} realizado via cartão de débito.')
            break
        else:
            print('Opção Inválida. Tente novamente.')
