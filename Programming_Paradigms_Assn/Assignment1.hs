-- Description: Complete the requirements set forth in the assignment description.
-- Author: Michael Krakovsky  
-- Date: January 23, 2019
-- Version: 1.0

module Jan23 where

----------------------------------------------- QUESTION 1 -----------------------------------------------

-- Description: Helper function that takes a single integer and either returns its binary value
-- Parameters: numInSeq (Integer: The position in the binary string) binaryNumber (Integer: The actual binary digit)
-- Returns: Integer (The corresponding binary digit)
-- Throws: None

binaryValue :: Integer -> Integer -> Integer
binaryValue binaryNumber numInSeq
    | binaryNumber == 0 = 0                         -- First Base Case: The final number is 0, return 0.
    | binaryNumber == 1 = 2 ^ numInSeq              -- Second Base Case: The final number is 1, calculate appropriate value.
    | ((mod binaryNumber 10 /= 0) && (mod binaryNumber 10 /= 1)) = error "There is an element that is neither 1 or 0."          -- Detect an element that is neither 0 nor 1. (mod is modular)
    | (mod binaryNumber 10 == 1) = (2 ^ numInSeq) + binaryValue (quot binaryNumber 10) (numInSeq + 1)           -- Calculate the appropriate value in the binary string depending on its location
    | otherwise = 0 + binaryValue (quot binaryNumber 10) (numInSeq + 1)             -- Nothing happens except we move the string forward (quot is essentially integer division)

-- Description: Initiating function that checks initial integer and sends the integer to be converted  
-- Parameters: binaryNumber (Integer: The actual binary digit)
-- Returns: Integer (The corresponding binary digit)
-- Throws: An error when the digit is neither 1 or 0

convertFromBinary :: Integer -> Integer
convertFromBinary binaryNum
    | binaryNum >= 0 = binaryValue binaryNum 0                      -- Check if the int is negative and begin the conversion                 
    | otherwise = error "You cannot enter a negative number!"

----------------------------------------------- QUESTION 2 -----------------------------------------------

-- Description: The recursive function that implements the binary search. (Floor Implementation)
-- Parameters: highBound (Integer: The max bound in the binary search), lowBound (Integer: The min bound in the binary search), 
-- midBound (Integer: The midpoint of the algorithm (Integer: Where the comparison will be incurred)), target (Integer: The value that is being searched),
-- numSteps (Integer: The number of steps it takes to find the value)
-- Returns: Integer (The number of searches required to find the value)
-- Throws: None 

findValue :: Integer -> Integer -> Integer -> Integer -> Integer -> Integer
findValue highBound lowBound midBound target numSteps
    | (midBound == target)  = (numSteps + 1)                    -- End the recursion when the value is found
    | (target < midBound) = findValue (midBound - 1) lowBound (quot ((midBound - 1) + lowBound) 2) target (numSteps + 1)            -- Shift the scope downwards and add a step
    | otherwise = findValue highBound (midBound + 1) (quot (highBound + (midBound + 1)) 2) target (numSteps + 1)             -- Shift the scope upwards and add a step


-- Description: Initiating function that checks initial parameters and sends the parameters to be calculated in the binary search
-- Parameters: target (Integer: The value to be searched) highBound (Integer: The upper bound of the list)
-- Returns: Integer (The number of searches required to find the value)
-- Throws: An error when the input is out of range, or one of the parameters is negative 

countStepsInBinarySearch :: Integer -> Integer -> Integer
countStepsInBinarySearch target highBound
    | ((target < 1) || (highBound < 1)) = error "The values must be greater than 0!"     -- Prevent negative and 0 values
    | (target > highBound) = error "The search value is out of range!"                   -- Prevent out of bounds errors
    | otherwise = findValue highBound 1 (quot (highBound + 1) 2) target 0               -- Begin the recursive chain

----------------------------------------------- QUESTION 3 -----------------------------------------------

-- Description: The representation of the nested for loop that tracks both the outer loop and the inner loop position.
-- Parameters: outerLoopPos (Integer: The position of the outer loop), innerLoopPos (Integer: The position of the inner loop), 
-- limit (Integer: The limit entered by the user), count (Integer: The value that tracts the iteration) 
-- Returns: Integer (The count variable)
-- Throws: None 

nestedLoop :: Integer -> Integer -> Integer -> Integer -> Integer
nestedLoop outerLoopPos innerLoopPos limit count
    | (innerLoopPos >= limit) = count               -- The end of the loop
    | (outerLoopPos >= limit) = nestedLoop (innerLoopPos + 1) (innerLoopPos + 1) limit count       -- The outer loop has reached its limit, increase the inner loop and move forward.
    | otherwise = nestedLoop (outerLoopPos + 1) innerLoopPos limit (count + 1)                 -- Models the behaviour of the inner loop

-- Description: Accepts the user input and feeds the value to the helper function.
-- Parameters: limit (Integer: The limit entered by the user)
-- Returns: Integer (The count variable)
-- Throws: An error when the number is negative 

countNestedForwards :: Integer -> Integer
countNestedForwards limit 
    | (limit < 0) = error "You cannot enter a negative number!"        -- Ensure the number is above 0
    | otherwise = nestedLoop 0 0 limit 0          -- Commence the loop