def sum_of_multiples(limit, multiples):
    result_sets = []
    for element in multiples:
        if element <= 0:
            continue
        cur_set = set()
        multiple = element
        while multiple < limit:
            cur_set.add(multiple)
            multiple += element
        result_sets.append(cur_set)
    points = sum(set().union(*result_sets))
    return points

