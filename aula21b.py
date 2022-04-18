def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

# Programa Principal
n = 2
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, x vale {x}')


# a variável n tem escopo global
# a variável x tem escopo local... só vai funcionar dentro do def...
