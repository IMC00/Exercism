def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1: raise ValueError("Classification is only possible for positive integers.")

    start = number // 2
    sum_factors = 0
    while start > 0:
        if number % start == 0:
            sum_factors += start
        start -= 1
        if sum_factors > number: return "abundant"

    if sum_factors == number: return "perfect"
    return "deficient"