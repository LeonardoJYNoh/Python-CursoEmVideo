#Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

soma = 0
contador = 0
while True:
    valor = int(input('Digite um valor (999 para parar):'))
    if valor == 999:
        break
    contador += 1
    soma += valor
print(f'a soma dos {contador} valores foi {soma}!')