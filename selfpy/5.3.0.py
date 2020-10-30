def amount_of_oranges(small_cups=20, large_cups=10):
    oranges_result = small_cups + large_cups * 3
    kg_result = oranges_result / 5
    print("today you'll need", oranges_result, "oranges")
    print("buy", kg_result, "kg of oranges")



amount_of_oranges(3,4)


