# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3

def is_sublist(list_one, list_two):
    if not list_one:  # An empty list is a sublist of any list
        return True
    i = 0
    while i <= len(list_two) - len(list_one):
        j = 0
        while j < len(list_one) and list_one[j] == list_two[i + j]:
            j += 1
        if j == len(list_one):  # Full match found
            return True
        i += 1
    return False

def sublist(list_one, list_two):
    l1 = len(list_one)
    l2 = len(list_two)

    if not list_one and not list_two:  # Both lists are empty
        return EQUAL
    elif not list_one:  # Empty list is always a sublist
        return SUBLIST
    elif not list_two:  # Non-empty list can't be a sublist of an empty list
        return SUPERLIST

    if l1 > l2:
        is_subset = is_sublist(list_two, list_one)
        if is_subset:
            return SUPERLIST
        else:
            return UNEQUAL
    else:
        is_subset = is_sublist(list_one, list_two)
        if is_subset:
            if l1 == l2:
                return EQUAL
            else:
                return SUBLIST
        else:
            return UNEQUAL
