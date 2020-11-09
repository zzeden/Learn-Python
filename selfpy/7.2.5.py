def sequence_del(my_str):
    listy = []
    listy.append(my_str[0])

    for s in my_str:
        if listy[-1] != s:
            listy.append(s)
    return listy


print(sequence_del("ppyyyyythhhhhooonnnnn"))

print('u' in 'trtreewefggg')
print(66 in [55, 77, 88, 99, 66, 55])
