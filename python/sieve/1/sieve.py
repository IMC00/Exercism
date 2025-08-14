def primes(limit):
    composite_set = set()
    prime_list = []

    for num in range(2, limit+1):
        if num not in composite_set:
            prime_list.append(num)
            mult = 2
            while mult*num <= limit:
                composite_set.add(mult*num)
                mult += 1

    return prime_list
