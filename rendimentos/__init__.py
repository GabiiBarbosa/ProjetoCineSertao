import filmes
import validacoes

def ver_rendimento_do_dia(dicioFilmes):
    total = 0
    for codigoFilme in dicioFilmes:
        filme = dicioFilmes[codigoFilme]
        total += filme[8] * filme[7]
    print(f'\nRendimento do dia: R${total}\n')


def ingressos_vendidos_total(dicioFilmes):
    print('\nIngressos vendidos por filme:')
    for codigoFilme in dicioFilmes:
        filme = dicioFilmes[codigoFilme]
        print(f'Filme: {filme[0]}, Ingressos vendidos: {filme[8]}')

def ingressos_vendidos_por_filme(dicioFilmes):
    if not filmes.buscar_filmes(dicioFilmes):
        return
    codigoFilme = validacoes.validar_campo('Digite o código do filme: ')
    encontrado = False
    for codigo in dicioFilmes:
        if codigo == codigoFilme:
            filme = dicioFilmes[codigo]
            ingressos = (f'\nFilme: {filme[0]}, Ingressos vendidos: {filme[8]}')
            print(ingressos)
            arquivo = open('ingressos_vendidos_por_filme.txt', 'w')
            arquivo.write(ingressos)
            arquivo.close()
            encontrado = True
            break

    if not encontrado:
        print('Filme não encontrado.')

def relatorio_de_desempenho(dicioFilmes):
    ingressos_vendidos = 0
    filme_mais_vendido = ''
    maximo_vendas = 0

    for codigoFilme in dicioFilmes:
        filme = dicioFilmes[codigoFilme]
        ingressos_vendidos += filme[8]
        if filme[8] > maximo_vendas:
            maximo_vendas = filme[8]
            filme_mais_vendido = filme[0]

    print(f'Total de ingressos vendidos: {ingressos_vendidos}')
    print(f'Filme mais vendido: {filme_mais_vendido} com {maximo_vendas} ingressos.')
