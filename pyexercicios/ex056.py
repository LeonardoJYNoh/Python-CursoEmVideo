

soma = 0
mulherjovem = 0
for i in range(1, 5):
    print('----- {}° PESSOA -----'.format(i))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    if i == 1 and sexo == 'M':      #podemos usar essa parte fora do
        velhonome = nome            #'for' para acelerar o processamento do codigo
        velhoidade = idade
    else:
        if idade > velhoidade and sexo == 'M':
            velhoidade = idade
            velhonome = nome
    soma += idade
    if sexo == 'F' and idade < 20:
        mulherjovem += 1

print('A média de idade do grupo é de {:.1f} anos'.format(soma/4))
print('O homem mais velho tem {} anos e se chama {}.'.format(velhoidade, velhonome))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulherjovem))