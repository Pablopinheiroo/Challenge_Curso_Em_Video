""" Desafio 037
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""

msg = '        Conversões de Bases Numéricas        '
m = len(msg)
print('\033[32m' + ('-' * m))
print('{}'.format(msg))
print(('-' * m) + '\033[m')

numero = int(input('Digite um número inteiro: '))
escolha = int(input("""Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
Sua opção: """))

if escolha == 1:
    print('{} covertido para BINÁRIO é igual a {}'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('{} covertido para BINÁRIO é igual a {}'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('{} covertido para BINÁRIO é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida. Tente novamente!')
