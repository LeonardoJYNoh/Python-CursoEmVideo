#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

cont = 0
soma = 0
for i in range(0, 501, 3):
    soma += i
    cont += 1
print('foram somas {} e o resutado deu {}'.format(cont, soma))