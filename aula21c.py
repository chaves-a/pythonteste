def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 fora vale {n1}')


# Veja que a variável n1 ele criou como local para dentro da função... mas ele mantém fora da função o escopo global da N1
