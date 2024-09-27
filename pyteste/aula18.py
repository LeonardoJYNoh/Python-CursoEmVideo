pessoas = {'nome':'Leonardo', 'sexo':'M', 'idade':21}
print(pessoas)
#print(pessoas[0]) erro
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for f, v in pessoas.items():
    print(f'{k} = {v}')

#podemos deletar
#del pessoas['sexo']
#podemos mudar
#pessoas['nome'] = Jorge
#ou adicionar valores
#pessoas['peso'] =  98.5 

brasil = list()
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', }
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])


estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    print(e)
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')