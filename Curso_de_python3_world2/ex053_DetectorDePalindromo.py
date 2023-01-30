""" Desafio 052
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços."""

msg = '             DETECTOR DE PALÍNDROMO            '
m = len(msg)
print('\033[32m' + ('-' * m))
print('{}'.format(msg))
print(('-' * m) + '\033[m')

frase = str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]  # irá pegar as palavras de "junto" do começo ao final voltando -1

msg1 = '\033[32mÉ SIM\033[m'
msg2 = '\033[31mNÃO É\033[m'

msg = msg1 if inverso == junto else msg2
print(f'O inverso de {junto} é {inverso}')
print(f'A frase digitada {msg} um palíndromo!')
