""" Desafio 027
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente."""

msg = '   Separando o Primeiro e o Último Nome   '
m = len(msg)
print('-' * m)
print('{}'.format(msg))
print('-' * m)

nome = str(input('Digite seu nome completo: ').strip().title())
nome = nome.split()

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[-1]))
