lanche = ('hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[1])
print(lanche[3])
print(lanche[-1])
print(lanche[1:3])
print(lanche[2:])
print(lanche[1::2])

#tuplas são imutaveis
#lanche[1] = 'Refrigerante' erro

for comida in lanche:
    print(f'vou comer{comida}')
print('Comi muito')

for cont in range(0, len(lanche)):
    print(lanche[cont])

for pos, comida in enumerate(lanche):
     print(f'vou comer {comida} na posição {pos}')