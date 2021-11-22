def parseGraphFromTextFile(inputFile):
    """
    Takes in a file with each line being
    "Edge_ID Start_Node_ID End_Node_ID Length"
    and returns a dictionary where each entry is 
    Edge_ID : [Start_Node_ID, End_Node_ID, Length]
    """
    try:
        edgeFile = open(inputFile,"r")
        
        graphDictionary = {}
        for line in edgeFile:
            edge = line.split(" ")
            graphDictionary[int(edge[0])] = [int(edge[1]),int(edge[2]),float(edge[3].strip())]
        return graphDictionary
        edgeFile.close()
    except Exception as e:
        print("There was an exception in trying to read the file with the edges")
        raise e

def writeGraphToTextFile(outputFile, graphDictionary):
    try:
        edgeFileOut = open(outputFile, "w")

        for i,edge in enumerate(graphDictionary.items()):
            if i == len(graphDictionary)-1:
                edgeFileOut.write(f"{edge[0]} {edge[1][0]} {edge[1][1]} {edge[1][2]:.6f}")
            else:
                edgeFileOut.write(f"{edge[0]} {edge[1][0]} {edge[1][1]} {edge[1][2]:.6f}\n")
        edgeFileOut.close()     
        
    except Exception as e:
        print("There was an exception trying to write to the output file")
        raise e