def guess_the_number(correct_num):
    while True:
        user_number = int(input('Введите цифру: '))
        if user_number == correct_num:
            print('Поздравляю! Вы угадали!')
            break
        else:
            print('Попробуйте снова')

number = 1
guess_the_number(number)
