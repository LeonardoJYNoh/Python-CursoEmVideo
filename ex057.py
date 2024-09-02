#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

genero = input('Informe seu sexo: [M/F] ').upper()

while genero != 'M' and genero != 'F':
    genero = input('Dados inválidos. Por favor, informe seu sexo: ')
print('Sexo {} registrado com sucesso'.format(genero))