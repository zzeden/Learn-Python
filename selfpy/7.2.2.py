def numbers_letters_count(my_str):
    numbers_counter = 0

    for c in my_str:
        if c.isdigit():
            numbers_counter += 1

    return numbers_counter, len(my_str) - numbers_counter


print(numbers_letters_count("Python 3.6.3"))
