a = [2, 3, 4, 7]
b = a  # essa situação cria uma ligação entre essas listas
b[2] = 8  # com isso, ao alterar uma, a outra também muda
print(f'Lista A: {a}')
print(f'Lista B: {b}')
