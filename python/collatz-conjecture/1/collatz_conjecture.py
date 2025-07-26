def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    current = number
    steps = 0
    while current != 1:
        steps += 1
        if current % 2 == 0:
            current = current // 2
        else:
            current = 3 * current + 1
    return steps
