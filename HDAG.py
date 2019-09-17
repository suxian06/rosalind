# Hamiltonian path in DAG
# Given: A positive integer k≤20 and k simple directed acyclic graphs in the edge list format with at most 103 vertices each.
# Return: For each graph, if it contains a Hamiltonian path output "1" followed by a Hamiltonian path (i.e., a list of vertices), otherwise output "-1".

def readSQfile(Dir):
    f = open(Dir)
    r = f.read()
    f.close()
    alldata = r.split('\n\n')[1:]
    alldata = [ x.split('\n') for x in alldata]
    alldata[-1] = alldata[-1][:-1]
    for i in range(len(alldata)):
        alldata[i] = [[int(y) for y in x.split(" ") ]for x in alldata[i]]
    return alldata


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

    def hamiltonian_path(self,):

        path = self.L
        for i in range(len(path)-1):
            if path[i+1] not in self.adj[path[i]]:
                return -1
        return 1

if __name__ == "__main__":
    Dir = "D:/Downloads/rosalind_hdag.txt"
    f = readSQfile(Dir)

    l1 = []

    for i in range(len(f)):
        myG = Graph(f[i][0][0]+1)
        for x,y in f[i][1:]:
            myG.addEdge(x,y)
        myG.topological_sorting()
        for x,y in f[i][1:]:
            myG.addEdge(x,y)
        if myG.hamiltonian_path() == 1:
            l1.append([1]+myG.L)
        else:
            l1.append(-1)

    for x in l1:
        if x == -1:
            print(x)
        else:
            print(" ".join([str(v) for v in x]))
