def calculate(outputs):
    for output in outputs:
        calc_num = int(output.split(':')[-1]) + 10
        print(calc_num)


output_1 = 'результат операции: 42'
output_2 = 'результат операции: 54'
output_3 = 'результат работы программы: 209'
output_4 = 'результат: 2'

program_putput = (output_1, output_2, output_3, output_4)

calculate(program_putput)
