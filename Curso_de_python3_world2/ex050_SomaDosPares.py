""" Desafio 050
Desenvolva um programa que leia seis números inteiros e
mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o."""

msg = '             Somando Números Pares             '
m = len(msg)
print('\033[32m' + ('-' * m))
print('{}'.format(msg))
print(('-' * m) + '\033[m')

soma = par = 0

for valor in range(1, 7):
    tabuada = int(input(f'Digite o {valor}º valor: '))
    if tabuada % 2 == 0:
        par += 1
        soma += tabuada
        
print(f'Você informou {par} número PARES e a soma foi {soma}!')