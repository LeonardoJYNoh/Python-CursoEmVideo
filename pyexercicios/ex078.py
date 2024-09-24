#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = list()
for i in range(0,5):
    valores.append(int(input(f'Digite um valor para a Posição {i}: ')))

print('=-'*30)
print(f'Você digiou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')

for pos, num in enumerate(valores):
    if max(valores) == num:
        print(f'{pos}... ',end='')

print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')
for pos, num in enumerate(valores):
    if min(valores) == num:
        print(f'{pos}... ',end='')


'''
max = min = 0

for c in range(0, 5):
    valores.append(int(input('...')))
        if c == 0:
            max = min = valores[c]
        else:
            if valores[c] > max:
                max = valores[c]
            if valores[c] < min:
                min = valores[c]
print(...)
    for i, v in enumerate(valores):
        if v == max:
            print(f'{i}... ',end='')
    for i, v in enumerate(valores):
        if v == min:
            print(f'{i}... ',end='')
        
'''