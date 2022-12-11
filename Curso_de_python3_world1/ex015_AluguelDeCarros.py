""" Desafio 015
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""

msg = 'Custo do Aluguel de Carro'
m = len(msg)
print('-'*m)
print('{}'.format(msg))
print('-'*m)

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

total = (dias * 60) + (km * 0.15)

print('O Total a pagar é de R${:.2f}'.format(total))
