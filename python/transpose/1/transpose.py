def transpose(text : str):
    lines = text.split("\n")
    line_len = {idx: len(line) for idx, line in enumerate(lines)}

    max_len = max(line_len.values())

    result = [[] for _ in range(max_len)]
    for idx, line in enumerate(lines):
        len_idx = len(line)
        for jdx in range(max_len):
            if jdx < len_idx:
                result[jdx].append(line[jdx])
            else:
                result[jdx].append(None)

    ## Triming lines
    for line in result:
        is_none_tail = True
        for idx in range(len(line)-1, -1, -1):
            if is_none_tail:
                if line[idx] is not None:
                    is_none_tail = False
                else:
                    line.pop()
            elif line[idx] is None:
                line[idx] = ' '


    return "\n".join(["".join(line) for line in result])



