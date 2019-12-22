a = float(input('Введіть сторону А: '))
b = float(input('Введіть сторону B: '))
c = float(input('Введіть сторону C: '))

if (a + b > c) and (b + c > a) and (b + c > a):
    print('Трикутний існує')
else:
    print('Трикутний не існує')
