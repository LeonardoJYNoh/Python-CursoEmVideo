#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = list()
for i in range(0,5):
    valor = int(input('Digite um valor: '))
    pos = 0
    for j in lista:
        if valor > j:
            pos += 1
        else:
            break
    if pos == len(lista):
        print('Adicionado ao final da lista...')
    else:
        print(f'Adicionado na posição {pos} da lista...')
    lista.insert(pos,valor)
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')

'''
codigo do gustavo guanabara
lista = []
for c in range(0,5)
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')
'''