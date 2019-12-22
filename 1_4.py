import random

user_win = 0
computer_win = 0

a = int(input('Ваш хід: (1 - камінь, 2 - ножниці, 3 - папір): '))
computer_choice = random.randint(1, 3)
if a == computer_choice:
    print('Нічия')
elif a == 1 and computer_choice == 2:
    print('Ви виграли!, компютер вибрав ножниці')
    user_win = user_win + 1
elif a == 1 and computer_choice == 3:
    print('Ви програли, компютер вибрав папір')
    computer_win = computer_win + 1
elif a == 2 and computer_choice == 1:
    print('Ви програли, компютер вибрав камінь')
    computer_win = computer_win + 1
elif a == 2 and computer_choice == 3:
    print('Ви виграли!, компютер вибрав папір')
    user_win = user_win + 1
elif a == 3 and computer_choice == 1:
    print('Ви виграли!, компютер вибрав камінь')
    user_win = user_win + 1
elif a == 3 and computer_choice == 2:
    print('Ви програли, компютер вибрав ножниці')
    computer_win = computer_win + 1


a = int(input('Ваш хід: (1 - камінь, 2 - ножниці, 3 - папір): '))
computer_choice = random.randint(1, 3)
if a == computer_choice:
    print('Нічия')
elif a == 1 and computer_choice == 2:
    print('Ви виграли!, компютер вибрав ножниці')
    user_win = user_win + 1
elif a == 1 and computer_choice == 3:
    print('Ви програли, компютер вибрав папір')
    computer_win = computer_win + 1
elif a == 2 and computer_choice == 1:
    print('Ви програли, компютер вибрав камінь')
    computer_win = computer_win + 1
elif a == 2 and computer_choice == 3:
    print('Ви виграли!, компютер вибрав папір')
    user_win = user_win + 1
elif a == 3 and computer_choice == 1:
    print('Ви виграли!, компютер вибрав камінь')
    user_win = user_win + 1
elif a == 3 and computer_choice == 2:
    print('Ви програли, компютер вибрав ножниці')
    computer_win = computer_win + 1

a = int(input('Ваш хід: (1 - камінь, 2 - ножниці, 3 - папір): '))
computer_choice = random.randint(1, 3)
if a == computer_choice:
    print('Нічия')
elif a == 1 and computer_choice == 2:
    print('Ви виграли!, компютер вибрав ножниці')
    user_win = user_win + 1
elif a == 1 and computer_choice == 3:
    print('Ви програли, компютер вибрав папір')
    computer_win = computer_win + 1
elif a == 2 and computer_choice == 1:
    print('Ви програли, компютер вибрав камінь')
    computer_win = computer_win + 1
elif a == 2 and computer_choice == 3:
    print('Ви виграли!, компютер вибрав папір')
    user_win = user_win + 1
elif a == 3 and computer_choice == 1:
    print('Ви виграли!, компютер вибрав камінь')
    user_win = user_win + 1
elif a == 3 and computer_choice == 2:
    print('Ви програли, компютер вибрав ножниці')
    computer_win = computer_win + 1

print()
if computer_win == user_win:
    print('Ви класно грали, але і компютер нічого так - нічия')
if computer_win > user_win:
    print('желєзяка виграв')
if user_win > computer_win:
    print('Ваша взяла!')