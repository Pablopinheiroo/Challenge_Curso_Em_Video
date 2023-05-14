""" Desafio 070
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""

msg = '             LOJA SUPER BARATÃO             '
m = len(msg)
print('\033[32m' + ('-' * m))
print(f'{msg}')
print(('-' * m) + '\033[m')

tot_compra = tot_produto = 0
menor_valor = None
nome_barato = ''
parada = 'S'

while parada in 'S':
    nome_produto = str(input('Nome do Produto: '))
    valor_produto = float(input('Preço: R$'))

    tot_compra += valor_produto

    if valor_produto > 1000:
        tot_produto += 1

    if menor_valor is None or valor_produto < menor_valor:
        menor_valor = valor_produto
        nome_barato = nome_produto

    parada = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]

    while parada not in 'SN':
        print('Entrada inválida. Digite S ou N.')
        parada = str(input('Quer Continuar? [S/N] ')).upper().strip()[0]

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${tot_compra:.2f}')
print(f'Temos {tot_produto} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_barato} que custa R${menor_valor:.2f}')
