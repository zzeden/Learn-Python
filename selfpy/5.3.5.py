def distance(num1, num2, num3):
    if ((abs(num2 - num1) == 1) or (abs(num3 - num1) == 1)):
        print("true")
    else:
        print("false")


distance(1, 2, 10)  # true
distance(4, 5, 3)  # false
