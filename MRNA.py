### Inferring mRNA from Protein
#

def ReversTranslate(aa):
    """Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)"""
    rna_codon = {"UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V",
               "UUC" : "F", "CUC" : "L", "AUC" : "I", "GUC" : "V",
               "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V",
               "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V",
               "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A",
               "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
               "UCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
               "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
               "UAU" : "Y", "CAU" : "H", "AAU" : "N", "GAU" : "D",
               "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
               "UAA" : "STOP", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
               "UAG" : "STOP", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
               "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G",
               "UGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
               "UGA" : "STOP", "CGA" : "R", "AGA" : "R", "GGA" : "G",
               "UGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G"
               }
    n = len(aa)
    mult = 1
    for i in range(n):
        mult *= len([ k for k ,v in rna_codon.items() if v == aa[i]])
    return mult*3 % 1000000 #modular arithmic

if __name__ == "__main__":
    with open("D:/Downloads/rosalind_mrna.txt") as f:
        r = f.read()
    r = r.replace("\n","")
    print(ReversTranslate(r))
