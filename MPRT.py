### Find a protein motif
#
mass_table = """A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333 """.split('\n')
mass_table = [ x.split("   ") for x in mass_table]
mass_dict = {}

all_aa = list(mass_dict.keys()) #list of all amino acid

def FindProteinMotif(protein_list):
    """Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found."""

    import urllib
    N_glycosylation = ["N"+ x + y + z for x in all_aa for y in ["S","T"] for z in all_aa if (x != "P") and (z != "P")]

    for x in protein_list:
        f = urllib.request.urlopen("https://www.uniprot.org/uniprot/"+str(x)+".fasta")
        f = f.read().decode("utf-8")
        seq = "".join(f.split("\n")[1:])
        name, pos = x, []
        for x in N_glycosylation:
            try:
                pos.append(str(seq.index(x)+1))
            except ValueError:
                continue
        if pos != []:
            print(name)
            print(" ".join(pos))

if __name__ == '__main__':
    testProteinList = tmp = """A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST""".split("\n")
    FindProteinMotif(testProteinList)
