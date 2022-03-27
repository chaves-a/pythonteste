galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3): # nesse for ele cria a lista dado com o par de informações e carrega o par para a lista galera.. cada par digitado pelo usuário
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # o [:] é que garante a cópia dos dados
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')
