'''
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)

valor = int(input('Qual valor você quer sacar? R$'))
total = valor
while total != 0:
    if total >= 50:
        c50 = total//50
        total = total - c50*50
        print(f'Total de {c50} cédulas de R$50')
    elif total >= 20:
        c20 = total//20
        total = total - c20*20
        print(f'Total de {c20} cédulas de R$20')
    elif total >= 10:
        c10 = total//10
        total = total - c10*10
        print(f'Total de {c10} cédulas de R$10')
    elif total >= 1:
        c1 = total//1
        total = total - c1
        print(f'Total de {c1} cédulas de R$1')
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')