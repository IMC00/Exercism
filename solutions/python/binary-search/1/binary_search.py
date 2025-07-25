def find(search_list, value):
    if not search_list:
        raise ValueError("value not in array")

    size = len(search_list)

    left_index = 0
    right_index = size

    mid = (left_index + right_index) // 2

    while search_list[mid] != value:
        if search_list[mid] > value:
            right_index = mid
        else:
            left_index = mid + 1

        mid = (left_index + right_index) // 2
        if right_index <= left_index or mid >= size: break
    else:
        return mid

    raise ValueError("value not in array")
