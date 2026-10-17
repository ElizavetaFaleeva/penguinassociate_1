def find_two_smallest(numbers):
    """Return the two smallest integers from a list.
    
    Args:
        numbers: A list of integers.
        
    Returns:
        A tuple containing the two smallest values.
    """

    sorted_numbers = sorted(numbers)
    return sorted_numbers[0], sorted_numbers[1]
