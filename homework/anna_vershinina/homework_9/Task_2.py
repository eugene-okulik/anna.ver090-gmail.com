temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22,
    22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]

hot_days_1 = list(filter(lambda t: t > 28, temperatures))
print("The highest temperature is", max(hot_days_1))
print("The lowest temperature is", min(hot_days_1))

avg_temp = round((sum(hot_days_1) / len(hot_days_1)), 1)
print("The average temperature is", avg_temp)
