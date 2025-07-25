def annotate(garden):
    if not garden:
        return []
    height = len(garden)
    width = len(garden[0])
    result = []
    for i, line in enumerate(garden):
        new_line = []
        if len(line) != height:
            raise ValueError("The board is invalid with current input.")
        for j, elem in enumerate(line):
            if elem == '*':
                new_line.append(elem)
                continue
            if elem != ' ':
                raise ValueError("The board is invalid with current input.")
            local_i = i - 2
            count = 0
            for _ in range(3):
                local_i += 1
                local_j = j - 2
                if local_i < 0 or local_i >= height:
                    continue
                for _ in range(3):
                    local_j += 1
                    if local_j < 0 or local_j >= width:
                        continue
                    if garden[local_i][local_j] == '*':
                        count += 1
            new_line.append(' ' if count == 0 else str(count))
        result.append(''.join(new_line))
    return result

    pass
