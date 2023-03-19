""" Desafio 055
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos."""


msg = '             IDENTIFICANDO O PESO            '
m = len(msg)
print('\033[32m' + ('-' * m))
print('{}'.format(msg))
print(('-' * m) + '\033[m')

peso_maior = peso_menor = 0

for p in range(1, 6):
    pessoa = float(input(f'Digite o Peso da {p} Pessoa : '))
    if p == 1:
        peso_maior = pessoa
        peso_menor = pessoa
    else:
        if pessoa > peso_maior:
            peso_maior = pessoa
        if pessoa < peso_menor:
            peso_menor = pessoa
print(f'O maior peso lido foi de {peso_maior:.1f}kg\n'
      f'O menor peso lido foi de {peso_menor:.1f}kg')
