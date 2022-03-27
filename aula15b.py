# ele explicou uma nova forma de escrever strings - veio após uma atualização do python
'''
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}')

# outros exemplos
nome = 'José'
idade = 33
print(f'O {nome} tem {idade} anos.')
print('O {} tem {} anos.'.format(nome, idade))
'''

nome = 'José'
idade = 33
salário = 987.3
print(f'O {nome:-^20} tem {idade} anos e ganha R${salário:.2f}')
