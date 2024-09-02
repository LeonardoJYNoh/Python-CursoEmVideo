dia = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))

preco = dia*60 + 0.15*km

print('O total a pagar é de R${:.2f}'.format(preco))