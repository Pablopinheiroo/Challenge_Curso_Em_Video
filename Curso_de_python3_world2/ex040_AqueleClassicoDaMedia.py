""" Desafio 040
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO"""

msg = '        Verificando a Nota de um Aluno        '
m = len(msg)
print('\033[32m' + ('-' * m))
print('{}'.format(msg))
print(('-' * m) + '\033[m')

nota_1 = float(input('Primeira Nota: '))
nota_2 = float(input('Segunda Nota: '))

media = (nota_1 + nota_2) / 2

if media >= 7:
    msg = '\033[32mAPROVADO'
elif media >= 5:
    msg = '\033[33mRECUPERAÇÃO'
else:
    msg = '\033[31mREPROVADO'
print('Tirando {} e {}, a média do aluno é {:.1f}'.format(nota_1, nota_2, media))
print('O aluno está {}\033[m'.format(msg))
