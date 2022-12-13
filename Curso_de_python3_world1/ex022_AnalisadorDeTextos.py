""" Desafio 022
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome."""

from time import sleep

msg = '     Informações sobre o nome de uma Pessoa     '
m = len(msg)
print('-' * m)
print('{}'.format(msg))
print('-' * m)

nome = str(input('Digite seu nome Completo: ')).strip()

print('Analisando seu nome...')
sleep(1)

print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome.replace(' ', ''))))
n = nome.split()[0]
print('Seu primeiro nome é {} e ele tem {} letras'.format(n, len(n)))
