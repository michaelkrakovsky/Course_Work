# Name: Michael Krakovsky (Student ID: 10134030)
# Date: Jan 25, 2018
# Description: Complete the requirements set forth in Assignment 1.2. (i.e. Sorting Algorithms)
# Version: 1.0   

import random               
import time

# Description: Merge Sort custom made to sort the given list
# Parameters: listToSort (The address of the list that will be sorted), sInd (The starting Index), eInd (The ending Index)
# Returns: None
# Throws: None

def mergeSort(listToSort): 
    if len(listToSort) > 1:                     # Continue to break down the array if it is greater than one (Skip the search if there is one value in the array)
        mInd = len(listToSort) // 2             # The midpoint of the array 
        leftSide = listToSort[:mInd]            # Dividing the array elements into the left side and right side
        rightSide = listToSort[mInd:] 
        mergeSort(leftSide)                     # Recursively renter the array  
        mergeSort(rightSide) 
  
        i = 0           # Keeps track of where you are in the left array
        j = 0           # Keeps track of where you are in the right array
        k = 0           # Keeps track of where you are in the final array

        while i < len(leftSide) and j < len(rightSide):        # Copy the data into either the left array or right array
            if leftSide[i] < rightSide[j]:                     # Insert the lowest value first until all values are submitted 
                listToSort[k] = leftSide[i] 
                i = i + 1                                       
            else: 
                listToSort[k] = rightSide[j] 
                j = j + 1
            k = k + 1                                           # Increase final array index after value is inserted           
        while i < len(leftSide):                                # Insert any remaining values into the list (leftside)
            listToSort[k] = leftSide[i] 
            i = i + 1
            k = k + 1
        while j < len(rightSide):                               # Insert any remaining values into the list (rightside)
            listToSort[k] = rightSide[j] 
            j = j + 1
            k = k + 1 

# Description: Custom made binary search that identifies whether an item is present in the list.
# Parameters: item (The target number to search for), listToSearch (The address of the list to be searched, the list will be searched)
# Returns: True or False (True = The item is in the list, False = The item is not in the list)
# Throws: None

def binarySearch(item, listToSearch):
    low = 0                                      # Track where the scope of the search should be
    high = len(listToSearch) - 1
    mid = 0
    while (low <= high):                         # Search until the indexes overlap
        mid = low + (high - low) // 2            # Reset the mid every time
        if (item == listToSearch[mid]):          # Check whether the mid is the desired value
            return True
        elif (item > listToSearch[mid]):         # Adjust the index value to reduce the size of the scope
            low = mid + 1
        else:
            high = mid - 1
    return False

# Description: Brute force linear search... nothing special, This is the implementation of algorithm one from the assignment
# Parameters: item (The target number to search for), listToSearch (The address of the list to be searched, the list will be searched)
# Returns: True or False (True = The item is in the list, False = The item is not in the list)
# Throws: None

def bruteForceSearch(item, listToSearch):
    for i in listToSearch:
        if (i == item):                         # If the item is in the list, return True
            return True
    return False

# Description: Return a list filled with n number of random values between the ranges of 10 - 100000
# Parameters: n (The numbers you want in your list)
# Returns: True or False (True = The item is in the list, False = The item is not in the list)
# Throws: None

def generateRandomList(n):
    randomList = []
    for x in range(0, n):
        randomList.append(random.randint(10, 100000))                   # Pick random numbers within the range 10 - 100000
    return randomList                                                   # Return the random list

# Description: Return a list of size k / 2 that will provide a list of values that already exist within the array. The values are plucked randomly
# Parameters: listToPluck (The list to pluck random numbers from), k (Number of target values)
# Returns: randomValues (The list with the random values)
# Throws: None

def provideExistingNums(listToPluck, k):
    randomValues = []
    k = k // 2                   # We only want half the target values to be known 
    for x in range(0, k):
        randomValues.append(listToPluck[random.randint(0, len(listToPluck) - 1)])                     # Select a random value from within the list
    return randomValues

# Description: Recieve a list with n values, a list with values not in the list, and a list with values in the list and execute the algorithm 1
# Parameters: listToExecute (The target list to be subjugated to tests), inVals (Values in the list), nonVals (Values not in the list)
# Returns: None
# Throws: None

def runAlgoOne(listToExecute, inVals, nonVals):
    for i in inVals:                            # Search for values that are in the array
        bruteForceSearch(i, listToExecute)
    for i in nonVals:                           # Run the search knowing the values that are not in the array
        bruteForceSearch(i, listToExecute)     

# Description: Recieve a list with n values, a list with values not in the list, and a list with values in the list and execute the algorithm 2
# Parameters: listToExecute (The target list to be subjugated to tests), inVals (Values in the list), nonVals (Values not in the list)
# Returns: None
# Throws: None

def runAlgoTwo(listToExecute, inVals, nonVals):
    mergeSort(listToExecute)                    # Sort the list prior to running (Should not matter since algorithm will not be run anymore)
    for i in inVals:                            # Search for values that are in the array
       binarySearch(i, listToExecute) 
    for i in nonVals:                            # Run the search knowing the values that are not in the array
       binarySearch(i, listToExecute)

# Description: Recieve a dictionary with runtimes and covert each summation within the dictionary into averages
# Parameters: dictionaryToConv (The dictionary with the sums), numIters (The number of times the program was run)
# Returns: None
# Throws: None

def convertToAvg(dictionaryToConv, numIters):
    for key in dictionaryToConv:
        dictionaryToConv[key] = dictionaryToConv[key] / float(numIters)                 # Ensure the float form is maintained

def main():
    sizeLists = [1000, 2000, 5000, 10000]               # The size of the list of random numbers.
    randomValues = []                                   # Here are values that already exist in the list.
    randomList = []                                     # The list with the random numbers.
    algoOneTimes = {}                                   # The times of both algorithms.
    algoTwoTimes = {}
    numIters = 500                                     # Keeps track of the number of iterations run
    k = 200                                             # The number of values to search for. (Half will be in the list, half will not be in the list)
    
    if (k % 2 == 0):                                    # Guard against an odd k value. The single value produced from the remainder of mod 2 will be put in the valuesNotInList array.
        valuesNotInList = [-1] * (k // 2)
    else:
        valuesNotInList = [-1] * ((k // 2) + 1)
    
    counter = 0                                         # Control the number of iterations within the list
    while (counter < numIters):
        for i in sizeLists:
            randomList = generateRandomList(i)                                      # Generate the random list.
            randomValues = provideExistingNums(randomList, k)                       # Generate existing values from the list.
            startTime = time.time()                                                 # Time the first algorithm
            runAlgoOne(randomList, randomValues, valuesNotInList)
            endTime = time.time()
            if (i in algoOneTimes):                         # Record time into a dictionary and find summation of all the run times
                algoOneTimes[i] = algoOneTimes[i] + (endTime - startTime)
            else:
                algoOneTimes[i] = (endTime - startTime)

            startTime = time.time()                                                 # Time the second algorithm
            runAlgoTwo(randomList, randomValues, valuesNotInList)
            endTime = time.time()
            if (i in algoTwoTimes):
                algoTwoTimes[i] = algoTwoTimes[i] + (endTime - startTime)
            else:
                algoTwoTimes[i] = (endTime - startTime)
        counter += 1                                                               # Decrease counter
        if (counter % 50 == 0):
            print("Number of times iterated: " + str(counter))                 # Friendly message to remind user of loaction in algorithm
    
    convertToAvg(algoOneTimes, numIters)                                        # Convert to average values
    convertToAvg(algoTwoTimes, numIters)
    print(str(numIters) + ": When K equals for algo One " + str(k) + " , the times are: " + str(algoOneTimes))        # Display the times of the algorithms
    print(str(numIters) + ": When K equals for algo Two " + str(k) + " , the times are: " + str(algoTwoTimes))

if __name__ == '__main__':
    main()