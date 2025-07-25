def square(number):
    return 2 ** (number - 1) if number in range(1, 65) else (_ for _ in ()).throw(ValueError("square must be between 1 and 64"))


def total():
    return 2 ** 64 - 1
