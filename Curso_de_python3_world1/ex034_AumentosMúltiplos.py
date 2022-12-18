""" Desafio 034
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""

msg = '             Aumento salarial             '
m = len(msg)
print('-' * m)
print('{}'.format(msg))
print('-' * m)

salario = float(input('Qual é o salário do funcionário? R$ '))

# Estrutura Condicional Simplificada
# salario_novo receberá o salário com 15% se for menor que 1250, caso contrário receberá um aumento de 10%
salario_novo = salario + (salario * 15 / 100) if salario <= 1250 else salario + (salario * 10 / 100)
print('Quem recebia R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, salario_novo))

