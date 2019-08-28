### Introduction to mendelian inheritance
#
def comb(n,k):
    import numpy as np
    C = (np.ones([n+1,n+1])*0).astype(np.int64)
    for i in range(n+1):
        C[i,1] = i
        C[i,i] = 1
    for i in range(2,n+1):
        for j in range(2,n+1):
            if j > i:
                break
            C[i,j] = C[i-1,j] + C[i-1,j-1]
    return C[n,k]

def Mendel1stLaw(k,m,n):
    """Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate."""
    total = k+m+n
    divid = comb(total,2)
    situ = comb(k,2)+k*m+k*n+0.75*comb(m,2)+.5*m*n
    return situ / divid

if __name__ == "__main__":
    print(Mendel1stLaw(16,19,21))
