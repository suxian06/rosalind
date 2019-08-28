### Independent Alleles
#

def comb(n,k):
    import numpy as np
    C = (np.ones([n+1,n+1])*0).astype(np.int)
    for i in range(n+1):
        C[i,1] = i
        C[i,i] = 1
    for i in range(2,n+1):
        for j in range(2,n+1):
            if j > i:
                break
            C[i,j] = C[i-1,j] + C[i-1,j-1]
    return C[n,k]

def IndependentAlleles(k,N):

    """Given: Two positive integers k (k≤7) and N (N≤2^k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.

    Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors."""

    # Mendel's Second Law
    p = .25
    q = .75
    total = 2**k
    out = 0
    for i in range(N):
        out += comb(total,i)*p**i*q**(total-i)

    return 1 - out

if __name__ == "__main__":
    IndependentAlleles(5,8)
