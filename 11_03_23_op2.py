import random 
def get_sorted_unique_numbers(min, max, quantity):
    """
    Generate a specified quantity of unique random numbers within a given range, sorted in ascending order.
    If parameters do not meet the specified constraints, return an empty list.
    
    Parameters:
    - min (int): The minimum possible number in the set (at least 1).
    - max (int): The maximum possible number in the set (no more than 1000).
    - quantity (int): The number of numbers to select (between min and max).
    
    Returns:
    - list: A list of randomly selected, sorted numbers. The numbers in the set do not repeat.
    """
    if min < 1 or max > 1000 or quantity < 0 or max - min + 1 < quantity:
        return []

    random_numbers = random.sample(range(min, max + 1), quantity)
    random_numbers.sort()
    return random_numbers

test_numbers = get_sorted_unique_numbers(1, 100, 5)
test_numbers
