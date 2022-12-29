""" Desafio 042
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
"""

print('\033[33m=-' * 12 + ' TIPO DE TRIÂNGULO ' + 11 * '-=' + '\033[m')
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
print('\033[33m-=-' * 22 + '\033[m')
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('"\033[34mEQUILÁTERO\033[m"')
        print('Pois, Possuem todos os Lados iguais!')
    elif (r1 == r2 and r1 != r3) or (r2 == r3 and r2 != r1) or (r1 == r3 and r1 != r2):
        print('"\033[34mISÓSCELES\033[m"')
        print('Pois, dois Lados são iguais!')
    else:
        print('"\033[34mESCALENO\033[m"')
        print('Pois, todos os Lados são diferentes!')
else:
    print('\033[31mOS SEGMENTOS ACIMA NÃO PODEM FORMAR TRIÂNGULO\033[m')
print('\033[33m-=-' * 22)
