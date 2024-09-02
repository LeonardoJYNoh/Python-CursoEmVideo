n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
else:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))