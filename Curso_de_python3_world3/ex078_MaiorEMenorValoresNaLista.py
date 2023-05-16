""" Desafio 078
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

msg = '           Lista de 5 números           '
m = len(msg)
print('\033[32m' + ('=' * m))
print(f'{msg}')
print(('=' * m) + '\033[m')

menor = maior = 0
lista = []

for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        menor = maior = lista[c]
    else:
        if lista[c] > maior:  # Se a lista[c] for maior que o maior. Maior passa a valer a lista [c]
            maior = lista[c]
        elif lista[c] < menor:  # Se a lista[c] for menor que o menor. Menor passa a valer a lista [c]
            menor = lista[c]
print('-=' * 28)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, p in enumerate(lista):
    if p == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, p in enumerate(lista):
    if p == menor:
        print(f'{i}... ', end='')
print()
