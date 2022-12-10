""" Desafio 004
Faça um programa que leia algo pelo teclado e mostre na tela o
seu tipo primitivo e todas as informações possíveis sobre ele."""

msg = 'Para obter seu tipo primitivo e outras informações'
m = len(msg)
print('-'*m)
print('{}'.format(msg))
print('-'*m)

tipo = input('Digite algo a seguir: ')
print('O tipo primitivo dese valor é: ', type(tipo))
print('Só tem espaços? ', tipo.isspace())
print('É um número? ', tipo.isnumeric())
print('É alfabético? ', tipo.isalpha())
print('É alfanumérico? ', tipo.isalnum())
print('Está em maiúsculas? ', tipo.isupper())
print('Está em minúsculas? ', tipo.islower())
print('Está capitalizada? ', tipo.istitle())
