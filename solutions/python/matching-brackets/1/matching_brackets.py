def is_paired(input_string):
    queue = []
    OPENING = ["(", "[", "{"]
    CLOSING = [")", "]", "}"]
    for char in input_string:
        if char in OPENING:
            queue.append(char)
        elif char in CLOSING:
            if not queue: return False
            last_queued = queue.pop()
            if char == ")" and last_queued != "(":
                return False
            if char == "]" and last_queued != "[":
                return False
            if char == "}" and last_queued != "{":
                return False
    return queue == []

