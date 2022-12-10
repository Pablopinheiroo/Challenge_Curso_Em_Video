""" Desafio 013
Faça um algoritmo que leia o salário de um funcionário
e mostre seu novo salário, com 15% de aumento."""

msg = 'Reajuste salarial aumento de 15%'
m = len(msg)
print('-'*m)
print('{}'.format(msg))
print('-'*m)

valor = float(input('Qual é o salário do Funcionário: R$'))

aumento = valor + (valor * 15)/100

print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(valor, aumento))
