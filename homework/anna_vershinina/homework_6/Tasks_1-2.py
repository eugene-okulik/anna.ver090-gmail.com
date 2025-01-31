# Task 1
text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
        "Integer urna nisl, facilisis vitae semper at, "
        "dignissim vitae libero")

words = text.split()
new_words = []

for word in words:
    punctuation = ""

    if word[-1] in ".,":
        punctuation = word[-1]
        word = word[:-1]

    word = word + 'ing'
    new_words.append(word + punctuation)

new_text = " ".join(new_words)
print(new_text)


# Task 2
for i in range(1, 101):
    if (i % 5 == 0) and (i % 3 == 0):
        print('FuzzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fuzz')
    else:
        print(i)
