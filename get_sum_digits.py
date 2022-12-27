def get_sum_digits(num):
    """
    A integer is given. Return the sum of digits in it.
    
    Args:
        num (int): an integer value
    
    Returns:
        int: the sum of digits
    """
    sum=0
    for digit in str(num):
        sum+=int(digit)
    # return sum of digits in integer
    return  sum
#print(get_sum_digits(23243))
