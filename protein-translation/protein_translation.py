def proteins(strand):
    PROTEIN_DICT = { 'AUG': 'Methionine',
                     'UUU': 'Phenylalanine',
                     'UUC': 'Phenylalanine',
                     'UUA': 'Leucine',
                     'UUG': 'Leucine',
                     'UCU': 'Serine',
                     'UCC': 'Serine',
                     'UCA': 'Serine',
                     'UCG': 'Serine',
                     'UAU': 'Tyrosine',
                     'UAC': 'Tyrosine',
                     'UGU': 'Cysteine',
                     'UGC': 'Cysteine',
                     'UGG': 'Tryptophan',
                     'UAA': 'STOP',
                     'UAG': 'STOP',
                     'UGA': 'STOP' }

    rna_list = [''.join(x) for x in zip(*[list(strand[z::3]) for z in range(3)])]
    protein_list = []
    for rna in rna_list:
        if PROTEIN_DICT[rna] == 'STOP':
            return protein_list
        else:
            protein_list.append(PROTEIN_DICT[rna])

    return protein_list
