def extend_list_x(list_x, list_y):
    for x in list_x:
        list_y.append(x)

x = [4, 5, 6]
y = [1, 2, 3]
extend_list_x(x, y)
print(y)
