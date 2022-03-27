galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])
print('-=' * 20)
for p in galera:
    print(p)
print('-=' * 20)
for p in galera:
    print(p[0])
print('-=' * 20)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')