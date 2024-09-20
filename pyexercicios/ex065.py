#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

continua = 'S'
#usaremos o maiusculo para aceitar todos os strings, maiusculos ou minusculos
soma = 0
contador = 0

while continua in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    contador += 1
    continua = input('Quer continuar? [S/N]').upper().strip()[0]
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
print('Você digitou {} números e a média foi {:.2f}'.format(contador, soma/contador))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))



#esse codigo não é totalmente otimizado, ele checa mtas coisas desnecessarias aumentando o tempo de processamento.

#podemos otimizar esse loop perguntando o número fora dele para evitar a comparação entre o maior e menor.


'''
numero = int(input('Digite um número: '))
maior = menor = soma = numero
contador = 1
while continua in 'Ss'
    if continua == 'S'
        numero = int(input('Digite um número: '))
        soma += numero
        contador += 1
        continua = input('Quer continuar? [S/N]').upper().strip()[0]
'''