n1 = int(input('Digite um valor: ')) # necessário colocar int pois sem ele qualquer entrada é considerada string
n2 = int(input('Digite outro valor: '))
s = n1 + n2
# print('A soma entre', n1, 'e', n2, 'vale', s)
print('A soma entre {} e {} vale {}'.format(n1, n2, s))

