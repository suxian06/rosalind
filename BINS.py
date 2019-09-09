#  Binary Search
#  Given Given: Two positive integers n≤105 and m≤105, a sorted array A[1..n] of integers from −105 to 105 and a list of m integers −105≤k1,k2,…,km≤105.
#  Return: For each ki, output an index 1≤j≤n s.t. A[j]=ki or "-1" if there is no such index.

def Bsearch(A,k):

    m = int(len(A)/2)
    right = len(A) - 1
    left = 0

    while True:

        if k == A[m]:
            return m + 1

        if k < A[m]:
            right = m

        elif k > A[m]:
            left = m + 1

        m = int((left + right)/2)

        if left >= right:
            return -1

if __name__ == "__main__":

    A=[ int(x) for x in """10 20 30 40 50""".split(" ")]
    k=[ int(x) for x in """40 10 35 15 40 20""".split(" ")]

    l = []
    for i in range(0,len(k)):
        l.append(Bsearch(A,k[i]))
    print(l)
