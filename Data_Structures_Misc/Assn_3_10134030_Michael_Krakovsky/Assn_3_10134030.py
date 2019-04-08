# Name: Michael Krakovsky (Student ID: 10134030)
# Date: March 18, 2019
# Description: Complete the requirements set forth in Assignment 3.
# Version: 1.0

import re                           # Needed to remove symbols from a sentence
import os                           # Used for testing files 

# Qu 1.2.1 Node has fields left and right for subtrees, key and value for its key-value pairs, and the node height.

class Node:

    def __init__(self):

        # Class Description: Create an object to encapsulate the contents of a node. 
        # Parameters: self (The instance of the class) # Returns: None # Throws: None

        self.leftChild = None
        self.rightChild = None
        self.key = None 
        self.value = None
        self.nodeHeight = None 

class AVLTreeMap:

    def __init__(self):
                        
        # Class Description: Init the AVL tree with the tree root
        # Parameters: self (The instance of the class)

        self.root = None 

    def __SearchPath(self, currentNode, searchKey):
        
        # Function Description: Print the search that returns a list of keys along the path.
        # Parameters: self (The instance of the class), currentNode (The node to be examined), 
        # key (The key to be located)
        # Returns: keyList (The list of all the keys that were visited) # Throws: None

        thePath = []
        while (currentNode):
            thePath.append(currentNode.key)
            if (searchKey > currentNode.key):
                currentNode = currentNode.rightChild
            elif (searchKey < currentNode.key):
                currentNode = currentNode.leftChild
            else:
                return thePath
        return thePath

    # Qu 1.2.2 

    def searchPath(self, key):
        
        # Function Description: Print the search that returns a list of keys along the path.
        # The path will be a pre-order traverse.
        # Parameters: self (The instance of the class), key (The key to search for) 
        # Returns: The list of the search path # Throws: None

        return self.__SearchPath(self.root, key)

    def _getImplemented(self, currentNode, searchKey):

        # Function Description: Find the value associated with the key.
        # Parameters: self (The instance of the class), currentNode (The node to be examined), 
        # key (The key to be located)
        # Returns: keyList (The value of the node) # Throws: None

        if (not currentNode):
            return None
        if (currentNode.key > searchKey):
            return self._getImplemented(currentNode.leftChild, searchKey)
        elif (currentNode.key < searchKey):
            return self._getImplemented(currentNode.rightChild, searchKey)
        else:
            return currentNode.value

    # Qu 1.2.3

    def get(self, key):

        # Function Description: Return the associated value given the key.
        # The path will be a pre-order traverse.
        # Parameters: self (The instance of the class) # Returns: The locations of all the values # Throws: None

        return self._getImplemented(self.root, key)

    def _checkChildHeight(self, currentNode):

        # Function Description: Ensure the current node is not equal to None. Otherwise, return the current the height.
        # Parameters: self (The instance of the object), currentNode (The node to be checked)
        # Returns: currentNode.height (The height of the node) # Throws: None

        if (currentNode == None):
            return 0
        else:
            return currentNode.nodeHeight

    def _getNewBalance(self, currentNode):

        # Function Description: Find the weight balance of the node
        # Parameters: self (The instance of the object), currentNode (The node to be checked)
        # Returns: (The new balance of the node) # Throws: None

        if (currentNode == None):
            return 0
        else:
            return (self._checkChildHeight(currentNode.leftChild) - self._checkChildHeight(currentNode.rightChild))

    def _rotateTreeRight(self, currentNode):
        
        # Function Description: Rotate the tree node to the right
        # Parameters: self (The instance of the object), currentNode (The node that will be rotated)
        # Returns: (The new node with the adjusted sub-tree) # Throws: None

        leftNode = currentNode.leftChild
        leftNodeRightChild = leftNode.rightChild 
        leftNode.rightChild = currentNode              # Perform the rotation, shift the left child up and the current node right
        currentNode.leftChild = leftNodeRightChild 
        currentNode.nodeHeight = 1 + max(self._checkChildHeight(currentNode.leftChild), self._checkChildHeight(currentNode.rightChild))  # Update the heights of the newly rotated nodes
        leftNode.nodeHeight = 1 + max(self._checkChildHeight(leftNode.leftChild), self._checkChildHeight(leftNode.rightChild))  
        return leftNode 

    def _rotateTreeLeft(self, currentNode):
        
        # Function Description: Rotate the tree node to the left
        # Parameters: self (The instance of the object), currentNode (The node that will be rotated)
        # Returns: (The new node with the adjusted sub-tree) # Throws: None

        rightNode = currentNode.rightChild
        rightNodeLeftChild = rightNode.leftChild
        rightNode.leftChild = currentNode           # Perform the rotation, shift the current node left, and render the right child the main node
        currentNode.rightChild = rightNodeLeftChild
        currentNode.nodeHeight = 1 + max(self._checkChildHeight(currentNode.leftChild), self._checkChildHeight(currentNode.rightChild))
        rightNode.nodeHeight = 1 + max(self._checkChildHeight(rightNode.leftChild), self._checkChildHeight(rightNode.rightChild))
        return rightNode

    def _putInNode(self, currentNode, newKey, newVal): 
      
        # Function Description: Insert a new node and adjust the tree along the path of the node.
        # Parameters: newKey (The new key to insert), newVal (The new value to insert)
        # Returns: None # Throws: None

        if (currentNode == None):
            newNode = Node()
            newNode.key = newKey
            newNode.value = newVal
            newNode.nodeHeight = 1                       # We have reached the end of the tree, create the new node and add to the tree. 
            return newNode
        elif (currentNode.key == newKey):                # If the keys match, simply replace the value and end the recursive calling
            currentNode.value = newVal
            return currentNode
        elif (currentNode.key > newKey):              # Keep moving down the tree, every node along the path will need to be recalibrated!
            currentNode.leftChild = self._putInNode(currentNode.leftChild, newKey, newVal) 
        else: 
            currentNode.rightChild = self._putInNode(currentNode.rightChild, newKey, newVal) 
        currentNode.nodeHeight = 1 + max(self._checkChildHeight(currentNode.leftChild), self._checkChildHeight(currentNode.rightChild))  # Recalibrate the height
        balFactor = self._getNewBalance(currentNode)            # Check to see if the tree is still balanced
        # Handle the four cases if a roation is required. 
        if (balFactor > 1) and (newKey > currentNode.leftChild.key):           # The handling of the left right case
            currentNode.leftChild = self._rotateTreeLeft(currentNode.leftChild) 
            return self._rotateTreeRight(currentNode)
        elif (balFactor > 1) and (newKey < currentNode.leftChild.key):        # The double left case
            return self._rotateTreeRight(currentNode)
        elif (balFactor < -1) and (newKey < currentNode.rightChild.key):             # Handling the right left case
            currentNode.rightChild = self._rotateTreeRight(currentNode.rightChild)
            return self._rotateTreeLeft(currentNode)
        elif (balFactor < -1) and (newKey > currentNode.rightChild.key):             # The double right case
            return self._rotateTreeLeft(currentNode)
        return currentNode

    # Qu 1.2.4

    def put(self, newKey, newVal):

        # Function Description: Insert a new node and adjust the tree.
        # Parameters: newKey (The new key to insert), newVal (The new value to insert)
        # Returns: None # Throws: None

        self.root = self._putInNode(self.root, newKey, newVal)     

# Qu 1.2.3 -> Write a WebPageIndex class that will contain the index representation of a web page.

class WebPageIndex:

    def __init__(self, fileName):               # Qu 1.3.1

        # Function Description: Init the webpage index class. Accept the filename to read.
        # Parameters: self (The instance of the object), fileName (The name of the file to read)
        # Returns: None # Throws: None
         
        self.fileName = fileName                # Qu 1.3.2
        self.formattedContent = self._readInFile()                  # Read in the file name and store the words in the order they appear all lower case.
        self.avlTree = self._createAVLTree(self.formattedContent)   # Qu 1.3.3: The avl tree of words in the file
        self.queryValue = 0                                         # This value represents the query value and will be used later to prioritise the most important queries.

    def _readInFile(self):

        # Function Description: Take the filename, create a list with the words that appeared in the file and ensure only lower case.
        # Parameters: self (The instance of the object)
        # Returns: readInFile (The converted file) # Throws: None

        words = []
        with open(self.fileName, 'r') as f:
            for line in f:
                line = line.lower()                     # Lower all the case and remove unnecessary symbols.
                line = re.sub(r"[^\w\s]", '', line)
                splitLines = line.split()
                words = words + splitLines           # Add the words to the existing list of words gathered
        return words           
    
    def getCount(self, s):                      # Qu 1.3.4

        # Function Description: Retrieve the frequency count from the dictionary created earlier.
        # Assumption: We will be neglecting the excistence of symbols and discard them.
        # Parameters: self (The instance of the object), s (The string to analyse)
        # Return: numTimes (The number of times the word occurs) # Throws: None

        s = re.sub(r"[^\w\s]", '', s)                # Format the inputted string without punctuation
        keyList = self.avlTree.get(s)
        if keyList == None:                      # Return the frequency count.
            return 0
        else:
            return len(keyList)

    def _provideLocations(self, wordsInOrder, word):

        # Function Description: Create an AVL Tree to store the words as specified.
        # Parameters: self (The instance of the object), wordsInOrder (The words as they appear in the file), 
        # word (The word to be found)
        # Returns: wordLoc (The location of the words for where they appear) # Throws: None

        wordLoc = []
        for idx, val in enumerate(wordsInOrder):
            if (val != None):
                if (val == word):
                    wordLoc.append(idx)
                    wordsInOrder[idx] = None
        return wordLoc

    def _createAVLTree(self, wordsInOrder):
                
        # Function Description: Create an AVL Tree to store the words as specified.
        # Parameters: self (The instance of the object), wordsInOrder (The words as they appear in the file)
        # Returns: theAVLTree (The final AVL tree) # Throws: None

        theAVLTree = AVLTreeMap()
        for word in wordsInOrder:
            if (word != None):
                locs = self._provideLocations(wordsInOrder, word)       # Get locations of where each word appears in the file.
                theAVLTree.put(word, locs) 
        return theAVLTree

class WebpagePriorityQueue:

    def __init__(self, query, webPageSet):

        # Function Description: Init the WebpagePriorityQueue. Accept the users query and the the set of webpages.
        # Parameters: self (The instance of the object), query (User's query), webPageSet (The set of web pages)
        # Returns: None # Throws: None

        self.query = query                                              # Qu: 1.4.2 Store the query value 
        self.maxHeap = self._createMaxHeap(query, webPageSet)           # Qu: 1.4.1 The max heap.
        self.webPages = webPageSet                                      # The web page set stored if needed later.

    def _findWebPageValue(self, query, webPage):

        # Function Description: Find the priority value of the web page 
        # Parameters: self (The instance of the object), query (User's query), webPage (A single web page)
        # Returns: val (The number of times the query words appear in the web page) # Throws: None

        line = query.lower()                     # Lower all the case and remove unnecessary symbols.
        line = re.sub(r"[^\w\s]", '', line)
        getWords = line.split()
        totalCount = 0
        for i in getWords:
            totalCount += webPage.getCount(i)                            #webPage.wordCount[i]
        return totalCount

    def peek(self):                     # Qu: 1.4.3

        # Function Description: Return the top of the heap array.
        # Parameters: self (The instance of the object)
        # Returns: (The top of the heap) # Throws: None  

        if (len(self.maxHeap) <= 1):       # The list does not contain values, return none.
            return None
        else:
            return self.maxHeap[1]         # This is the first value in the list.

    def poll(self):                     # Qu: 1.4.4

        # Function Description: Return the top of the heap array AND remove the value from the heap.
        # Parameters: self (The instance of the object)
        # Returns: (The top of the heap) # Throws: None  

        highestPriority = self.maxHeap[1]
        length = len(self.maxHeap)  
        if len(self.maxHeap) == 2:
            return self.maxHeap.pop(1)                             # Remove and return the top node if only one exists   
        if len(self.maxHeap) < 2:
            return None                                             # The list is empty             
        self.maxHeap[1] = self.maxHeap.pop(length - 1)            # Replace the top node with the last value of the array.
        length -= 1
        parentLoc = 1
        childOne = parentLoc * 2
        childTwo = parentLoc * 2 + 1 
        while (childOne < length):                                  # Propogate downwards to recalibrate the entire heap
            if (childTwo >= length):                                # Signifies the end of the heap.                   
                if (self.maxHeap[childOne].queryValue > self.maxHeap[parentLoc].queryValue):          # Case One: A single left child that is bigger.
                    buffer = self.maxHeap[parentLoc]
                    self.maxHeap[parentLoc] = self.maxHeap[childOne]
                    self.maxHeap[childOne] = buffer                             
                return highestPriority                              # The tree is fully calibrated since the right child D.N.E, we have reached the end.
            if (self.maxHeap[childOne].queryValue > self.maxHeap[parentLoc].queryValue and self.maxHeap[childOne].queryValue > self.maxHeap[childTwo].queryValue):          # Case Two: Two children, the left is bigger
                buffer = self.maxHeap[parentLoc]
                self.maxHeap[parentLoc] = self.maxHeap[childOne]
                self.maxHeap[childOne] = buffer
                parentLoc = childOne                                # Move the propogation downward
                childOne = parentLoc * 2
                childTwo = parentLoc * 2 + 1
            elif (self.maxHeap[childTwo].queryValue > self.maxHeap[parentLoc].queryValue and self.maxHeap[childTwo].queryValue > self.maxHeap[childOne].queryValue):        # Case Three: Two children, the right is bigger
                buffer = self.maxHeap[parentLoc]
                self.maxHeap[parentLoc] = self.maxHeap[childTwo]
                self.maxHeap[childTwo] = buffer
                parentLoc = childTwo                                # Move the propogation downward
                childOne = parentLoc * 2
                childTwo = parentLoc * 2 + 1
            else:                                                   # Case Four: The parent is bigger than its children, heap is now legal.
                break
        return highestPriority

    def _insertValue(self, page, heapArray):

        # Function Description: Insert a new value into the heap array.
        # Parameters: self (The instance of the object), page (The page to insert into the queue), heapArray (The heap to modify)
        # Returns: None # Throws: None

        heapArray.append(page)                             # Insert the value at the end of the list, regardless of position. (The first value in the array does not matter)
        childPos = len(heapArray) - 1                # Start at the end of the array where the value was inserted
        while childPos > 1:                          # We desire to avoid the first value.
            parentPos = childPos // 2
            if heapArray[parentPos].queryValue < heapArray[childPos].queryValue:        # Find the appropriate node to insert the new value. Once found switch the value.
                buffer = heapArray[childPos]
                heapArray[childPos] = heapArray[parentPos]
                heapArray[parentPos] = buffer
            #?else:
            childPos = parentPos          # Traverse upwards within the list. (We only focus on one side of the tree.)

    def _createMaxHeap(self, query, webPageSet):

        # Function Description: Create the intial max heap after the intialisation of the object.
        # Parameters: self (The instance of the object), query (User's query), webPageSet (All the webpages)
        # Returns: webPageMaxHeap (The max heap based on query importance) # Throws: None

        maxHeap = [None]                            # Intialise the max heap with a 0 in location 0. This value will never be used.
        for page in webPageSet:                     # Find the web page value of each web page.
            page.queryValue = self._findWebPageValue(query, page)           # Set the value in the web page object which will be used to prioritise the pages.
            self._insertValue(page, maxHeap)
        return maxHeap

    def reheap(self, newQuery):                   # Qu: 1.4.5

        # Function Description: Takes in a new query and reheaps the priorty queue.
        # Parameters: self (The instance of the object), newQuery (User's new query)
        # Returns: None # Throws: None

        if (newQuery != self.query):
            self.maxHeap = self._createMaxHeap(newQuery, self.webPages)
            self.query = newQuery

class ProcessQueries:

    def __init__(self, webPageFolder, queryFile, userLimit):

        # Function Description: Init the ProcessQueries. Process text files into webpages and read in the query file.
        # Parameters: self (The instance of the object), webPageFolder (Folder with the web pages files), 
        # queryFile (The file with all the queries), userLimit (The number of webpages to print)
        # Returns: None # Throws: None

        self.webPageIndexList = self._createWebPageObject(webPageFolder)
        self.queryList = self._createQueryList(queryFile)
        self.userLimit = userLimit
        self._printResultingQueries(self.webPageIndexList, self.queryList, self.userLimit)

    def _createWebPageObject(self, folderName):

        # Function Description: Read folder of web pages into a web page set.
        # Parameters: self (The instance of the object), folderName (Folder with web pages)
        # Returns: webPageSet (The web page set) # Throws: None

        webPageSet = []                       # Create web pages from the folder.
        for i in os.listdir(folderName):
            webPageSet.append(WebPageIndex(folderName + '\\' + i))
        return webPageSet

    def _createQueryList(self, queryFile):

        # Function Description: Read file and put each query into an element in a list.
        # Parameters: self (The instance of the object), queryFile (File with queries)
        # Returns: queries (List of queries) # Throws: None

        with open(queryFile) as f:
            queries = f.readlines()
        queries = [x.strip() for x in queries]              # Strip all new line characters
        return queries

    def _stripFileName(self, fileName):

        # Function Description: Strip the path to only the file name.
        # Parameters: self (The instance of the object), fileName (The full path name), 
        # Returns: None # Throws: None

        counter = 1
        while (fileName[(counter) * -1:][0] != '\\'):
            counter += 1
        return fileName[(counter) * -1:]

    def _printResult(self, pagePriorityQueue, limit):

        # Function Description: Print the priority queue based on the limit and the query used.
        # Parameters: self (The instance of the object), pagePriorityQueue (The files from the queue), 
        # limit (The number of files to print)
        # Returns: None # Throws: None

        print("The Query Executed: " + pagePriorityQueue.query)
        for i in range(0, limit):                 # Gather every web page and print the web page name and the number of times the query appears.
            popPage = pagePriorityQueue.poll()
            if popPage.queryValue != 0:
                print("File Priority Num: " + str(i + 1), end="     :     ")
                print((self._stripFileName(popPage.fileName), popPage.queryValue))  
            else:
                break                             # End the search since no values were found in the next prioritised node.
        print(25 * "-----")

    def _printResultingQueries(self, pageIndexList, queries, limit):

        # Function Description: Execute each query and print the top query results.
        # Parameters: self (The instance of the object), pageIndexList (List of web pages), 
        # queries (The list of queries), limit (The number of queries to print)
        # Returns: webPageSet (The web page set) # Throws: None

        pagePriorityQueue = WebpagePriorityQueue(queries[0], pageIndexList)     # Intialise the first query
        self._printResult(pagePriorityQueue, limit)
        for qu in queries[1:]:           # Execute the remaining queries using the existing queries
            pagePriorityQueue.reheap(qu)
            self._printResult(pagePriorityQueue, limit)


def main():
    # Test Code For the AVL Tree -- Please Ignore
    """test = AVLTreeMap()
    test.put(15, "bob")
    test.put(20, "anna") 
    test.put(24, "tom") 
    test.put(10, "david") 
    test.put(13, "david") 
    test.put(7, "ben")
    test.put(30, "karen")
    test.put(36, "erin")
    test.put(25, "david")
    test.put(13, "nancy")"""

    # Test Code For the Max Heap Directory with web page files -- Please Ignore
    filesDir = r"C:\Users\micha\Documents\Queen's University\University_5\CISC_235\Assn_3_10134030_Michael_Krakovsky\Test_Files"
    queryFile = r"C:\Users\micha\Documents\Queen's University\University_5\CISC_235\Assn_3_10134030_Michael_Krakovsky\queries.txt"

    processQueries = ProcessQueries(filesDir, queryFile, 5)

if __name__ == '__main__':
    main()


