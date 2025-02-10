def repeat_me(func):

    def wrapper(*args, **kwargs):
        num = kwargs.pop('count', 1)
        for _ in range(num):
            result = [func(*args, **kwargs) for _ in range(num)]
            return result

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=6)
