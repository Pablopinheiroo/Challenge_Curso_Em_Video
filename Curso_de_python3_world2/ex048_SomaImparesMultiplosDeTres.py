""" Desafio 048
Faça um programa que calcule a soma entre todos os números
que são múltiplos de três e que se encontram no intervalo de 1 até 500."""

msg = '          Soma Ímpares Múltiplos de Três          '
m = len(msg)
print('\033[32m' + ('-' * m))
print('{}'.format(msg))
print(('-' * m) + '\033[m')

valores = 0
soma = 0

for impares in range(3, 501, 3):
    if impares % 2 == 1:
        valores += 1
        soma += impares
print(f'A soma de todos os {valores} valores solicitados é {soma}')
