import sys
from graphIO import parseGraphFromTextFile, writeGraphToTextFile

try:
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
except:
    inputFile = "testData.txt"
    outputFile = "testOut.txt"
d = parseGraphFromTextFile(inputFile)

writeGraphToTextFile(outputFile,d)
print("done")