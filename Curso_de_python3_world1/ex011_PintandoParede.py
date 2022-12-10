""" Desafio 011
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintála,
sabendo que cada litro de tinta, pinta uma área de 2m^2."""

msg = 'Cálculo: Quantidade de tinta: m^2'
m = len(msg)
print('-'*m)
print('{}'.format(msg))
print('-'*m)

l1 = float(input('Digite a Largura da Parede em Metros: '))
h1 = float(input('Digite a Altura da Parede em Metros: '))
area = l1 * h1
qlitro = area / 2

print('Sua parede tem a dimensão de {}m x {}m e a sua area é de {}m².'.format(l1, h1, area))
print('Para pintar essa parede, você precisará de {}l de Tinta.'.format(qlitro))

