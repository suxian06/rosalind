### The secondary and teritary structures of dna
###

def ReversDNA(dna):
    """Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s."""
    complement = {"T":"A","G":"C","C":"G","A":"T"}
    cdna = ""
    for i in range(len(dna)-1,-1,-1):
        cdna+=complement[dna[i]]
    return cdna

if __name__ == "__main__":
    print(ReversDNA("AAAACCCGGT"))
