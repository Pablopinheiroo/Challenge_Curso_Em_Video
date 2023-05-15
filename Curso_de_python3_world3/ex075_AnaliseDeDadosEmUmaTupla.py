""" Desafio 075
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

msg = '           Leitura de Números           '
m = len(msg)
print('\033[32m' + ('=' * m))
print(f'{msg}')
print(('=' * m) + '\033[m')

num = (int(input('Digite um número: ')),
       int(input('Digite Outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))

print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição.')
else:
    print('O valor 3 não foi digitada em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
