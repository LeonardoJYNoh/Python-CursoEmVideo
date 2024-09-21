'''
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
'''
print('-'*30)
print('LOJA SUPER BARATÃO')
print('-'*30)

#mais otimizado seria fazer a primeira compra, fora do loop para melhorar o funcionamento.

cont = soma = totmil = 0
while True:
    produto = input('Nome do Produto: ')
    preco = float(input('Preço: R$'))
    cont += 1
    soma += preco
    resp = ' '
    if cont == 1:
        menor = preco
        prodmenor = produto
    else:
        if preco < menor:
            menor = preco
            prodmenor = produto
    if preco > 1000:
        totmil += 1
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N]').upper().strip()[0]
    if resp == 'N':
        break
print('--------------FIM DO PROGRAMA--------------')
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {prodmenor} que custa R${menor:.2f}')