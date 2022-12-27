""" Desafio 041
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
"""
from datetime import date

msg = '        Categoria de um Atleta       '
m = len(msg)
print('\033[32m' + ('-' * m))
print('{}'.format(msg))
print(('-' * m) + '\033[m')

ano = int(input('Ano de Nascimento: '))
dat = date.today().year
ano1 = dat - ano
rank = ''  # rank vazio para declarar a existência da variável
executa = True  # Teste booleano para não executar as categorias dos atletar e revelar a mensagem de erro
teste = ano <= dat  # Teste boolano para evitar erro do ano inserido ser maior que o ano atual

# CONDIÇÕES
if ano1 <= 9 and teste:
    rank = 'MIRIM'
elif ano1 <= 14 and teste:
    rank = 'INFANTIL'
elif ano1 <= 19 and teste:
    rank = 'JUNIOR'
elif ano1 <= 20 and teste:
    rank = 'SÊNIOR'
elif 20 < ano1 < 130 and teste:
    rank = 'MASTER'
else:
    executa = False
    print('\033[31mERRO: VALOR INVÁLIDO\033[m')

if executa:
    print('O atleta tem {} anos.'.format(ano1))
    print('Classificação: \033[34m{}\033[m'.format(rank))
