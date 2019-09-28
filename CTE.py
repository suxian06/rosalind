# Given: A positive integer k≤20 and k simple directed graphs with positive integer edge weights and at most 103 vertices in the edge list format.

# Return: For each graph, output the length of a shortest cycle going through the first specified edge if there is a cycle and "-1" otherwise.

def readDAfile(Dir):
    f = open(Dir)
    r = f.read()
    f.close()
    sampledata = [[ int(y) for y in x.split(' ')] for x in r.split("\n")[:-1]]
    n = sampledata[0][0]
    return n, sampledata

#import numpy as np

class Graph():

    def __init__(self,V):
        self.V = V
        self.adj = [{} for i in range(self.V)]
        self.dist = [1000000 for i in range(self.V)]
        self.visited = [False] * (self.V-1)
        self.predist = [0] * (self.V)

    def addEdge(self,u,v,w):
        if v in self.adj[u]:
            if self.adj[u][v] > w:
                self.adj[u].update({v:w})
        else:
            self.adj[u].update({v:w})

    def BellmanFord(self,v):
        # initiate
        self.dist[v] = 0
        for i in range(self.V - 2):
            for ver in range(1,self.V):
                for nei in self.adj[ver].keys():
                    if self.dist[nei] > self.dist[ver] + self.adj[ver][nei]:
                        self.dist[nei] = self.dist[ver] + self.adj[ver][nei]

    def CTE(self,u,v):
        self.BellmanFord(v)
        self.dist = [x if x!= 1000000 else -1 for x in self.dist]
        if self.dist[u] != -1:
            self.dist[u] += self.adj[u][v]
        return self.dist[u]

if __name__ == "__main__":
    f = readDAfile("D:/Downloads/rosalind_cte.txt")
    f = f[1]

    init_val = []
    init_index = []
    for y,x in enumerate(f):
        if len(x) == 2:
            init_val.append(x)
            init_index.append(y)

    graph = []
    for i in range(len(init_index)-1):
        graph.append(f[init_index[i]:init_index[i+1]-1])
    graph.append(f[init_index[-1]:])

    for val in graph:
        G = Graph(val[0][0]+1)
        for x,y,z in val[1:]:
            G.addEdge(x,y,z)
        print(G.CTE(val[1][0],val[1][1]),end = ' ')

# using bellmanFord algorithm
