# um for para digitar números
'''
for c in range (1, 4):
    n = int(input('Digite um valor: '))
print('Fim')
'''

# um laço para digitar números quando vc não sabe o limite
# vai digitando até que o usuário digite o zero
# é uma condição de padara / ou flag
'''
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')
'''

# outro exemplo
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar? [S/N] ')).upper()
print('Fim')
