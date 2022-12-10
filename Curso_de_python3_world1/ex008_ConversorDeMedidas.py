""" Desafio 008
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros."""

msg = 'De Metros para Centímetros e Milímetros'
m = len(msg)
print('-'*m)
print('{}'.format(msg))
print('-'*m)

m = float(input('Digite o valor em Metros: '))

print('{} m = {:.0f} Centímetros.\n{} m = {:.0f} Milímetros.'.format(m, m*100, m, m*1000))
