""" Desafio 059
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""


msg = '             Menu de Opções            '
m = len(msg)
print('\033[32m' + ('-' * m))
print('{}'.format(msg))
print(('-' * m) + '\033[m')

menu = False

n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))

while not menu:
    opcao = int(input('''\033[33m[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa\033[m
>>>>> Qual é a sua opção? '''))

    if opcao == 1:
        soma = n1 + n2
        print(f'A soma de {n1} + {n2} é igual a  {soma}')
    elif opcao == 2:
        resul = n1 * n2
        print(f'A multiplicação de {n1} x {n2} é igual a {resul}')
    elif opcao == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print(f'O número maior é o {maior}')
    elif opcao == 4:
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif opcao == 5:
        print('Saindo do programa...')
        menu = True
    else:
        print('Opção inválida. Tente Novamente')
    print('=-' * 15)

print('FIM do Programa!')
