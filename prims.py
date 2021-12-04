from queueADT import PQueue, element
import sys

def prim(graph):
    mstHeap = PQueue()
    mstGraph = Graph()
    #create the heap with distance estimates, 0 as the current node and inf for the others
    key_list = list(graph.ad_list.keys())

    parent_list = {}
    
    #insert first vertex with a key value of 0
    mstHeap.enqueue([key_list[0], 0])
    parent_list[key_list[0]] = -1

    #Insert the rest of the vertices with inf key value
    for v in range(1, len(graph.ad_list)):
        mstHeap.enqueue([key_list[v], 10**10])
        parent_list[key_list[v]] = -1

    while mstHeap.queue.size >= 0:
      
        u = mstHeap.dequeue()
        u_edges = graph.get_edges(u[0])


        for v in u_edges.keys():
            v_index = mstHeap.queue.search(v)
            if v_index != -1: # If vertex v is not in the MST
                dst_estimate = mstHeap.queue.heap[v_index][1]
                if dst_estimate > graph.get_line_weight(u[0], v): #If cheaper than distnace estimate 

                    mstHeap.queue.heap[v_index][1] = graph.get_line_weight(u[0], v)
                    parent_list[v] = u[0]
 
                    mstHeap.queue.shiftUp(v_index)
    for x in parent_list.keys():
        if parent_list[x] != -1:
            mstGraph.insert_edge(x, parent_list[x])
    return mstGraph
def keysort(e):
    return e[1]
def prim3(graph):
    mstHeap = []
    mstGraph = Graph()
    #create the heap with distance estimates, 0 as the current node and inf for the others
    key_list = list(graph.ad_list.keys())
    parent_list = {}
    still_in = {}
    
    #insert first vertex with a key value of 0
    mstHeap.append([key_list[0], 0])
    parent_list[key_list[0]] = -1
    still_in[key_list[0]] = False
    #Insert the rest of the vertices with inf key value
    for v in range(1, len(graph.ad_list)):
        mstHeap.append([key_list[v], 10**10])
        parent_list[key_list[v]] = -1
        still_in[key_list[v]] = True
    mstHeap.sort(key = keysort)
    while True:
        length = len(mstHeap)
        if length <= 0:
            break
        # print(length)
        mstHeap.sort(key = keysort)
        u = mstHeap.pop(0)
        still_in[u[0]] = False
        u_edges = graph.get_edges(u[0])


        for v in u_edges.keys():
            # for x in mstHeap:
            #     print(x)
            # print()
            if still_in[v]:
                v_index = [x[0] for x in mstHeap].index(v)
                # print(parent_list)
                dst_estimate = mstHeap[v_index][1]
                # print(dst_estimate)
                if dst_estimate > graph.get_line_weight(u[0], v): #If cheaper than distnace estimate 

                    mstHeap[v_index][1] = graph.get_line_weight(u[0], v)
                    parent_list[v] = u[0]
                    
                    
    for x in parent_list.keys():
        if parent_list[x] != -1:
            mstGraph.insert_edge(x, parent_list[x])
    return mstGraph   
def prim2(graph):
    mstGraph = Graph()
    mstSet = {}
    parent_list = {}
    vertices = list(graph.ad_list.keys())
    keys = {}
    graphSize = len(vertices)



    #Insert the rest of the vertices with inf key value\
    print(len)
    for v in range(len(vertices)):
        mstSet[v] = False
        parent_list[vertices[v]] = -1
        keys[vertices[v]] = 10**10
    parent_list[vertices[0]] = -1
    keys[vertices[0]] = 0


    for x in range(graphSize):
        #Find the a safe edge, ie the node with the smallest distance estimate 
        minKey = 10**11
        for v in vertices:
            
            if keys[v] < minKey and not mstSet[v]:
                minKey = keys[v]
                minIndex = v
        mstSet[vertices[minIndex]] = True
        
        #Go through the nodes connected to the min index and  update their distance estimates 
        for v in graph.get_edges(minIndex).keys():
            dst_estimate = keys[vertices[v]]
            line_weight = graph.get_line_weight(minIndex, v)
            if line_weight < dst_estimate and mstSet[vertices[v]] == False:
                keys[vertices[v]] = line_weight
                parent_list[vertices[v]] = minIndex
    for x in parent_list.keys():
        if parent_list[x] != -1:
            mstGraph.insert_edge(x, parent_list[x])
    return mstGraph

        

                




class Graph():
    """
    A graph class which stores the graph in an adjeceny list(modified)
    Its actaully a dictionary where the key is the node id and the payload is a list of pairs which are {nodeID, edge weight}
    """
    def __init__(self):
        self.ad_list = {}

    def get_edges(self, i):
        return self.ad_list[i]

    def get_line_weight(self, u, v):
        return self.ad_list[u][v]
    def convertToDict(self):
        returnDict = {}
        edgeId = 0
        for v in self.ad_list.keys():
            for u in self.ad_list[v].keys():
                returnDict[edgeId] = [v, u, self.ad_list[v][u]]
                del self.ad_list[u][v]
                edgeId += 1
        return returnDict

    def convertFromDict(self, graphDict):

        for e in graphDict.keys():
            node1 = graphDict[e][0]
            node2 = graphDict[e][1]
            weight = graphDict[e][2]
            
            try:
                self.ad_list[node1][node2] = weight
            except Exception as e:
                self.ad_list[node1] = {node2:weight}
                
            try:
                self.ad_list[node2][node1] = weight
            except Exception as e:
                self.ad_list[node2] = {node1:weight}
 
    def insert_edge(self, node1, node2, weight = 0):
        try:
            self.ad_list[node1][node2] = weight
        except Exception as e:
            self.ad_list[node1] = {node2:weight}
            
        try:
            self.ad_list[node2][node1] = weight
        except Exception as e:
            self.ad_list[node2] = {node1:weight}
    
    def __str__(self):
        result = ""

        for x in self.ad_list.keys():
            result += "{} : {}\n".format(x, self.ad_list[x])
        return result
