'''
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(sorted(lanche)) # mostra o lanche em ordem
print(lanche) # veja que a tupla não mudou com o sorted
'''

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a # cria a tupla c
print(a)
print(b)
print(c)
print(len(c))
print(c.count(5)) # quantas vezes aparece o número 5
print(c.index(8)) # em que posição está o 8
print(c.index(2)) # ele pega a primeira ocorrência
print(c.index(5, 1)) # a partir da posição 1 ele pega a primeira ocorrência
