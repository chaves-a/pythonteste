def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# Programa principal
soma(4, 5)
soma(5, 1)
# também posso explicitar na chamada da função...
soma(a=4, b=5)
soma(b=4, a=5) # explicitando eu posso mudar a ordem...
