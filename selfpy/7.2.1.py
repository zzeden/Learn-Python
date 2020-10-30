def is_greater(my_list, n):
    result = []
    for x in my_list:
        if x > n:
           result.append(x)
    return result

result = is_greater([1, 30, 25, 60, 27, 28], 28)
print(result)
