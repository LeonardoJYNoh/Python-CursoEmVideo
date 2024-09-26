#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
numeros = list()
pares = list()
impares = list()

numeros.append(pares)
numeros.append(impares)

for i in range(1,8):
    valor = int(input(f'Digite o valor {i}o. valor:'))
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

pares.sort() #numeros[0].sort()
impares.sort() #numeros[1].sort()

print('-='*20)
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores impares digitados foram: {numeros[1]}')

