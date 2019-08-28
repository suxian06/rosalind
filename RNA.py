### code for transcribing DNA into RNA
###
def readfile(Dir):
    f = open(Dir)
    r = f.read()
    f.close()
    return r

def TranscribDNA(dna):
    """Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t."""
    dna = dna.replace("T","U")
    return dna

if __name__ == "__main__":
    print(TranscribDNA("GATGGAACTTGACTACGTAAATT"))
