# Name: Michael Krakovsky (Student ID: 10134030)
# Date: Feb 18, 2019
# Description: Complete the requirements set forth in Assignment 2. (i.e. Create the bag object)
# Version: 1.0

FILENAME = r"C:\Users\micha\Documents\Queen's University\University_5\CISC_235\Assn_2_10134030_Michael_Krakovsky\testFile.txt"     # File path for the test file

# Question 1.1: Creating and Implementing a Stack and its desired functions.

class Stack():

    # Function Description: Initialisation function that sets up the foundation of the stack. (i.e. the list)
    # Parameters: self (The instance of the class) # Returns: None # Throws: None

    def __init__(self):
        self.theStack = []

    # Function Description: Check whether the object's list contains any elements.
    # Parameters: self (The instance of the class) # Returns: True if the stack is empty, False otherwise # Throws: None
    
    def isEmpty(self):
        if not self.theStack:
            return True
        else:
            return False
    
    # Function Description: Push an element to the top of the list
    # Parameters: self (The instance of the class), item (The data to insert at the top of the list) # Returns: None # Throws: None

    def push(self, item):
        self.theStack.insert(0, item)

    # Function Description: Pop an element from the list (remove and return)
    # Parameters: self (The instance of the class) # Returns: None # Throws: None

    def pop(self):
        return self.theStack.pop(0)

    # Function Description: Return the value at the top of the list but do not remove
    # Parameters: self (The instance of the class) # Returns: Item at the top of the list # Throws: None

    def top(self):
        if not self.theStack:               # Return none if there are no values at the top of the list
            return None
        else:
            return self.theStack[0]

    # Function Description: Return the length of the stack
    # Parameters: self (The instance of the class) # Returns: The stack's length # Throws: None

    def size(self):
        return len(self.theStack)

# Question 1.2: Implementing the Binary Search Tree

class TreeNode():

    # Function Description: Initialisation function that defines binary tree node. The TreeNode class will be used in the 
    # final implementation of the BinarySearchTree
    # Parameters: self (The instance of the class)
    # Returns: None # Throws: None

    def __init__(self):
        self.leftChild = None
        self.rightChild = None
        self.value = None                    

class BinarySearchTree():

    # Function Description: Initialisation function that creates the beginning instance of the binary tree.
    # The instance will be created with a root node with no left or right child with a value the users wishes to start with.
    # Parameters: self (The instance of the class)
    #  # Returns: None # Throws: None
 
    def __init__(self):
        self.rootNode = TreeNode()

    # Function Description: Insert the a new value into the tree
    # Parameters: self (The instance of the class), newValue (The new value to insert)
    # Returns: None # Throws: None
 
    def insert(self, newValue):
        currentNode = self.rootNode                  # Start from the root node
        if (currentNode.value == None):
            currentNode.value = newValue             # If the binary tree is empty, insert a root node
        else:
            while (currentNode != None):                        # Traverse throughout the list and find the proper insertion point.
                lastNode = currentNode                          # Store a memory of the previous traverse
                if (newValue >= currentNode.value):         
                    currentNode = currentNode.rightChild
                    if (currentNode == None):
                        lastNode.rightChild = TreeNode()        # Insert the new value here using the last node
                        lastNode.rightChild.value = newValue
                else:
                    currentNode = currentNode.leftChild
                    if (currentNode == None):
                        lastNode.leftChild = TreeNode()
                        lastNode.leftChild.value = newValue

    # Function Description: Find the desired value in the tree using a stack
    # Parameters: self (The instance of the class), searchValue (The value to search for)
    # Returns: thePath (The path in which the algorithm traversed) # Throws: None

    def searchPath(self, searchValue):
        traverseStack = Stack()
        thePath = []                                       # Reset the traverse path
        if (self.rootNode.value == None):                       # Ensure the tree is not empty
            return thePath
        else:
            traverseStack.push(self.rootNode)
            while (not traverseStack.isEmpty()):           # Traverse throughout the entire the stack until the item is found.
                current = traverseStack.pop()
                thePath.append(current.value)                   # Record the path in the list
                if (current.value == searchValue):
                    return thePath
                if (current.rightChild):
                    traverseStack.push(current.rightChild)
                if (current.leftChild):
                    traverseStack.push(current.leftChild)
        return thePath         

    # Function Description: Count the nodes at that level and return the depth count.
    # Parameters: self (The instance of the class), depth (The current depth), 
    # stackOut (The stack to pop the nodes), stackIn (The stack to push the nodes)
    # Returns: Int (The sum of the depths at a particular level) # Throws: None

    def __exchangeNodes(self, depth, stackOut, stackIn):
        depthAtLevel = 0
        while(not stackOut.isEmpty()):                  # Empty the stack, and add to the depth level for every node 
            current = stackOut.pop()                    # that exists beneath the node.
            if (current.leftChild):                     # Only add if the node actually exists.
                stackIn.push(current.leftChild)
                depthAtLevel += depth + 1
            if (current.rightChild):
                stackIn.push(current.rightChild)
                depthAtLevel += depth + 1
        return depthAtLevel

    # Function Description: Returns the total depth of a tree. 
    # I choose to use stacks instead of recursion to prevent overflowing the stack.
    # Parameters: self (The instance of the class)
    # Returns: Int (The sum of all the depths) # Throws: None

    def getTotalDepth(self):    
        stackOne = Stack()
        stackTwo = Stack()
        if (not self.rootNode.value):                   # Return None when the tree is empty
            return None
        stackOne.push(self.rootNode)                    
        depth = 0                                       # Keep track of the depth level
        totalDepth = 0                                  # Keep track of the total depth
        oneTurn = True
        while((not stackOne.isEmpty()) or (not stackTwo.isEmpty())):                       # Loop until both stacks are completely empty 
            if(oneTurn):
                totalDepth += self.__exchangeNodes(depth, stackOne, stackTwo)                # Count the number of nodes on the depth level
            else:
                totalDepth += self.__exchangeNodes(depth, stackTwo, stackOne)
            oneTurn = (not oneTurn) 
            depth += 1
        return totalDepth

    # Function Description: Finds the number of nodes underneath the target node
    # Parameters: self (The instance of the class), currentNode (The node that you wish to find number of nodes underneath)
    # Returns: The number of nodes # Throws: None

    def __getNumNodes(self, currentNode):
        if (not currentNode):
            return 0                            # We are in empty space, exit
        return 1 + self.__getNumNodes(currentNode.leftChild) + self.__getNumNodes(currentNode.rightChild)               # Recursively call down

    # Function Description: Find the difference between the number of nodes in the left and right subtree
    # Parameters: self (The instance of the class), currentNode (The node you wish to calculate the weight difference)
    # Returns: The difference of that particular node # Throws: None

    def __getAbsDifference(self, currentNode):
        if ((not currentNode.rightChild) and (not currentNode.leftChild)):
            return 0                                        # This is a leaf which has no difference in weight
        elif (not currentNode.leftChild):
            return self.__getNumNodes(currentNode.rightChild)                   # When the child doesn't exist
        elif (not currentNode.rightChild):
            return self.__getNumNodes(currentNode.leftChild)
        else:
            return abs(self.__getNumNodes(currentNode.leftChild) - self.__getNumNodes(currentNode.rightChild))    # When both exist, we then should calculate the number of nodes in each subtree

    # Function Description: Find the weight difference of each node and return the highest weight balance factor
    # Parameters: self (The instance of the class), currentNode (The node you wish to calculate the weight difference)
    # theMax (The highest wight difference)
    # Returns: The highest weight difference # Throws: None

    def __getWeight(self, currentNode, theMax=0):
        if (not currentNode):
            return                  # Handle when the tree is empty
        if ((currentNode.leftChild) and (currentNode.rightChild)):                  # Pass the Max variable through each recursive call, and compare each new found weight balance to the current max
            theMax = max(theMax, self.__getAbsDifference(currentNode))              # Find the weight when handling four different situations  
            return max(self.__getWeight(currentNode.leftChild, theMax), self.__getWeight(currentNode.rightChild, theMax))
        elif (currentNode.leftChild):
            theMax = max(theMax, self.__getAbsDifference(currentNode))
            return self.__getWeight(currentNode.leftChild, theMax)
        elif (currentNode.rightChild):      
            theMax = max(theMax, self.__getAbsDifference(currentNode))
            return self.__getWeight(currentNode.rightChild, theMax)
        else:
            return theMax                                   # This is the leaf node, we are first to return 0  

    # Function Description: Find the weighted balance between the nodes in the tree
    # Parameters: self (The instance of the class)
    # Returns: The weight balance factor # Throws: None

    def getWeightBalanceFactor(self):
        return self.__getWeight(self.rootNode)

    # Question 1.3: Reconstruct a Binary Search Tree From a File Using a Stack

    # Function Description: This function takes a String ﬁlename as input, and return a BinarySearchTree object.
    # Each line contains a string which is the data value stored in the node, and two other 0/1 tags. The ﬁrst
    # tag indicates whether or not this node has a left child, the second tag indicates whether the node has a right child.
    # Parameters: self (The instance of the class), fileName (The name of the file to read)
    # Returns: None # Throws: None

    def loadTreeFromFile(self, fileName):
        newTree = BinarySearchTree()                            # The new tree to return
        stack = Stack()
        with open(fileName) as f:
            lines = f.readlines()
        for line in lines:                                      # Use the stack to render the tree.
            newNode = TreeNode()
            parsedStr = line.split()
            newNode.value = int(parsedStr[0])
            if (parsedStr[2] == '1'):                               # Add the right child if indicated of an existing node
                newNode.rightChild = stack.pop()
            if (parsedStr[1] == '1'):                               # Add the left child if indicated of an existing node
                newNode.leftChild = stack.pop()    
            stack.push(newNode)                                 # Place the node back on the stack to process later             
        newTree.rootNode = stack.pop()                          # A correctly formatted file will have one remaining node on the stack.
        return newTree

# Question 1.4: Test Code and Style

def main():
    T = BinarySearchTree()
    T = T.loadTreeFromFile(FILENAME)         # Reconstruct Tree 1)
    print(T.getTotalDepth())                    # Total debth 2)
    print(T.getWeightBalanceFactor())           # Weight Balance Factor 3)
    T.insert(5)                                 # Insert a new value 4)
    print(T.searchPath(5))                      # Print the search path 5)
    print(T.getTotalDepth())                    # Total debth 6)
    print(T.getWeightBalanceFactor())           # Weight Balance Factor 3)


if __name__ == '__main__':
    main()