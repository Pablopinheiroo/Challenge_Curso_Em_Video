""" Desafio 076
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

print('--'*20)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('--'*20)

lista = ('Lápis', 1.75,
         'Borracha', 2.00,
         'Caderno', 15.90,
         'Estojo', 25.00,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livros', 34.90
         )
for i, item in enumerate(lista):
    if i % 2 == 0:
        print(f'{item:.<30}', end='')
    else:
        print(f'R$ {item:>6.2f}')
print('--'*20)
