def format_list(my_list):
    xo = my_list[::2] 
    x = ", ".join(xo)
    return x + ", and " + my_list[-1]


my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
print(format_list(my_list))
