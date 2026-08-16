def distance(strand_a, strand_b):
    strand_len = len(strand_a)

    if strand_len != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    dist = 0
    for pos in range(strand_len):
        dist += 0 if strand_b[pos] == strand_a[pos] else 1

    return dist