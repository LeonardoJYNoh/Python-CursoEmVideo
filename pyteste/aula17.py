teste = list()
teste.append('Leonardo')
teste.append(21)
galera = list()
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)

#listas se ligam
#para se corrigir isso é necessario fazer uma copia
#galera.append(teste[:])


pessoal = [['João', 19],['Ana', 33],['Joaquim', 13],['Maria', 45]]
print(pessoal)
print(pessoal[0])
print(pessoal[0][0])
print(pessoal[2][1])

for p in pessoal:
    print(p)
    print(p[0])
    print(p[1])


galera = list()
dado = list()
for c in range(0,3):
    dado.append(input('Nome: '))
    dado.append(input('Idade: '))
    galera.append(dado[:])
    dado.clear()
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
    else:
        print(f'{p[0]} é menor de idade')