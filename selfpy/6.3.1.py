def are_lists_equal(list1, list2):
    list2 = list2.sort()
    list1 = list1.sort()
    if list1 == list2:
        print("true")

    else:
        print("false")
are_lists_equal([5, 6, 7], [6, 5, 7])