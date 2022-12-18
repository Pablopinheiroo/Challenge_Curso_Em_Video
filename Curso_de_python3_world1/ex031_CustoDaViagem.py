""" Desafio 031
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da
passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas."""

from time import sleep

msg = '   Calculando o Valor da Passagem   '
m = len(msg)
print('-' * m)
print('{}'.format(msg))
print('-' * m)

km = float(input('Informe a Distância da Viagem? (km): '))

# Para if será calculado o valor da passagem em 0.5
if km <= 200:
    valor_passagem = 0.5 * km
    print('Aguarde um momento')
    sleep(1)
    print('Percorrendo {} Km, sua passagem irá custar R${:.2f} Reais.'.format(km, valor_passagem))
# Para else será calculado o valor da passagem em 0.45
else:
    valor_passagem = 0.45 * km
    print('Aguarde um momento')
    sleep(1)
    print('Por percorrer uma longa distância com a nossa empresa, será cobrado um valor menor que o habitual!')
    sleep(1.5)
    print('Percorrendo {} Km, sua passagem irá custar R${:.2f} Reais.'.format(km, valor_passagem))
