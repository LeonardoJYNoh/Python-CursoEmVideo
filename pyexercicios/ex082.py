lista = []
pares = []
impares = []
while True:
    valor = int(input('Digite um valor: '))
    continua = ' '
    lista.append(valor)
    while continua not in 'SN':
        continua = input('Quer continuar? [S/N] ').upper().strip()[0]
    if continua == 'N':
        break

print('-='*30)
print(f'A lista completa é {lista}')
lista.sort()

#ordenei depois de print a lista, para economizar o processo de organização depois, agilizando o procesos de processamento.

for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')