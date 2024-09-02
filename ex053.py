#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

frase = input('Digite uma frase: ').upper().strip()

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
tamanho = len(frase)

for i in range(len(junto)-1, -1, -1):
    inverso += junto[i]

print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('Está frase é um Palíndromo')
else:
    print('Esta frase não é um Palíndromo')