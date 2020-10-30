BOTTLE_SIZE = 1.5

def num_of_water_bottles():
    """
    this function calculates the number of water bottles.
    required for the trip, given  a liters value.
    :param num_of_liters: total number of liters
    :type num_of_liters: float
    :return: number of water 
    :rtype: int
    """

    return int(num_of_liters / BOTTLE_SIZE)
