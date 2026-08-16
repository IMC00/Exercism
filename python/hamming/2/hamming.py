def distance(strand_a, strand_b):
    strand_len = len(strand_a)

    if strand_len != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    dist = 0
    for nucleotide_a, nucleotide_b in zip(strand_a, strand_b):
        dist += 0 if nucleotide_a == nucleotide_b else 1

    return dist