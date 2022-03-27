s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))


# o range(a, b) vai do "a" até "b - 1"
'''
for c in range(1, 6):
    print('Oi')
print('FIM')
'''

# contagem de 1 até 6: range(1, 7)

# contagem de 6 até 0: range(6, 0, -1)
'''
for c in range(1, 6):
    print(c)
print('FIM')
'''

# contagem de 0 a 7 pulando de 2 em 2
'''
for c in range(0, 7, 2):
    print(c)
print('FIM')
'''

# ler um valor (n) e usa-lo como parte de passagem pro for
'''
n = int(input('Digite um número: '))
for c in range(0, n + 1):
    print(c)
print('FIM')
'''

# ler valores de início, fim e o passo como parâmetros para o for
'''
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f + 1, p):
    print(c)
print('FIM')
'''

# ler/pedir pra digitar um número x vezes (3 vezes, no exemplo)
'''
for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('FIM')
'''

# fazer o somatório de x números (4 números, no exemplo)
'''
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))
'''
