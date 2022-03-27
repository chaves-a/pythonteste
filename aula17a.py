num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
num.remove(2) # remove a primeira ocorrência do 2
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
print(num)
print(f'Essa list tem {len(num)} elementos.')
