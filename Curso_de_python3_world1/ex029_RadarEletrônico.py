""" Desafio 029
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite."""

from time import sleep

msg = '    Consulta de Multa   '
m = len(msg)
print('-' * m)
print('{}'.format(msg))
print('-' * m)

velocidade = int(input('Qual é a velocidade do carro? '))

if velocidade <= 80:
    sleep(0.5)
    print('Velocidade dentro do limite aceitável\nTenha um bom dia! Dirija com segurança')

else:
    print('Ultrapassou a velocidade máxima permitida de 80km/h. Você foi multado!')
    sleep(1)
    print('Cálculando o valor da multa... ')
    sleep(3)
    print('Sua multa é de R${:.2f} Reais.'.format((velocidade - 80) * 7))
