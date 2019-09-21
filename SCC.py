# Strongly Connected Components
# Given: A simple directed graph with n≤103 vertices in the edge list format.
# Return: The number of strongly connected components in the graph.
def readrosalinfile(Dir):
    f = open(Dir)
    t = f.read()
    t = t.split('\n')
    f.close()
    f = t
    return f

class Graph():

    def __init__(self,V):
        self.V = V
        self.G_adj = [[] for i in range(self.V)]
        self.Gt_adj = [[] for i in range(self.V)]
        self.visited = [False]*(self.V - 1)
        self.stack = []

    def addEdge(self,u,v):
        self.G_adj[u].append(v)
        self.Gt_adj[v].append(u)

    def DFS(self,i):

        self.visited[i - 1] = True
        for adj in self.G_adj[i]:
            if not self.visited[adj - 1]:
                self.DFS(adj)
        self.stack.append(i)

    def DFS_GT(self,SCC,i):
        neighbors = []
        neighbors.append(i)

        self.visited[i - 1] = True
        SCC.append(i)

        for adj in self.Gt_adj[i]:
            if not self.visited[adj - 1]:
                self.DFS_GT(SCC,adj)

        return SCC

    def SCC(self,):
        for i in range(1,self.V):
            if not self.visited[i - 1]:
                self.DFS(i,)

        self.visited = [False]*(self.V - 1)
        SCC = []
        while self.stack:
            val = []
            init = self.stack.pop(-1)
            if not self.visited[init - 1]:
                val = self.DFS_GT(val,init)
                if val != []:
                    SCC.append(val)

        return SCC

if __name__ == "__main__":
    f = readrosalinfile("D:/Downloads/rosalind_scc.txt")
    arr = [ [ int(y) for y in x.split(' ')] for x in f[1:-1]]
    V = int(f[0].split(' ')[0]) + 1
    G = Graph(V)
    for x,y in arr:
        G.addEdge(x,y)
    scc = G.SCC()
    print(len(scc))
