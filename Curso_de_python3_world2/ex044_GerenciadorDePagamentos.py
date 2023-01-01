""" Desafio 044
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
"""

msg = '        Formas de Pagamento da Loja        '
m = len(msg)
print('\033[32m' + ('-' * m))
print('{}'.format(msg))
print(('-' * m) + '\033[m')

valor = float(input('Preço das compras: R$'))
pg = int(input('''FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Escolha a opção? '''))

aprovar = True
novo_valor = 0

if pg == 1:
    novo_valor = valor - (valor * 10) / 100
elif pg == 2:
    novo_valor = valor - (valor * 5) / 100
elif pg == 3:
    parcela = int(input('Quantas parcelas? '))
    if parcela == 1 or parcela == 2:
        novo_valor = valor
        juros = novo_valor / parcela
        print('Sua compra será parcelada em {}x de R${:.2f} SEM JUROS'.format(parcela, juros))
    else:
        aprovar = False
        print('ERRO: Número de parcela inválida pela opção selecionada!')
elif pg == 4:
    parcela = int(input('Quantas parcelas? '))
    if parcela >= 3:
        novo_valor = valor + (valor * 20) / 100
        juros = novo_valor / parcela
        print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcela, juros))
    else:
        aprovar = False
        print('ERRO: Número de parcela inválida pela opção selecionada!')
else:
    aprovar = False
    print('ERRO: Opção digitada inválida. Tente novamente! ')

if aprovar:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, novo_valor))
