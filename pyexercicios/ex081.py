'''
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.                                          B) A lista de valores, ordenada de forma decrescente.                                        C) Se o valor 5 foi digitado e está ou não na lista.
'''

lista = []
cont = 0
while True:
    valor = int(input('Digite um valor: '))
    continua = ' '
    lista.append(valor)
    cont += 1
    while continua not in 'SN':
        continua = input('Quer continuar? [S/N] ').upper().strip()[0]
    if continua == 'N':
        break

lista.sort(reverse=True)

print('-='*30)
print(f'Voce digitou {cont} elementos')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')