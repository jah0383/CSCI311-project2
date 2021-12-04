class KruskalGraph:
    def __init__(self, vertex = 0):
        self.V = vertex # number of vertices
        self.graph = [] # dictionary to store graph

    def convertToDict(self):
        returnDict = {}
        edgeId = 0
        for u, v, weight in self.graph:
            returnDict[edgeId] = [u, v, weight]
            edgeId += 1 
        return returnDict

    def convertFromDict(self, graphDict):
        unique_nodes = set()
        for e in graphDict.keys():
            
            node1 = graphDict[e][0]
            node2 = graphDict[e][1]
            weight = graphDict[e][2]
            self.add_edge(node1, node2, weight)

            if node1 not in unique_nodes:
                self.V+=1 
                unique_nodes.add(node1)
            if node2 not in unique_nodes:
                self.V+=1 
                unique_nodes.add(node2)                

    
    # function to add edge to graph
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # find set of element i
    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])
 
    # union of 2 sets x and y
    def union(self, parent, rank, x, y):
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)
        
        # attach smaller rank under higher rank
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []# store MST result
        i = 0 
        e = 0

        # sort all edges in ascending order of weight
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        # create V subsets of with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        
        
        while e < self.V - 1:
            # pick the smallest edge, and increment index
            u, v, w = self.graph[i]
            i = i + 1
            x = self.search(parent, u)
            y = self.search(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        return result

    def __str__(self):
        result = ""
        for e in self.graph:
            result += (str(e) + "\n")
        return result 

