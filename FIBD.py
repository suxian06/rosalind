### Mortal Fibonacci Rabbits
#

def MortalFB(n,m):
    """
    Given: Positive integers n≤100 and m≤20.

    Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
    """
    if m == 1:
        return 0
    if m == 2:
        return 1

    F = [1]*n
    for i in range(2,n):
        if i < m:
            F[i] = F[i-1]+F[i-2]
        else:
            F[i] = F[i-1]+F[i-2]-F[i-m-1] # F[-1] = 1
    return F[n-1]

if __name__ == "__main__":
    print(MortalFB(96,20))
