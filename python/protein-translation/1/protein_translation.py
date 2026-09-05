RNA_TO_CODON = {
    'AUG': "Methionine",
    'UUU': "Phenylalanine",
    'UUC': "Phenylalanine",
    'UUA': "Leucine",
    'UUG': "Leucine",
    'UCU': "Serine",
    'UCC': "Serine",
    'UCA': "Serine",
    'UCG': "Serine",
    'UAU': "Tyrosine",
    'UAC': "Tyrosine",
    'UGU': "Cysteine",
    'UGC': "Cysteine",
    'UGG': "Tryptophan",
    'UAA': None,
    'UAG': None,
    'UGA': None,
    ''   : None
}

def proteins(strand):
    amino = RNA_TO_CODON[strand[:3]]
    remaining_strand = strand[3:]
    result = []

    while amino:
        result.append(amino)
        amino = RNA_TO_CODON[remaining_strand[:3]]
        remaining_strand = remaining_strand[3:]

    return result