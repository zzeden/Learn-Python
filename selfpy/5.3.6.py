def filter_teens(a=13, b=13, c=13):
    a = fix_age(a)
    b = fix_age(b)
    c = fix_age(c)

    ageSum = a + b + c
    return ageSum
def fix_age(age):
    if age == 13 or age == 14 or age == 17 or age == 18 or age == 19:
        age = 0
    return age

print (filter_teens())

print (filter_teens(1, 2, 3))

print (filter_teens(2, 13, 1))

print (filter_teens(2, 1, 15))

