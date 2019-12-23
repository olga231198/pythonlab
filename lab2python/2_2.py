n = int(input('Введіть n: '))

x = []
for i in range(n):
    numbers = input('Введіть {} чисел(ла), {} рядка через пробіл: '.format(n, i + 1))
    x.append(numbers.split())

print()

sym = True

for k in range(0, n - 1):
    for l in range(k + 1, n):
        if (x[k][l] != x[l][k]):
            sym = False
            break

if sym:
    print('Список симетричний відносно головної діагоналі')
else:
    print('Список не симетричний відносно головної діагоналі')
