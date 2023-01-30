""" Desafio 054
Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

from datetime import date

msg = '             IDENTIFICANDO MAIORIDADE            '
m = len(msg)
print('\033[32m' + ('-' * m))
print('{}'.format(msg))
print(('-' * m) + '\033[m')

ano_atual = date.today().year
maior = menor = 0

for d in range(1, 8):
    ano_nasc = int(input(f'Em que ano a {d}º Pessoa nasceu? '))
    idade = ano_atual - ano_nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
        
print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'E também tivemos {menor} pessoas menores de idade')
