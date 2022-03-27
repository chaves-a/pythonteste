# nome = input('Qual é seu nome? ')
# print('Prazer em te conhecer, {:20}!'.format(nome))
# print('Prazer em te conhecer, {:<20}!'.format(nome))
# print('Prazer em te conhecer, {:>20}!'.format(nome))
# print('Prazer em te conhecer, {:^20}!'.format(nome))
# print('Prazer em te conhecer, {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' >>> ') # O end junta os prints. Para quebrar linha bota \n dentro da string. O :.3f limita o número de casas.
print('Divisão inteira é {} e potência {}'.format(di, e))