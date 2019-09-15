# Connected Components
# Given: A simple graph with n≤103 vertices in the edge list format.
# Return: The number of connected components in the graph.

def readrosalinfile(Dir):
    """
    read files from rosalind.

    parameters:
    -----------
    Dir: the directory to extract files

    return: a list of information
    """
    f = open(Dir)
    t = f.read()
    t = t.split('\n')
    f.close()
    f = t
    return f

class Graph():

    def __init__(self,V):
        self.V = V
        self.adj = [[] for i in range(V)]
        self.visited = [False]*self.V

    def addEdge(self,u,v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def DFS(self,i,stack):
        self.visited[i] = True
        stack.append(i)
        for neighbor in self.adj[i]:
            if self.visited[neighbor] == False:
                self.DFS(neighbor,stack)

    def CC(self,):
        CC = []
        for i in range(1,self.V):
            stack = []
            if self.visited[i] == False:
                self.DFS(i,stack)
            if stack != []:
                CC.append(stack)
        return CC

if __name__ == "__main__":
    # loading local file
    Dir = "C:/Users/Xian/rosalind.algorithm/rosalind_cc.txt"
    f = readrosalinfile(Dir)
    t = f[1:-1]
    n = [ int(x) for x in f[0].split(' ')][0]
    t = [ [ int(y) for y in x.split(' ')] for x in t]
    #
    myGraph = Graph(n+1)
    for x,y in t:
        myGraph.addEdge(x,y)
    cc = myGraph.CC()
    print(len(cc))
