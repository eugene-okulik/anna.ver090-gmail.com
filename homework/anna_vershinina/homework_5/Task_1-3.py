# Task 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

name, last_name, city, phone, country = person

# Task 2
output_1 = 'результат операции: 42'
output_2 = 'результат операции: 514'
output_3 = 'результат работы программы: 9'

num_1 = int(output_1[-2:]) + 10  # did not use index
num_2 = int(
    output_2[output_2.index('514'):]
    ) + 10  # used index to find a position of '514' using slice and save it as int
num_3 = int(
    output_3[output_3.index(': ') + 2:]
    ) + 10  # used index to find a position of ':' and start the slice from the next position

print(num_1, num_2, num_3)

# Task 3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print(
    f'Students {", ".join(students)} study these subjects:'
    f' {", ".join(subjects)}'
    )
