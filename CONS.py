### Consensus and Profile
#

import numpy as np

def ConsensusProfile(seq):
    dim = len(seq[0])
    Profile = {"A":[0]*dim,
               "C":[0]*dim,
               "G":[0]*dim,
               "T":[0]*dim}
    for s in seq:
        for base,pos in zip(s,range(dim)):
            Profile[base][pos]+=1
    return Profile

def ConsensusStr(Profile):
    #keys = Profile.keys()
    dim = len(Profile["A"])
    indexlist = ["A","C","G","T"]
    consensus = ""
    for pos in range(dim):
        comp=[Profile["A"][pos],
               Profile["C"][pos],
               Profile["G"][pos],
               Profile["T"][pos]]
        consensus+=indexlist[np.argmax(comp)]
    return consensus

def main():
    allfiles = """>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT""".split("\n")

    header,seq = allfiles[0::2],allfiles[1::2]
    conProfile = ConsensusProfile(seq)
    conStr = ConsensusStr(conProfile)

    for x in conProfile.keys():
        print(str(x)+": "+" ".join([str(x) for x in conProfile[x]]))
    print(conStr)
if __name__ == '__main__':
    main()
