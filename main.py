import sys
from graphIO import parseGraphFromTextFile, writeGraphToTextFile, writeFromEdgeList
from prims import Graph, prim, prim2
from time import time_ns
#Toy test is the graph here https://www.geeksforgeeks.org/prims-mst-for-adjacency-list-representation-greedy-algo-6/
def tick():
    return time_ns()

def tock(start):
    return time_ns() - start
try:
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
except:
    inputFile = "toyTest.txt"
    outputFile = "toyTestOut.txt"
d = parseGraphFromTextFile(inputFile)
g = Graph()
g.convertFromDict(d)
print(g)
prim(g)
writeGraphToTextFile(outputFile,d)
print("done")
print("-----------------------------------------------------")

from kruskals import KruskalGraph
# Driver code
g2 = KruskalGraph()
d2 = parseGraphFromTextFile("testData.txt")
g2.convertFromDict(d2)
print(g2.V)
# print(g2)
s = tick()
el = g2.kruskal()
# for x in el:
#     print(x)
print(tock(s)//10.0**9)
writeFromEdgeList("testOut.txt",el)
