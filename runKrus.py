import sys
from prims import Graph, prim, prim2
from graphIO import parseGraphFromTextFile, writeGraphToTextFile, writeFromEdgeList
try:
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
except:
    inputFile = "toyTest.txt"
    outputFile = "toyTestOut.txt"


from kruskals import KruskalGraph
# Driver code
g2 = KruskalGraph()
d2 = parseGraphFromTextFile(inputFile)
g2.convertFromDict(d2)
# print(g2)
el = g2.kruskal()
# for x in el:
#     print(x)
writeFromEdgeList(outputFile,el)