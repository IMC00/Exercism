def flatten(iterable):
    result = []
    for elem in iterable:
        if isinstance(elem, list):
            result.extend(flatten(elem))
        elif elem is not None:
            result.append(elem)
    return result
