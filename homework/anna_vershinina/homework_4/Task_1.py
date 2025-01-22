# Homework_4

my_dict = {'tuple': ('new', 5, 23, 'k', True, 5),
           'list': [1, 'to_delete', [5, 787838, {9, 0}], 7, 2],
           'dict': {'country': 'Germany',
                    'capital': 'Berlin',
                    'code': 'GR',
                    'continent': 'Europe',
                    'language': 'German'
                    },
           'set': {58, '40', 'no', True, 40, 100}
           }

# Subtask 1
print(my_dict['tuple'][-1])

# Subtask 2
my_dict['list'].append('one_more')
my_dict['list'].pop(1)
print(my_dict['list'])

# Subtask 3
my_dict['dict']['i am a tuple'] = 'added'
print(my_dict['dict'])

# Subtask 4
my_dict['set'].add(False)
my_dict['set'].discard(True)
print(my_dict['set'])
