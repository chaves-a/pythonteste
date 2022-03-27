a = [2, 3, 4, 7]
b = a[:]  # essa situação copia os elementos sem criar uma ligação entre essas listas
b[2] = 8  # com isso, ao alterar uma, a outra não muda
print(f'Lista A: {a}')
print(f'Lista B: {b}')
