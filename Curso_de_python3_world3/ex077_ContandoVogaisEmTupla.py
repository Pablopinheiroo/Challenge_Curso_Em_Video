""" Desafio 077
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

msg = '           Separando Vogais           '
m = len(msg)
print('\033[32m' + ('=' * m))
print(f'{msg}')
print(('=' * m) + '\033[m')

palavras = ('amigo', 'computador', 'historia', 'porta', 'telefone', 'vida', 'cidade', 'pessoa', 'carro', 'verde')

for i in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[i].upper()} temos: ', end='')
    for letras in palavras[i]:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')
