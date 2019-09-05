### Counting point mutations
#

def HmmDistance(dna,ref):
    """Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t)."""
    import numpy as np
    hmm = np.sum([x != y for x,y in zip(dna,ref)])
    return hmm

if __name__ == "__main__":
    print(HmmDistance("GAGCCTACTAACGGGAT","CATCGTAATGACGGCCT"))
