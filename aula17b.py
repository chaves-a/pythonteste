valores = list()  # outra forma de criar lista vaiza: valores = []
valores.append(5)
valores.append(9)
valores.append(4)

print(valores)

for v in valores:
    print(f'{v}...')

for c, v in enumerate(valores):  # o enumerate pega tanto a chave quanto o valor
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')


outra = list()
for cont in range(0, 5):
    outra.append(int(input('Digite um valor: ')))

for c, v in enumerate(outra):
    print(f'Na posição {c} encontrei o valor {v}!')
