### code for counting DNA nucleotides
###
def readfile(Dir):
    f = open(Dir)
    r = f.read()
    f.close()
    return r

def CountDNA(dna):
    """Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s."""
    A = dna.count("A")
    C = dna.count("C")
    G = dna.count("G")
    T = dna.count("T")
    print(str(A)+' '+str(C)+' '+str(G)+' '+str(T))

if __name__ == "__main__":
    r = readfile("D:/Downloads/rosalind_dna.txt")
    CountDNA(r)
