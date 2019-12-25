n = 9

r = []

for i in range(n):
    r.append('a' * (i+1) + '\n')

f = open('file.txt', 'w')
f.writelines(r)
f.close()

print('Результат записано в файл file.txt')

