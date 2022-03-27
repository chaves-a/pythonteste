lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche[2]) # explorando os elementos

print(len(lanche)) # tamanho da tupla

for comida in lanche: # laço com itens utilizando diretamente a variável composta
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!\n')

for cont in range(0, len(lanche)): # outra forma de fazer o laço utilizando o range
    print(f'Eu vou comer {lanche[cont]} na posição {cont}') # ele vai iterar e, a cada vez, ele vai imprimir o lanche na posição cont
print('Comi pra caramba!\n')

# uma forma de usar o primeiro for acima e mostrar a posição é:
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!\n')
