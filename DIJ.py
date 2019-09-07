### Dijkstra's Algorithm
#
# Given: A simple directed graph with positive edge weights from 1 to 103 and n≤103 vertices in the edge list format.

# Return: An array D[1..n] where D[i] is the length of a shortest path from the vertex 1 to the vertex i (D[1]=0). If i is not reachable from 1 set D[i] to −1.

import numpy as np

class Graph():

    def __init__(self,V):
        self.V = V
        self.adj = [[] for i in range(V+1)]
        self.dist = [{} for i in range(V+1)]
        self.distance = [np.inf]*(V)
        self.distance[0] = 0
        self.visited = [{} for i in range(V+1)]

    def addEdge(self,v,u,dist):
        self.adj[v].append(u)
        if u not in self.dist[v].keys():
            self.dist[v][u] = dist
        elif dist < self.dist[v][u]:
            self.dist[v][u] = dist
        self.visited[v][u] = False

    def DijkstraAlgorithm(self,init,neighbors_step):
        neighbors = self.adj[init]
        if init == 1:
            neighbors_step = 0

        for n in neighbors :
            if self.distance[n-1] > self.dist[init][n] + neighbors_step:
                self.distance[n-1] = self.dist[init][n] + neighbors_step
                self.visited[init][n] = True
                #print("Set d "+str(n) + " = " +str(self.distance[n-1]) + " through " + str(init)+" to "+  str(n))

                self.DijkstraAlgorithm(n,neighbors_step+self.dist[init][n])

    def runDA(self):
        self.DijkstraAlgorithm(1,0)

def readDAfile(Dir):
    f = open(Dir)
    r = f.read()
    f.close()
    sampledata = [[ int(y) for y in x.split(' ')] for x in r.split("\n")[:-1]]
    n = sampledata[0][0]
    return n, sampledata

### Running code using file from local directory
n, sampledata = readDAfile("D:/Downloads/rosalind_dij.txt")
myGraph = Graph(n)
### adding edges and distances
for x,y,z in sampledata[1:]:
    myGraph.addEdge(x,y,z)
### Run DijkstraAlgorithm
myGraph.runDA()
### print results
val = myGraph.distance
for x in val:
    if x == np.inf:
        print(-1,end= ' ')
    else:
        print(x,end = ' ')
