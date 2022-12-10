""" Desafio 005
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor."""

msg = 'Para obter o Antecessor e o Sucessor de um Número'
m = len(msg)
print('-'*m)
print('{}'.format(msg))
print('-'*m)

n = int(input('Digite um número inteiro: '))

print('Analisando o valor {}, seu antecessor é {} e o sucessor {}.'.format(n, n-1, n+1))
