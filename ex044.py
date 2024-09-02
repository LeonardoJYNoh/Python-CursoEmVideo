print('='*10, 'LOJAS NOH', '='*10)
preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = preco * 0.9
elif opcao == 2:
    total = preco * 0.95
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x e R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 0.2)
    totparc = int(input('Quantas parcelas'))
    parcela = preco / totparc
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(totparc, parcela))
else:
    total = preco
    print('Opção inválidade de pagamento. Tente novamente')

print('Sua compra de R${:.2f} vai custa R${:.2f} no final'.format(preco, total))