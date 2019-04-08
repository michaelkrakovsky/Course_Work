# Name: Michael Krakovsky (Student ID: 10134030)
# Date: April 7, 2019
# Description: Complete the requirements set forth in Assignment 4.
# Version: 1.0

from random import randint
from queue import Queue

class MinHeap:

    def __init__(self):

        # Class Description: Init the MinHeap. Create a MinHeap. The format of the list will be of tuples.
        # (verticieOne, verticieTwo, edgeWeight)
        # Parameters: self (The instance of the object)
        # Returns: None # Throws: None

        self.minHeap = [(0, 0, 0)]                      # The intial value will never be touched.

    def peek(self):                     

        # Function Description: Return the top of the heap array.
        # Parameters: self (The instance of the object)
        # Returns: (The top of the heap) # Throws: None  

        if (len(self.minHeap) <= 1):       # The list does not contain values, return none.
            return None
        else:
            return self.minHeap[1]         # This is the first value in the list.

    def poll(self):                     

        # Function Description: Return the top of the heap array AND remove the value from the heap.
        # Parameters: self (The instance of the object)
        # Returns: (The top of the heap) # Throws: None  

        highestPriority = self.minHeap[1]
        length = len(self.minHeap)  
        if len(self.minHeap) == 2:
            return self.minHeap.pop(1)                             # Remove and return the top node if only one exists   
        if len(self.minHeap) < 2:
            return None                                            # The list is empty             
        self.minHeap[1] = self.minHeap.pop(length - 1)             # Replace the top node with the last value of the array.
        length -= 1
        parentLoc = 1
        childOne = parentLoc * 2
        childTwo = parentLoc * 2 + 1 
        while (childOne < length):                                  # Propogate downwards to recalibrate the entire heap
            if (childTwo >= length):                                # Signifies the end of the heap.                   
                if (self.minHeap[childOne][2] < self.minHeap[parentLoc][2]):          # Case One: A single left child that is bigger.
                    buffer = self.minHeap[parentLoc]
                    self.minHeap[parentLoc] = self.minHeap[childOne]
                    self.minHeap[childOne] = buffer                             
                return highestPriority                              # The tree is fully calibrated since the right child D.N.E, we have reached the end.
            if (self.minHeap[childOne][2] <= self.minHeap[parentLoc][2] and self.minHeap[childOne][2] <= self.minHeap[childTwo][2]):          # Case Two: Two children, the left is bigger
                buffer = self.minHeap[parentLoc]
                self.minHeap[parentLoc] = self.minHeap[childOne]
                self.minHeap[childOne] = buffer
                parentLoc = childOne                                # Move the propogation downward
                childOne = parentLoc * 2
                childTwo = parentLoc * 2 + 1
            elif (self.minHeap[childTwo][2] <= self.minHeap[parentLoc][2] and self.minHeap[childTwo][2] <= self.minHeap[childOne][2]):        # Case Three: Two children, the right is bigger
                buffer = self.minHeap[parentLoc]
                self.minHeap[parentLoc] = self.minHeap[childTwo]
                self.minHeap[childTwo] = buffer
                parentLoc = childTwo                                # Move the propogation downward
                childOne = parentLoc * 2
                childTwo = parentLoc * 2 + 1
            else:                                                   # Case Four: The parent is bigger than its children, heap is now legal.
                break
        return highestPriority

    def insert(self, value):

        # Function Description: Insert a new value into the heap array.
        # Parameters: self (The instance of the object), value (The value to insert)
        # Returns: None # Throws: None

        self.minHeap.append(value)                   # Insert the value at the end of the list, regardless of position. (The first value in the array does not matter)
        childPos = len(self.minHeap) - 1             # Start at the end of the array where the value was inserted
        while childPos > 1:                          # We desire to avoid the first value.
            parentPos = childPos // 2
            if self.minHeap[childPos][2] < self.minHeap[parentPos][2]:        # Find the appropriate node to insert the new value. Once found switch the value.
                buffer = self.minHeap[childPos]
                self.minHeap[childPos] = self.minHeap[parentPos]
                self.minHeap[parentPos] = buffer
            childPos = parentPos          # Traverse upwards within the list. (We only focus on one side of the tree.)

    def printHeap(self):

        # Function Description: Print the min Heap in order.
        # Parameters: self (The instance of the class), minHeap (A min heap of edges)
        # Returns: None # Throws: None

        new = MinHeap()
        while len(self.minHeap) > 1:
            newVal = self.poll()
            print(newVal, end=" ")
            new.insert(newVal)
        print("")
        self.minHeap = new.minHeap

class Tester:

    def __init__(self):

        # Class Description: PLEASE IGNORE THIS CLASS UNLESS YOU NEED TO USE A FUNCTION. The person of this class is develop 
        # tester functions to help assist in the develop.
        # Parameters: None # Returns: None # Throws: None

        pass

    def printGraph(self, graph):

        # Function Description: Print a given a graph.
        # Parameters: graph (The desired graph to be printed)
        # Throws: None # Returns: None

        for i in range(0, len(graph)):
            print("Printing Verticie " + str(i) + " Contents:", end=' ')
            print(graph[i])

# 1.1 Random Graph Generation

class GenerateConnectedGraph:

    def __init__(self, numVerticies, edgeWeightsMax, hardCodedGraph=None):

        # Class Description: Create an object to generate a connected graph with random weights on the edges.
        # Parameters: numVerticies (The number of vertices), edgeWeightsMax (The upper bound range for the edge weights),
        # hardCodedGraph (The option for a user to input there own hardcoded graph)
        # The data structure that will store the edge information will be an array of Dictionaries. 
        # The first layer of the index will represent the verticies number. The dictionary attached 
        # will represent the edges that the verticie is connected to. The value will be the weight.
        # Here is what the structure will appear like.
        # graph = [p1, p2, ..., pn]    Where p is the pointer to the dictionary of edges and the index of p is the number to the verticie. 
        # p1 = {3: 12.32, 6: 65.23, 0: 35}      Each pointer will contain at least one edge and will look like the previous example.
        # Parameters: self (The instance of the class), numVerticies (The number of the verticies), 
        # edgeWeightsMax (The range of edge weights to be attatched)
        # Returns: None # Throws: None

        if not hardCodedGraph:          # Create if the user doesn't input their own graph format
            self.graph = self.createTwoDArray(numVerticies, edgeWeightsMax)
        else:
            self.graph = hardCodedGraph

    def createTwoDArray(self, numVerticies, edgeWeightsMax):

        # Function Description: Create a 2D array to store the random weights of the graph, the current graph will be undirected.
        # Parameters: self (The instance of the class), numVerticies (The number of the verticies)
        # Returns: graph (The graph with the randomly generated edge values) Throws: None

        verticieNumbers = [i for i in range(0, numVerticies)]
        graph = [{} for i in range(0, numVerticies)]                        # Create all the dictionaries
        for verticie in range(0, numVerticies): 
            numEdgesToConnect = randint(1, numVerticies - 1)      # numVerticies Holds the number of edges that will be appended to this graph. We can manipulate how sparse the graph is here
            usedVerticies = []                                              # The edges that were already added to this verticie.
            usedVerticies.append(verticieNumbers.pop(verticie))             # This will esnure a loop will not exist in the graph.
            while len(graph[verticie]) < numEdgesToConnect:                 # Generate x number of weighted edges. (x is denoted as numEdgesToConnect)
                verticieIndex = randint(0, len(verticieNumbers) - 1)        # Get the verticie to connect to the graph.
                popedVertice = verticieNumbers.pop(verticieIndex)
                if (popedVertice not in graph[verticie]):                   # If it is not in your current dictionary, add the new key to both afiliated dictionaryies
                    getEdgeWeight = randint(1, edgeWeightsMax)              # Get the edge weight
                    graph[verticie][popedVertice] = getEdgeWeight           # Add to both this dictionary and the other dictionary
                    graph[popedVertice][verticie] = getEdgeWeight
                usedVerticies.append(popedVertice)
            usedVerticies.sort()                                            # Ensure the list is resorted prior to popping all the indexes back.
            while len(usedVerticies) > 0:                                   # Re-add the verticies to the unused list
                temp = usedVerticies.pop(0)
                verticieNumbers.insert(temp, temp)
        return graph

    def _convertToGraph(self, edgeDict):
    
        # Function Definition: Convert the edge dictionary into a graph
        # Parameters: self (The instance of the class), edgeDict (The dictionary containing the edges)
        # Returns: convertedGraph (The converted Graph) # Throws: None

        convertedGraph = [{} for i in range(0, len(edgeDict) + 1)]
        for i in edgeDict:
            convertedGraph[i[0]][i[1]] = i[2]
            convertedGraph[i[1]][i[0]] = i[2]
        return convertedGraph

    def breadthSearch(self, aGraph):

        # Function Description: Perform a Breadth-First Search on a given graph.
        # Parameters: self (The instance of the class), aGraph (A given graph)
        # Returns: None # Throws: None

        q = Queue()
        visitedVerticies = {}
        edgeSum = 0
        startingPoint = randint(0, len(aGraph) - 1)
        q.put(aGraph[startingPoint])                                # Start at a random point on the queue and add its verticie information
        visitedVerticies[startingPoint] = 0                         # We do not care about the 0 value.
        while (q.qsize() > 0):
            currentVert = q.get()                                   # This will be the connected verticies
            for key, value in currentVert.items():
                if key not in visitedVerticies:
                    visitedVerticies[key] = 0
                    edgeSum += value
                    q.put(aGraph[key])
        return edgeSum

    def _getEdgeHeap(self, aGraph):

        # Function Description: Put all the edges from a graph into a min heap.
        # Parameters: self (The instance of the class), aGraph (A given graph to reduce to a MST)
        # Returns: edgeMinHeap (A min heap containing all the edges) # Throws: None

        edgeMinHeap = MinHeap()
        vertNum = 0
        for edgeDict in aGraph:
            for key, value in edgeDict.items():
                edgeMinHeap.insert((vertNum, key, value))
            vertNum += 1
        return edgeMinHeap

    def _addVertEdgesToHeap(self, verticieNum, verticieDict, minH):

        # Function Description: Add all the edges from a verticie in tuple form to the minheap.
        # Parameters: self (The instance of the class), verticieNum (The verticie number)
        # verticieDict (The dictionary attatched to the verticie), minH (The min Heap to receive the edges)
        # Returns: None # Throws: None

        for key, edgeWeight in verticieDict.items():
            minH.insert((verticieNum, key, edgeWeight))

    def primSpanningTree(self, aGraph):

        # Function Description: Using Prim's Algorithm, create a minimum spanning tree.
        # Parameters: self (The instance of the class), aGraph (A given graph to reduce to a MST)
        # Returns: newGraph (The prim spanning tree of the graph) # Throws: None

        newGraph = [{} for i in range(0, len(aGraph))]
        edgesToChooseFrom = MinHeap()
        startingVerticie = randint(0, len(aGraph) - 1)
        t = {}                                                  # Set the verticie dictionaries up
        t[startingVerticie] = 0
        self._addVertEdgesToHeap(startingVerticie, aGraph[startingVerticie], edgesToChooseFrom)
        q = {}
        #print("Starting at the vertice: " + str(startingVerticie))     # To Debug
        for i in range(0, len(aGraph) - 1):                     # All the verticies that are not included in t list
            if i != startingVerticie:
                q[i] = 0
        edgesAdded = 0
        while edgesAdded < (len(aGraph) - 1):
            possibleEdgeToInsert = edgesToChooseFrom.poll()
            if possibleEdgeToInsert[1] not in t:                # If the next min edge doesnt create a cycle (The connecting verticie hasn't been connected yet) add to the edge set
                newGraph[possibleEdgeToInsert[0]][possibleEdgeToInsert[1]] = possibleEdgeToInsert[2]
                newGraph[possibleEdgeToInsert[1]][possibleEdgeToInsert[0]] = possibleEdgeToInsert[2]
                q.pop(possibleEdgeToInsert[1], None)            # Remove from q and add to t
                t[possibleEdgeToInsert[1]] = 0                  
                self._addVertEdgesToHeap(possibleEdgeToInsert[1], aGraph[possibleEdgeToInsert[1]], edgesToChooseFrom)               # Add new options to the min heap
                edgesAdded += 1
        return newGraph                                                                                                           # The edges are in the keys

    def kruskalSpanningTree(self, aGraph):

        # Function Description: Implement solution one from class to create a minimum spanning tree.
        # Parameters: self (The instance of the class), aGraph (A given graph to reduce to a MST)
        # Returns: newGraph (The prim spanning tree of the graph) # Throws: None 
        
        edgeSet = [i for i in range(0, len(aGraph))]
        newGraph = [{} for i in range(0, len(aGraph))]
        edgesToChooseFrom = MinHeap()
        edgeNumber = 0
        for edgeDict in aGraph:                     # Add all the edges to a heap
            self._addVertEdgesToHeap(edgeNumber, edgeDict, edgesToChooseFrom)
            edgeNumber += 1
        numTransitions = 0
        while numTransitions < (len(aGraph) - 1):
            edge = edgesToChooseFrom.poll()
            if edgeSet[edge[0]] != edgeSet[edge[1]]:        # Add the edge to the edge set
                oldArray = edgeSet[edge[1]]
                for indx, val in enumerate(edgeSet):
                    if val == oldArray:
                        edgeSet[indx] = edgeSet[edge[0]]
                newGraph[edge[0]][edge[1]] = edge[2]
                newGraph[edge[1]][edge[0]] = edge[2]
                numTransitions += 1
        return newGraph

    def compareSpanningTrees(self, ns, numTimesToRepeat):

        # Function Description: Compare the two algorithms that create a spanning tree.
        # Parameters: self (The instance of the class), ns (The combinateion of different number of verticies)
        # numTimesToRepeat (The number of times to repeat the experiment)
        # Returns: avgDifferences (A dictionary illustrating the number of verticies (The keys) 
        # and the differences themselves (The values)) 
        # Throws: None

        avgDifferences = {}
        for verticieNum in ns:
            diffs = []
            counter = 0
            while counter < numTimesToRepeat:
                counter += 1
                randomGraph = GenerateConnectedGraph(verticieNum, 100)
                bfsWeight = self.breadthSearch(randomGraph.graph)
                primSpanningWeight = self.breadthSearch(self.primSpanningTree(randomGraph.graph))
                percDiff = (bfsWeight - primSpanningWeight) / primSpanningWeight
                diffs.append(percDiff)
            avgDifferences[verticieNum] = sum(diffs) / float(len(diffs))            # Calculate differencs, apply the label
        return avgDifferences          

def main():

    testGraph = [                               # This is the graph from question 1.2 Hardcoded
                {1: 15, 3: 7, 4: 10}, 
                {0: 15, 2: 9, 3: 11, 5: 9}, 
                {1: 9, 4: 12, 5: 7}, 
                {0: 7, 1: 11, 4: 8, 5: 14}, 
                {0: 10, 2: 12, 3: 8, 5: 8}, 
                {1: 9, 2: 7, 3: 14, 4: 8}    
            ]     

    ### Test Code ###
    t = Tester()    # To Show the resulting graphs
    testGraphObject = GenerateConnectedGraph(None, None, testGraph)
    t.printGraph(testGraphObject.graph)
    print(30 * "-" + " Prim MST: ")
    primSpan = testGraphObject.primSpanningTree(testGraphObject.graph)
    t.printGraph(primSpan)
    print(30 * "-" + " Kruskal MST: ")
    kruskalSpanningTree = testGraphObject.kruskalSpanningTree(testGraphObject.graph)
    t.printGraph(kruskalSpanningTree)
    print(30 * "-" + " Comparing Prim and BST: ")
    print(testGraphObject.compareSpanningTrees([10, 20, 50, 100], 25))

if __name__ == '__main__':
    main()