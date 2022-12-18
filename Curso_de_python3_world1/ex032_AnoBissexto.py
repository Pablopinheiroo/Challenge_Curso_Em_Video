""" Desafio 032
Faça um programa que leia um ano qualquer e mostre se ele é bissexto."""
from datetime import date
msg = '   Separando o Primeiro e o Último Nome   '
m = len(msg)
print('-' * m)
print('{}'.format(msg))
print('-' * m)
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 or 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO'.format(ano))
