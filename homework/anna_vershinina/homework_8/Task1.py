import random

salary = int(input('Type a salary: '))
bonus = random.choice([True, False])

bonus_amount = random.randint(100, 1000) if bonus else 0
total_salary = salary + bonus_amount

print(f"{salary}, {bonus} - '${total_salary}'")
