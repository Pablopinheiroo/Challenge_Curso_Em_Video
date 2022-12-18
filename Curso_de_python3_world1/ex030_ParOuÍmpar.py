""" Desafio 030
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR."""

msg = '   Identificando se é PAR ou ÍMPAR   '
m = len(msg)
print('-' * m)
print('{}'.format(msg))
print('-' * m)

entrada_pessoa = int(input('Digite um número qualquer: '))

# Condição If para os números "Pares" e else para os "Ímpares"
if entrada_pessoa % 2 == 0:
    print('O Número {} é um número PAR.'.format(entrada_pessoa))
else:
    print('O Número {} é um número ÍMPAR.'.format(entrada_pessoa))
