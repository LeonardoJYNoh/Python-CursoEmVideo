#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = []
linha = []

for i in range(0,3):
    for j in range(0,3):
        valor = int(input(f'Digite um valor para [{i},{j}]: '))
        linha.append(valor)
    matriz.append(linha[:])
    linha.clear()

print('-='*40)

for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]:^5}]',end='')
    print()