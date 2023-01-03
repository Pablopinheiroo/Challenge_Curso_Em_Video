""" Desafio 049
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for."""

msg = '             Tabuada V2.0             '
m = len(msg)
print('\033[32m' + ('-' * m))
print('{}'.format(msg))
print(('-' * m) + '\033[m')

tabuada = int(input('Digite um número para ver sua tabuada: '))

for conta in range(1, 11):
    print('{}  x {:2} = {}'.format(tabuada, conta, tabuada * conta))
