def last_early(my_str):
    length = len(my_str)
    last_latter = my_str[length-1]
    if last_latter in my_str[:length-2]:
        print("true")
    else:
        print("false")

last_early("55")