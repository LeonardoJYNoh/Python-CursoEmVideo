#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year


menor = 0
maior = 0
for i in range(1, 8):
    nasc = (int(input('Em que ano a {} pessoa nasceu? '.format(i))))
    if atual - nasc < 21:
        menor += 1
    else:
        maior +=1

print('')
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
if maior != 7:
    print('E também tivemos {} pessoas menores de idade'.format(menor))