### Open Reading Frames
#

def ReversDNA(dna):
    complement = {"T":"A","G":"C","C":"G","A":"T"}
    cdna = ""
    for i in range(len(dna)-1,-1,-1):
        cdna+=complement[dna[i]]
    return cdna

def TranscribDNA(dna):
    dna = dna.replace("T","U")
    return dna

def Translation(rna):
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
    protein = ""
    for i in range(0,len(rna),3):
        stop = False
        if i+3 < len(rna):
            peptide = rna_codon[rna[i:i+3]]
            if peptide == "STOP":
                stop = True
                break
            protein += peptide
    if stop == True:
        return protein

def OpenReadingFrames(dna):
    rev = ReversDNA(dna)
    rna1 = TranscribDNA(dna)
    rna2 = TranscribDNA(rev)
    start_coden = "AUG"
    ORFS = []
    for i in range(3):
        rna = rna1[i:]
        for j in range(0,len(rna),3):
            if rna[j:j+3] == start_coden:
                ORFS.append(Translation(rna[j:]))
                #break
    for i in range(3):
        rna = rna2[i:]
        for j in range(0,len(rna),3):
            if rna[j:j+3] == start_coden:
                ORFS.append(Translation(rna[j:]))
                #break
    return set(ORFS)

if __name__ == '__main__':
    dna = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
    print(OpenReadingFrames(dna))
