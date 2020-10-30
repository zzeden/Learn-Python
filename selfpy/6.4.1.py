def check_valid_input(letter_guessed, old_letters_guessed):
    if len(letter_guessed) != 1:
        return False
    if not letter_guessed.isalpha():
        return False
    if letter_guessed in old_letters_guessed:
        return False

    return True


old_letters = ['a', 'b', 'c']
print(check_valid_input('ep', old_letters))
print(check_valid_input('$', old_letters))
print(check_valid_input('c', old_letters))
print(check_valid_input('s', old_letters))