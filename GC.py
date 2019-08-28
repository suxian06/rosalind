# Computing GC Content
#

def GCcontent(dna):
    """Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below."""
    import numpy as np
    count = dna.count("G")+dna.count("C")
    percent = count/np.float(len(dna))
    return percent

if __name__ == "__main__":
    Dir = "D:/Downloads/rosalind_gc.txt"
    with open(Dir) as f:
        r = f.read()
    allstr = r.split(">")[1:]
    allindex = [x.split("\n")[0] for x in allstr]
    alllist=[]
    for i in range(len(allstr)):
        alllist.append(GCcontent("".join(allstr[i].split("\n")[1:])))
    return_index = np.argmax(alllist)
    return_id = allindex[return_index]
    return_percent = alllist[return_index]*100
    print(return_id)
    print(return_percent)
