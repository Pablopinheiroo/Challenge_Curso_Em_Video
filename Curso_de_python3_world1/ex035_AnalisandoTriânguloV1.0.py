""" Desafio 035
Desenvolva um programa que leia o comprimento de três retas e diga
ao usuário se elas podem ou não formar um triângulo."""

msg = '        Analisador de Triângulos        '
m = len(msg)
print('-' * m)
print('{}'.format(msg))
print('-' * m)

t1 = float(input('Primeiro Segmento: '))
t2 = float(input('Segundo Segmento: '))
t3 = float(input('Terceiro Segmento: '))

if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
