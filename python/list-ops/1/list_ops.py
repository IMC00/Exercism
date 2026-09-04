from functools import reduce


def append(list1, list2):
    return list1 + list2


def concat(lists):
    return reduce(append, lists, [])


def filter(function, list):
    return [elem for elem in list if function(elem)]


def length(list):
    total = 0
    for elem in list:
        total += 1
    return total

def map(function, list):
    result = []
    for elem in list:
        result.append(function(elem))
    return result


def foldl(function, list, initial):
    result = initial
    for elem in list:
        result = function(result, elem)
    return result


def foldr(function, list, initial):
    return foldl(function, reversed(list), initial)


def reverse(list):
    return list[::-1]
