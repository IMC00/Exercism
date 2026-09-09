from math import sqrt


def factors(value):
    result = []
    current_value = value
    current_test = 2
    print()
    while current_test <= current_value:
        print(current_test, current_value, value % current_test == 0)
        if current_value % current_test == 0:
            result.append(current_test)
            current_value //= current_test
        else:
            current_test += 1 if current_test == 2 else 2
    return result
