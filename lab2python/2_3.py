movu = {
    'ua': 'українська',
    'ru': 'російська',
    'pl': 'польська',
    'de': 'німецька',
    'en': 'англійська',
}

uchni = {
    'ivan': ['ua', 'ru', 'en'],
    'ruslan': ['ua', 'ru', 'en'],
    'olexander': ['ua', 'ru'],
    'anastassia': ['ua', 'ru'],
    'victoria': ['ua', 'ru'],
    'alina': ['ua', 'ru', 'de'],
    'igor': ['ua', 'ru', 'de', 'pl'],
    'petro': ['ua', 'ru', 'de'],
    'volodymyr': ['ua', 'ru', 'en'],
    'julia': ['ua']
}

kilkist_mov = 0
name = ''

for uchen in uchni:
    print(uchen, ' знає такі мови: ', end=' ')

    if len(uchni[uchen]) > kilkist_mov:
        kilkist_mov = len(uchni[uchen])
        name = uchen

    for mova in uchni[uchen]:
        print(movu[mova], end=' ')
    print()

print()
print('Найбільше мов знає ', name, ' - ', kilkist_mov)