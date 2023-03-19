""" Desafio 056
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""


msg = '             Analisador            '
m = len(msg)
print('\033[32m' + ('-' * m))
print('{}'.format(msg))
print(('-' * m) + '\033[m')

idade_t = mulheres = h_velho = velho = 0

for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).title().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    idade_t += idade
    if sexo in 'Mm' and idade > h_velho:
        h_velho = idade
        velho = nome
    if sexo == 'F' and idade < 20:
        mulheres += 1
print('-' * 15)
print('A média de Idade do Grupo é de {:.1f} anos.'.format(idade_t/4))
print(f'O homem mais velho é o Sr. {velho}, com seus {h_velho} anos.')
print(f'No Grupo existem {mulheres} mulheres com menos de 20 anos.')
