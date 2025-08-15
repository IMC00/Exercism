def triplets_with_sum(number):
    # print()
    result = list()
    for b in range(1, number):
        if b > number - b:
            break
        for a in range(1, b):
            c = number - a - b
            if a**2 + b**2 == c ** 2:
                result.append([a,b,c])
    # print(result)
    return list(result)
