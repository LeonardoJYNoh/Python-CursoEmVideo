nome = input('Digite seu nome completo: ')
print('Analisando seu nome...')
print('Seu nome em maiúsculas é', nome.upper())
print('Seu nome em minúsculas é', nome.lower())

espacos = nome.count(' ')
tamanho = len(nome)
primeiro = nome.find(' ')
pn = nome[0:primeiro]
#split como exemplo
#pn = nome.split() >>> pn[0]


print('Seu nome tem ao todo {} letras'.format(tamanho - espacos))
print('Seu primeiro nome é {} e ele tem {} letras'.format(pn, len(pn)))