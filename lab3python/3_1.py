n = int(input('Введіть кількість іксів:'))
d = {}

def fun(dani = {}):

    print('x\ty')

    for x in dani.keys():
        print(x, '\t', dani[x], sep='')


print('Функція y = x^2')

for x in range(n):

    d[x] = x * x

fun(d)


