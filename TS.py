# Topological sorting
# Given: A simple directed acyclic graph with n≤10^3 vertices in the edge list format.
# Return: A topological sorting (i.e., a permutation of vertices) of the graph.

class Graph():

    def __init__(self,V):
        self.V = V
        self.adj = {}
        self.L = []
    def addEdge(self,u,v):
        if u not in self.adj:
            self.adj[u] = []
            self.adj[u].append(v)
        else:
            self.adj[u].append(v)

    def descendent(self,):
        descendent = set()
        for val in self.adj.values():
            descendent = set(list(descendent)+val)
        return descendent

    def topological_sorting(self,):

        descendent = self.descendent()

        S = [x for x in self.adj.keys() if x not in descendent]

        while S:
            for n in S:
                S.remove(n)
                self.L.append(n)
                try:
                    v = self.adj[n]
                    del self.adj[n]
                    descendent = self.descendent()
                    for val in v:
                        if val not in descendent:
                            S.insert(0,val)
                except KeyError:
                    break

if __name__ == "__main__":
    # read local file
    with open("D:/Downloads/rosalind_ts.txt") as f:
        r = f.read()
    arr = [ [ int(y) for y in x.split(" ")] for x in r.split("\n")[:-1]]
    # creating graph, adding edge
    myGraph = Graph(arr[0][0]+1)
    for x,y in arr[1:]:
        myGraph.addEdge(x,y)
    # topological sorting
    myGraph.topological_sorting()
    for x in myGraph.L:
        print(x,end = ' ')
