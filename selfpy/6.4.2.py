def check_valid_input(letter_guessed, old_letters_guessed):
    if len(letter_guessed) != 1:
        return False
    if not letter_guessed.isalpha():
        return False
    if letter_guessed in old_letters_guessed:
        return False

    return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    answer = check_valid_input(letter_guessed, old_letters_guessed)
    if answer == True:
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X")
        msort = sorted(old_letters_guessed)
        print(msort)
        string = ""
        for s in old_letters_guessed:
            string += s
            string += " -> "
        print(string[:-3])
        return False

old_letters = ['a', 'p', 'c', 'f']
print(try_update_letter_guessed('f', old_letters))

