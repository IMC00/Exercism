EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(layers):
    """
    Calculate the preparation time in minutes.

    This function computes the preparation time based on the number of
    layers, assuming that each layer requires a specific amount of
    preparation time.

    :param layers: The number of layers to prepare.
    :type layers: int
    :return: The total preparation time in minutes.
    :rtype: int
    """
    return layers * 2

def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """
    Calculate the total elapsed time in minutes for baking a lasagna.

    The function computes the total time spent in preparation and baking
    together. It requires the number of lasagna layers to calculate the
    preparation time and adds it to the time already spent baking.

    :param layers: The number of lasagna layers.
    :type layers: int
    :param elapsed_bake_time: The elapsed baking time in minutes.
    :type elapsed_bake_time: int
    :return: The total elapsed time in minutes.
    :rtype: int
    """
    return preparation_time_in_minutes(layers) + elapsed_bake_time
