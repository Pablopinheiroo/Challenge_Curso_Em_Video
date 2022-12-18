""" Desafio 033
Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""

msg = '   Identificando o Maior e o Menor Valor    '
m = len(msg)
print('-' * m)
print('{}'.format(msg))
print('-' * m)

numero_1 = int(input('Informe o Primero Valor: '))
numero_2 = int(input('Informe o Segundo Valor: '))
numero_3 = int(input('Informe o Terceiro Valor: '))
print('-' * m)

# Condição simples para o número menor
menor = numero_1
if numero_2 < numero_1 and numero_2 < numero_3:
    menor = numero_2
if numero_3 < numero_1 and numero_3 < numero_2:
    menor = numero_3

# Condição simples para o número maior
maior = numero_1
if numero_2 > numero_1 and numero_2 > numero_3:
    maior = numero_2
if numero_3 > numero_1 and numero_3 > numero_2:
    maior = numero_3

print('O menor valor digitado foi {}\nO maior valor digitado foi {}'.format(menor, maior))
