""" Desafio 036
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado."""

msg = '        Aprovando ou Não o Empréstimo Bancário        '
m = len(msg)
print('\033[32m' + ('-' * m))
print('{}'.format(msg))
print(('-' * m) + '\033[m')

casa = float(input('Valor da casa: R$ '))
salario_comprador = float(input('Salário do comprador: R$ '))
ano = int(input('Quantos anos de financiamento? '))

limite = (salario_comprador * 30) / 100  # 30% do salário do comprador
parcela_casa = casa / (ano * 12)  # Parcela mensal da casa pela quantidade dos anos de financiamento

msg_1 = '\033[32mpode ser CONCEDIDO'
msg_2 = '\033[31mNEGADO!'

msg = msg_1 if parcela_casa <= limite else msg_2
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, ano, parcela_casa))
print('Empréstimo {}'.format(msg))
