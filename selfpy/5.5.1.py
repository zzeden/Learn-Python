def is_valid_input(letter_guessed):
    length = len(letter_guessed)
    if length != 1:
        return False
    if not letter_guessed.isalpha():
        return False
    return True

print( is_valid_input('app$'))