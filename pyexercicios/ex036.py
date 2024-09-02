valor = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financeamento? '))

parcela = valor/(anos * 12)

print('Para pagar uma casa de R${:.2f} em {} anos a prestação de R${:.2f}'.format(valor, anos, parcela))

if sal * 0.3 > parcela:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')