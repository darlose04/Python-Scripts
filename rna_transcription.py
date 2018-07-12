'''
def to_rna(dna_strand):

    rnaList = []

    for char in dna_strand:
        if char == 'G':
            rnaList.append('C')
        elif char == 'C':
            rnaList.append('G')
        elif char == 'T':
            rnaList.append('A')
        elif char == 'A':
            rnaList.append('U')
        else:
            print('Invalid character!')

    return ''.join(rnaList)
'''


# redo with a dictionary

def to_rna(dna_strand):

    dna_to_rna = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

    rna = ''

    for char in dna_strand:
        if char not in dna_to_rna:
            raise ValueError('Invalid character!')
        rna += dna_to_rna[char]
    return rna


print(to_rna('GCTA'))
