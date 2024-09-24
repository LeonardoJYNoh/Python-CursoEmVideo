#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = list()
while True:
    novo = int(input('Digite um valor: '))
    if novo in lista:
        print('Valor duplicado! Não vou adcionar...')
    else:
        print('Valor adicionardo com sucesso...')
        lista.append(novo)
    continua = ' '
    while continua not in 'SN':
        continua = input('Quer continuar? [S/N] ').upper().strip()[0]
    if continua == 'N':
        break
lista.sort()
#necessita organizar antes
print(f'Você digitou os valores {lista}')