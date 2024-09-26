'''
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

matriz = []
linha = []

for i in range(0,3):
    for j in range(0,3):
        valor = int(input(f'Digite um valor para [{i},{j}]: '))
        linha.append(valor)
    matriz.append(linha[:])
    linha.clear()

print('-='*40)

somapar = tercol = maxdois = 0
for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]:^5}]',end='')
        if matriz[i][j] % 2 ==0:
            somapar += matriz[i][j]
        if j == 2:
            tercol += matriz[i][j]
        if i == 1:
            if j == 0:
                maxdois = matriz[i][j]
            if matriz[i][j] > maxdois:
                maxdois = matriz[i][j]
    print()

print('-='*40)
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {tercol}')
print(f'O maior valor da segunda linha é {maxdois}')
