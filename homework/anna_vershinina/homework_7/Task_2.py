"""
The most obvious solution from my perspective was the one without functions
"""
words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for i in words:
    print(i * words[i])

"""
The solution with a function and with a different key-value extraction method
"""

def print_dict(my_dict):
    for key, value in my_dict.items():
        print(key * value)

words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

print_dict(words)