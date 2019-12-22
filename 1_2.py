c = float(input('Введіть температуру у гр. Цельсія: '))

k = c + 273.15
f = c * 1.8 + 32
r = 0.8 * c

print('K: ', round(k, 2))
print('F: ', round(f, 2))
print('Ré: ', round(r, 2))
