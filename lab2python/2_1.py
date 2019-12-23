l = input('Введіть числа через пропуск: ').split()

seredne_aryfm = 0
suma = 0

for n in l:
    suma = suma + float(n)

seredne_aryfm = suma / len(l)

print('Сер арифм: ', seredne_aryfm)

for n in l:
    if float(n) < seredne_aryfm:
        print(n)
