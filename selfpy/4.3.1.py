letter = input('Guess a letter:')
length = len(letter)

if not letter.isnumeric() and not letter.isalpha() and length != 1:
    print("E3")
elif length != 1:
    print("E1")
elif not letter.isnumeric() and not letter.isalpha():
    print('E2')
else:
    print(letter.lower())



