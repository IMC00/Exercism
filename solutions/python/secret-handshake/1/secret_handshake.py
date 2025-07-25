def commands(binary_str: str):
    result = []
    items = ["jump", "close your eyes", "double blink", "wink"]
    str_as_list = list(binary_str)
    while items:
        if str_as_list.pop() == "1":
            result.append(items.pop())
        else:
            items.pop()
    return result if str_as_list.pop() == "0" else list(reversed(result))