def additional_operation(func):

    def wrapper(num_1, num_2):
        if num_1 == num_2:
            operator = '+'
        elif num_1 > num_2:
            operator = '-'
        elif num_1 < num_2:
            operator = '/'
        elif num_1 < 0 or num_2 < 0:
            operator = '*'
        else:
            return 'Invalid arguments were passed'
        return func(num_1, num_2, operator)

    return wrapper


@additional_operation
def calc(first, second, operator):
    if operator == '+':
        return f'The summ is {first + second}'
    elif operator == '-':
        return f'The difference is {first - second}'
    elif operator == '/':
        return f'The quotient is {first / second}'
    elif operator == '*':
        return f'The product is {first * second}'
    else:
        return 'Not an operator'


num_1, num_2 = (float(input('Type the first number: ')),
                float(input('Type the second number: ')),)


result = calc(num_1, num_2)
print(result)
