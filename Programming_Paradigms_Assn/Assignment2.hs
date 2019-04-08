module Assignment2 where
-- Description: Complete the requirements set forth in the assignment two description.
-- Author: Michael Krakovsky  
-- Date: February 6, 2019
-- Version: 1.0

-------------------------------------------------------------- Question 1 --------------------------------------------------------------

-- Description: Accepte a list of lists composed of integers and return a string format
-- Parameters: (head : tail) ([[Int]]: The 2-D array containing integers)
-- Returns: The formatted string
-- Throws: None

getFormattedString :: [[Int]] -> String
getFormattedString (head : tail)
    | tail == [] = show head                                       
    | otherwise = show head ++ "\n" ++ getFormattedString tail      -- Compose the string with newline characters in a recursive function

-- Description: Accept a list of lists and print each list on a new line.
-- Parameters: listOfLists (A list of lists to display in the output)
-- Returns: None (But there is the IO of the string itself)
-- Throws: None

showFormattedString :: [[Int]] -> IO()
showFormattedString [] = putStrLn("")                                        
showFormattedString listOfLists = putStrLn (getFormattedString listOfLists)    

-------------------------------------------------------------- Question 2 --------------------------------------------------------------

-- Description: Maintain a stack that tracks brackets while traversing through the expression
-- Parameters: (x : xs) (Traverse through the expression), currentStack (Track the order of the brackets) 
-- Returns: Bool (Depending whether the expression is legal)
-- Throws: None

formStack :: String -> String -> Bool
formStack (x : xs) currentStack
    | ((xs == "") && (x == '(')) = False                                                                         -- Multiply checks that will determine the state at the stacks end
    | ((x == ')') && ((currentStack == "") || (head currentStack /= '('))) = False                               
    | ((xs == "") && (x == ')')) = (head currentStack == '(' && (tail currentStack) == "")                      
    | ((xs == "") && ((x /= '(') || (x /= ')')) && (currentStack == "")) = True                                   
    | ((xs == "") && ((x /= '(') || (x /= ')')) && (currentStack /= "")) = False
    | (x == '(') = formStack xs ("(" ++ currentStack)                                                            -- Uses cases that will happen mid-stack                
    | ((x == ')') && (head currentStack == '(')) = formStack xs (tail currentStack)                              
    | otherwise = formStack xs currentStack                                                                      

-- Description: Accept userinput, ensure it is non-empty and pass to the helper function
-- Parameters: userInput (The user input) 
-- Returns: Bool (Depending whether the expression is legal)
-- Throws: None

parenthesesAreBalanced :: String -> Bool
parenthesesAreBalanced userInput
    | (userInput /= "") = formStack userInput ""                -- Begin to analyse the string
    | otherwise = True

-------------------------------------------------------------- Question 3 --------------------------------------------------------------

------------- Data, Please Ignore -------------
-- The User tuple is of the form (ID, Name)
type User = (Int, String)

-- The Content tuple is of the form (ID, Title)
type Content = (Int, String)

-- The Viewing tuple is of the form (User ID, Movie ID, Timestamp)
type Viewing = (Int, Int, Int)

-- The Rating tuple is of the form (User ID, Movie ID, Rating)
type Rating = (Int, Int, Int)

-- This is sample content for the sample output and for you to test with.
-- You should absolutely add your own values to these lists to test beyond the
-- data here.
userList = [(4, "SJW"), (73, "AA"), (34, "TB")]

contentList = [(12, "Dirk Gently's Holistic Detective Agency"), (15, "Black Panther"), (81, "Brooklyn 99"), (37, "The Good Place"), (51, "Iron Fist"), (43, "Solo"), (76, "The Vietnam War"), (29, "Secret City"), (60, "Ugly Delicious")]

viewingList = [(4, 12, 1516456852), (4, 15, 1537542147), (4, 81, 1504116489), (4, 37, 1541498412), (4, 51, 1508360754), (4, 76, 1516356148), (4, 29, 1536539720), (4, 60, 1508965289), (73, 51, 1517365941), (73, 60, 1516365257), (73, 43, 1536420631), (34, 60, 1507471645), (34, 15, 1509459643) ]

ratingList = [(4, 12, 5), (4, 15, 5), (4, 81, 5), (4, 37, 5), (4, 51, 2), (4, 43, 3), (4, 76, 5), (4, 29, 5), (4, 60, 3), (73, 51, 5), (73, 60, 4), (73, 43, 5), (34, 60, 1), (34, 15, 5)]

------------- Data Above, Please Ignore -------------

---------- 3.1 ----------

-- Description: Helper function that uses list comprehension
-- Parameters: contentID (The movie ID)  
-- Returns: The average of the list floored (Int)
-- Throws: None 

getAvg :: [Int] -> Int
getAvg [] = error "Error: There are no ratings for this movie!"
getAvg a = floor (realToFrac (sum a) / (realToFrac (length a)))

-- Description: Find the average rating of the specified movie id
-- Parameters: contentID (The movie ID)  
-- Returns: The average of the list floored (Int)
-- Throws: An error for provided a negative number for the content ID 
 
averageRating :: Int -> Int
averageRating contentID 
    | contentID < 0 = error "Error: The ID must be greater than 0."         
    | otherwise = getAvg [rating | (userID, movieID, rating) <- ratingList, contentID == movieID]         -- Essentially execute a query that retrieves the tuples that match the specified movie ID

---------- 3.2 ----------

-- Description: Get movies that the user has already watched.
-- Parameters: userNumber (The user number)  
-- Returns: contentWatched (The content already watched)
-- Throws: None

getMoviesUserWatched :: Int -> [Content]
getMoviesUserWatched userNumber = contentWatched
    where
        videosWatched = [movieID | (userID, movieID, timestamp) <- viewingList, userID == userNumber]           
        contentWatched = [movie | movie <- contentList, elem (fst movie) videosWatched]                         -- Get the movie title with the ID's we acquired

-- Description: Get movies that the user has already watched.
-- Parameters: userNumber (The user number)  
-- Returns: The content that was already watched.
-- Throws: None

watchItAgain :: Int -> [Content]
watchItAgain userID
    | userID < 0 = error "Error: The ID must be greater than 0."                         
    | otherwise = getMoviesUserWatched userID

---------- 3.3 ----------

-- Description: Get new movies that the user should watch.
-- Parameters: userNumber (The user number)  
-- Returns: newContent (The suggested content)
-- Throws: None

getNewMovies :: Int -> [Content]
getNewMovies userNumber = newContent
    where
        videosWatched = [movieID | (userID, movieID, timestamp) <- viewingList, userID == userNumber]                                                   
        videosNotWatched = [movieID | (userID, movieID, timestamp) <- viewingList, (movieID `elem` videosWatched) == False && userID /= userNumber]     
        newContent = [movie | movie <- contentList, (fst movie `elem` videosNotWatched) && (averageRating (fst movie) >= 2) ]                           -- Narrow down the search to a movie rating for greater than 2 avg                 

-- Description: Get new movies that the user should watch.
-- Parameters: userID (The user number)  
-- Returns: newContent (The suggested content)
-- Throws: Ensure the user rating is greater than 0.

suggestionsForYou :: Int -> [Content]
suggestionsForYou userID
    | userID < 0 = error "Error: The ID must be greater than 0."            
    | otherwise = getNewMovies userID