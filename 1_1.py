import math

# h = 10.9
# v = 363.33

h = float(input('Введіть висоту піраміди: '))
v = float(input('Введіть об\'єм піраміди: '))

S_osnovy = v / (1/3*h)

print('Площа основи: ', S_osnovy)

a = math.sqrt(S_osnovy)
x = a / 2

print('Сторона основи: ', a)

l = math.sqrt(x*x + h*h)

print('Висота трикутника: ', l)

S_bich_trykutnuka = 0.5 * a * l

print()
print('Площа бічної поверхні: ', round(S_bich_trykutnuka, 3))
