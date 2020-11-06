def seven_boom(end_number):
    listy = []
    for i in range(0, end_number):
        if i % 7 == 0 or "7" in str(i) :
            listy.append("BOOM")
        else:
            listy.append(i)

    return listy


print(seven_boom(19))
