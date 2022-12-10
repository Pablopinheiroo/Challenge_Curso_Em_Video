""" Desafio 010
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos Dólares ela pode comprar. *Considere: US$1,00 = R$3,27."""

msg = 'Conversão do Real para Dólar'
m = len(msg)
print('-'*m)
print('{}'.format(msg))
print('-'*m)

valor = float(input('Quanto dinheiro você tem na carteira? R$'))

x = (1 * valor)/3.27

print('Com R${} Reais, você pode comprar US${:.2f} Dólares!'.format(valor, x))

