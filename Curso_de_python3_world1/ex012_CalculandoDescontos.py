""" Desafio 012
Faça um algoritmo que leia o preço de um produto
e mostre seu novo preço, com 5% de desconto."""

msg = ' Desconto de 5% '
m = 35
print('-'*m)
print('{:.^35}'.format(msg))
print('-'*m)

valor = float(input('Digite o Preço do Produto: '))
desconto = (valor * 5)/100
desconto = valor - desconto

print('O Produto terá 5% de desconto:\nCom a promoção aplicada irá custar R${:.2f} Reais.'.format(desconto))
