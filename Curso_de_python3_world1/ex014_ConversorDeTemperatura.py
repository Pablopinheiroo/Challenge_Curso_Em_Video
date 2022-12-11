""" Desafio 014
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit."""

msg = 'Conversor de Temperatura'
m = len(msg)
print('-'*m)
print('{}'.format(msg))
print('-'*m)

tmp = float(input('Informe a temperatura em ºC: '))
f = (tmp * (9 / 5)) + 32

print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF'.format(tmp, f))
