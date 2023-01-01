""" Desafio 043
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""

msg = '        Avaliando seu IMC       '
m = len(msg)
print('\033[32m' + ('-' * m))
print('{}'.format(msg))
print(('-' * m) + '\033[m')

peso = float(input('Qual é seu peso? (Kg): '))
altura = float(input('Qual é sua altura? (m): '))

imc = peso / (altura * altura)

if imc < 18.5:
    msg = 'Abaixo do Peso'
elif imc < 25:
    msg = 'com o Peso ideal'
elif imc < 30:
    msg = 'com Sobrepeso'
elif imc < 40:
    msg = 'em estado de Obesidade'
else:
    msg = 'com Obesidade mórbida'

print('O IMC dessa pessoa é de {:.1f}'.format(imc))
print('Você está', msg)
