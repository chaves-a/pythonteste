# Um while infinito que quando digitar o 999 vai para o break sem somar o 999
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))
