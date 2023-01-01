""" Desafio 045
Crie um programa que faça o computador jogar Jokenpô com você."""

from random import randint

msg = '        Competindo Jokenpô: Pc vs Humano        '
m = len(msg)
print('\033[32m' + ('-' * m))
print('{}'.format(msg))
print(('-' * m) + '\033[m')

print('{:=^48}'.format(' JOKENPÔ '))
print('''ESCOLHA A SUA JOGADA
[ 1 ] \033[32mPEDRA\033[m
[ 2 ] \033[97mPAPEL\033[m
[ 3 ] \033[36mTESOURA\033[m''')
print('{:=^48}'.format(' JOKENPÔ '))

# Guarda o valor da minha Jogada
eu = int(input('QUAL SERÁ A SUA JOGADA?: '))

# O Pc gera e guarda na variável "pc", uma jogada aleatória entre 0 e 2
pc = randint(0, 2)

# Em "listaJogo" Está as jogadas dentro da lista desde a posição [0,1,2]
listaJogo = ['\033[32mPEDRA\033[m', '\033[97mPAPEL\033[m', '\033[36mTESOURA\033[m']

# Em "listaFaz" Está a Ação das Jogadas.
listaFaz = ['Quebra', 'Embrulha', 'Corta']

# A variável "eu" recebe ele mesmo -1, para se adaptar com as lista das Jogadas
# Transformando valor inserido em input em um novo valor, ou seja, a partir desse momento a variável "eu"
# Não será a mesma inserida inicialmente no input, e sim um novo valor.
eu = eu - 1
# Funciona: Se o número escolhido for menor que 3, de acordo com a "listaJogo" [0,1,2] e evitando Nºs Acima
# Funciona: Se a pessoa Não digitar 0, por isso a expressão "eu != -1". Devido a variável anterior de: (eu = eu - 1)
# Funciona: Se a minha Jogada não coincidir com a do "PC"
if eu < 3 and eu != pc and eu != -1:
    if eu == 0 and pc == 2 or (eu == 2 and pc == 1) or (eu == 1 and pc == 0):
        resultado = 'GANHOU'
        ganho = listaJogo[eu]
        ganhoFaz = listaFaz[eu]
        perda = listaJogo[pc]
        v1 = ganho
        v2 = perda
    else:
        resultado = 'PERDEU'
        ganho = listaJogo[eu]
        ganhoFaz = listaFaz[pc]
        perda = listaJogo[pc]
        v1 = perda
        v2 = ganho
    print('''\033[35mVOCÊ {}!\033[m
Você escolheu {} e o Computador {}
{} {} {}'''.format(resultado, ganho, perda, v1, ganhoFaz, v2))

# Funciona se der Empate & valor entre(0,1,2)
elif eu == pc and eu < 3 and eu != -1:
    ganho = listaJogo[eu]
    ganhoFaz = listaFaz[eu]
    perda = listaJogo[pc]
    print('\033[33mDEU EMPATE!\033[m')
    print('Você escolheu {} e o Computador {}'.format(ganho, perda))
# Funciona para valores maiores que 2, para a escolha do 0
else:
    print('\033[31mERRO: DIGITE UM VALOR VÁLIDO\033[m')
print('{:=^48}'.format('========='))
