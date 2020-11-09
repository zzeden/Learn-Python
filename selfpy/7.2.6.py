def main_fun():
    products = input("pls write a shoping list: ")
    number = input("write a number 1 -9: ")
    if number == "1":
        print(products)
    elif number == "2":
        print(products.count(",") + 1)


main_fun()
