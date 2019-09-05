### Finding a motif in dna
#

def FindDNAmofitf(motif,ref):
    """Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s."""

    l = len(motif)
    index = []
    for i in range(len(ref)):
        if ref[i:i+l] == motif:
            index.append(i+1)

    for i in index:
        print(i,end=' ')

if __name__ == "__main__":
    FindDNAmofitf("ATAT","GATATATGCATATACTT")
