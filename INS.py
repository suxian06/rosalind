# Insertion Sort
# Given: A positive integer n≤103 and an array A[1..n] of integers.
# Return: The number of swaps performed by insertion sort algorithm on A[1..n].

def InSort(A,n):
    Asort = A.copy()
    swap = 0
    for i in range(1,n):
        k = A[i]
        j = i-1
        while j >= 0:
            if k < Asort[j]:
                swap += 1
                Asort[j+1] = Asort[j]
                Asort[j] = k
                j -= 1
            else:
                j -= 1
    return swap,Asort

def readrosalindfile(Dir):
    f = open(Dir)
    t = f.read()
    f.close()
    t = t.split("\n")
    return t

def main():
    t = readrosalindfile("/Users/suxian/rosalind.file/rosalind_ins.txt")
    A=[ int(x) for x in t[1].split(' ')]
    n = int(t[0])
    swap , Asort = InSort(A,n)
    print(swap)

if __name__ == '__main__':
    main()
