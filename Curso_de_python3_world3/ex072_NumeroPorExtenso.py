""" Desafio 072
 Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
 Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

msg = '           VERIFICANDO O NÚMERO POR EXTENSO           '
m = len(msg)
print('\033[32m' + ('=' * m))
print(f'{msg}')
print(('=' * m) + '\033[m')

ext = ('zero', 'um', 'dois', 'três', 'quatro',
       'cinco', 'seis', 'sete', 'oito', 'nove',
       'dez', 'onze', 'doze', 'treze', 'catorze',
       'quinze', 'dezesseis', 'dezessete', 'dezoito',
       'dezenove', 'vinte')

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número {ext[n]}')
        continuando = str(input('Deseja Continuar? [S/N]: ')).upper().split()[0]
        while continuando not in 'SN':
            continuando = str(input('Erro. Tente novamente! Deseja Continuar? [S/N]: ')).upper().split()[0]
        if continuando == 'N':
            break
    else:
        print('Tente novamente. ', end='')
