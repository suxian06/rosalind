# Wascally Wabbits
#

def rabbits(n,k):
    """Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair)."""
    F=[0]*n
    F[0] = 1
    F[1] = 1
    for i in range(2,n):
        F[i] = k*F[i-2] + F[i-1]
    return F[n-1]

if __name__ == "__main__":
    print(rabbits(40,3))
