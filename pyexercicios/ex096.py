#Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.


def area(lar, comp):
    print(f'A área de um terreno {lar}x{comp} é de {lar*comp}m².')
print('  Controle de Terrenos')
print('-'*30)
lar = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(lar, comp)