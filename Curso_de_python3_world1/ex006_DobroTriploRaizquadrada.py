""" Desafio 006
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada."""

msg = 'Para Saber o Dobro, o Triplo e Sua Raiz Quadrada'
m = len(msg)
print('-'*m)
print('{}'.format(msg))
print('-'*m)

n = int(input('Digite um Número: '))

print('-> O Dobro é {}.\n-> O Triplo é {}.\n-> A Raiz Quadrada é {:.2f}.'.format(n*2, n*3, n**(1/2)))
