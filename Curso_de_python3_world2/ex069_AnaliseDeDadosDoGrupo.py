""" Desafio 069
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se
o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
"""

msg = '             Cadastramento de Pessoas            '
m = len(msg)
print('\033[32m' + ('-' * m))
print(f'{msg}')
print(('-' * m) + '\033[m')

sexo = continua = ' '
homem = maior = mulher = 0
while True:
    print('-'*25)
    print('   INSIRA OS DADOS PESSOA    ')
    print('-'*25)
    idade = int(input('Idade: '))
    if idade >= 18:
        maior += 1

    while sexo not in 'mf':
        sexo = str(input('Sexo: [M/F] ')).strip().lower()[0]
        if sexo == 'm':
            homem += 1
        else:
            if idade <= 20:
                mulher += 1
    print('-' * 25)
    while continua not in 'sn':
        continua = str(input('Quer Continuar? [S/N] ')).strip().lower()[0]
    if continua == 's':
        sexo = continua = ' '
    else:
        break

print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher} mulheres com menos de 20 anos')
