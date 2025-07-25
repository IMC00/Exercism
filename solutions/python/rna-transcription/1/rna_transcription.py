def to_rna(dna_strand):
    translation = {
        "C" : "G",
        "G" : "C",
        "T" : "A",
        "A" : "U",
    }

    result = []
    for char in dna_strand:
        result.append(translation[char])
    return "".join(result)
