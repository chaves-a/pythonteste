pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')  # no print formatado precisa usar aspas duplas para passar a chave
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for k in pessoas.values():
    print(k)

for k, v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['sexo']
print(pessoas)

pessoas['nome'] = 'Leandro'  # eu posso modificar o dicionário
print(pessoas)

pessoas['peso'] = 98.5
print(pessoas)