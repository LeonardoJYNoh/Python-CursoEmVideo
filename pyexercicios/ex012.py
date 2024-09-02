preco = float(input('Qual é o preco do produto? R$'))

promocao = preco*0.95

print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, promocao))