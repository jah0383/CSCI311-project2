import sys
from prims import Graph, prim, prim2
from graphIO import parseGraphFromTextFile, writeGraphToTextFile, writeFromEdgeList
try:
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
except:
    inputFile = "toyTest.txt"
    outputFile = "toyTestOut.txt"

d = parseGraphFromTextFile(inputFile)
g = Graph()
g.convertFromDict(d)
prim2(g)
writeGraphToTextFile(outputFile,d)