""" Desafio 039
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date

msg = '        Alistamento Militar        '
m = len(msg)
print('\033[32m' + ('-' * m))
print('{}'.format(msg))
print(('-' * m) + '\033[m')

ano_n = int(input('Ano de nascimento: '))

ano = date.today().year  # O ano atual
idade = ano - ano_n  # A idade
falta = 18 - idade  # Quantos anos falta para chegar aos 18 anos
atraso = idade - 18  # Quantos anos já ultrapassou a data de alistamento
alistamento = ano_n + idade + falta  # Em quantos anos irá fazer 18 anos

print('Quem nasceu em {} tem {} anos em {}.'.format(ano_n, idade, ano))
if idade < 18:
    print('\033[32mAinda faltam {} anos para o alistamento.'.format(falta))
    print('Seu alistamento será em {}.'.format(alistamento))
elif idade > 18:
    print('\033[31mVocê já deveria ter se alistado há {} anos.'.format(atraso))
    print('Seu alistamento foi em {}.'.format(alistamento))
else:
    print('\033[33mVocê tem que se alistar IMEDIATAMENTE!.'.format(ano_n, idade, ano))
print('\033[m', end='')  # Encerrando o processo de cores e desconsiderando o salto do print caso haja continuidade.
