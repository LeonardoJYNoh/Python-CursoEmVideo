#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

#primeira execução, codigo maior, mas mais rapido devido


peso = float(input('Peso da 1 pessoa: '))
maior = peso
menor = peso
for i in range(2, 6):
    peso = float(input('Peso da {} pessoa: '.format(i)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso lido foi de {:.1f}Kg'.format(maior))
print('O menor peso lido foi de {:.1f}Kg'.format(menor))


#segunda resolução

'''for p in range(1, 6):
    peso = float(input('Peso da {} pessoa: '.format(p)))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {:.1f}Kg'.format(maior))
print('O menor peso lido foi de {:.1f}Kg'.format(menor))'''

#funciona, mais curta, so que a função 'if p == 1' faz com que cada checagem
#seja feito em todos os numeros, oq dá lentidão ao codigo
