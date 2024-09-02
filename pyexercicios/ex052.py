n = int(input('Digite um número: '))
tot = 0

for i in range(1, n+1):
    if n % i == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[m', end='')
    print(i, end=' ')


print('\n\033[mo numero {} foi divisivel {} vezes'.format(n, tot))
if tot == 2:
    print('Esse número é primo')
else:
    print('Esse número não é primo')