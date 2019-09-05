###  Square in a graph
# python = 3.7
import numpy as np

def readSQfile(Dir):
    f = open("D:/Downloads/rosalind_sq.txt")
    r = f.read()
    f.close()
    alldata = r.split('\n\n')[1:]
    alldata = [ x.split('\n') for x in alldata]
    alldata[-1] = alldata[-1][:-1]
    for i in range(len(alldata)):
        alldata[i] = [[int(y) for y in x.split(" ") ]for x in alldata[i]]
    return alldata

def SquareInAGraph(adjmatrix):
    """1. Find the obj that have distance = 1 away from the init, store them in dist_1
       2. Find the dist = 1 obj that have distance = 1 away from the obj within dist_1, store in stacks
       3. Test if there exists a common obj that have dist = 1 from the obj in stacks, then it will form a circle of length = 4"""

    L = len(adjmatrix)
    for i in range(1,L):
        dist_1 =[ y for x,y in zip(adjmatrix[i],range(L)) if (x == 1) & (y != i) ]
        stacks = []
        if len(dist_1) <= 1:
            pass
        for j in dist_1:
            stacks.append([ y for x,y in zip(adjmatrix[j],range(L)) if (x == 1) & (y != j) & (y !=i)])
        for i in range(len(stacks)):
            for j in range(i+1,len(stacks)):
                if np.any([x in stacks[i] for x in stacks[j]]):
                    return 1
    return -1

def Adjmatr(n,pairs):
    adjmatrix = np.diag([1]*(n+1))
    for i in range(len(pairs)):
        adjmatrix[pairs[i][0],pairs[i][1]] = 1
        adjmatrix[pairs[i][1],pairs[i][0]] = 1
    return adjmatrix

if __name__ == "__main__":
    Dir = "D:/Downloads/rosalind_sq.txt"
    alldata = readSQfile(Dir)
    for i in range(len(alldata)):
        adjmatrix = Adjmatr(alldata[i][0][0],alldata[i][1:])
        print(SquareInAGraph(adjmatrix),end=' ')
