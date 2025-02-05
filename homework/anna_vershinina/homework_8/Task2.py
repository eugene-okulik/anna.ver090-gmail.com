import sys

sys.set_int_max_str_digits(1000000)  # The result for the last number is too long so this allows such a long numbers


def fibonacchi():
    num_1, num_2 = 0, 1
    while True:
        yield num_1
        num_1, num_2 = num_2, num_1 + num_2


def retrieve_num(n):
    num_gen = fibonacchi()
    for _ in range(n):
        fib_num = next(num_gen)
    return fib_num


print(retrieve_num(5))
print(retrieve_num(200))
print(retrieve_num(1000))
print(retrieve_num(100000))
