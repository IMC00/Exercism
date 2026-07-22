def proverb(*args, qualifier=None):
    if not args:
        return []

    first_elem, *arguments = args

    result = []
    item_2 = first_elem
    while arguments:
        item_1, item_2, *arguments = item_2, *arguments
        result.append(f"For want of a {item_1} the {item_2} was lost.")

    result.append(f"And all for the want of a {qualifier + ' ' if qualifier else ''}{first_elem}.")

    return result
