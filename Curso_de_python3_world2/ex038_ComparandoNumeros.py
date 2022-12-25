""" Desafio 038
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais"""

msg = '        Qual valor é o Valor maior ? ou são eles iguais ?        '
m = len(msg)
print('\033[32m' + ('-' * m))
print('{}'.format(msg))
print(('-' * m) + '\033[m')

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

if num1 > num2:
    print('O PRIMEIRO valor é maior')
elif num2 > num1:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS')
