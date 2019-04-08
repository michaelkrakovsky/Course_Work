module Assignment3 where
    -- Description: Complete the requirements set forth in assignment three.
    -- Author: Michael Krakovsky  
    -- Date: March 6, 2019
    -- Version: 1.0
    
-------------------------------------------------------------- Question 1 --------------------------------------------------------------
---------- Question 1.1: Items and Inventory ----------
----- 1.1.1 -----
-- The algebraic data type Item with two alternatives PhysicalItem and DigitalDownload
data Item = 
    -- Physical Item with the Item ID (Int), the Name (String), the Price (Float), the Inventory (Stock)
    PhysicalItem Int String Float Int |
    -- Digital Item with the Item ID (Int), the Name (String), the Price (Float), the File Link (String)
    DigitalDownload Int String Float String

----- 1.1.2 -----
-- Using 'instance' to customising the show function
instance Show Item where
    show (PhysicalItem id name price inventory) =
        "\n" ++ (show name) ++ " (" ++ (show id) ++ ") \n$" ++ (show price) ++ "\n" ++ (show inventory) ++ " in stock\n"
    
    show (DigitalDownload id name price fLink) =
        "\n" ++ (show name) ++ " (" ++ (show id) ++ ") \n$" ++ (show price) ++ "\n" ++ "Link: " ++ fLink ++ "\n"

----- 1.1.3 -----
-- getID and getPrice to return the Item's ID and price, respectively

getID :: Item -> Int
getID (PhysicalItem id _ _ _) = id
getID (DigitalDownload id _ _ _) = id

getPrice :: Item -> Float
getPrice (PhysicalItem _ _ price _) = price
getPrice (DigitalDownload _ _ price _) = price

----- 1.1.4 -----
-- A type synonym for a list of items named inventory.
type Inventory = [Item]

-- Test Code: Please Ignore --
smallTShirt = PhysicalItem 3 "Small T-shirt" 19.99 2
mediumTShirt = PhysicalItem 5 "Medium T-shirt" 19.99 10
largeTShirt = PhysicalItem 7 "Large T-shirt" 19.99 3

track1 = DigitalDownload 9 "Track 1" 0.99 "/track-1"
track2 = DigitalDownload 10 "Track 2" 0.99 "/track-2"
track3 = DigitalDownload 11 "Track 3" 0.99 "/track-3"
track4 = DigitalDownload 14 "Track 4" 0.99 "/track-4"

inventory :: Inventory
inventory = [smallTShirt, mediumTShirt, largeTShirt, track1, track2, track3, track4]

---------- Question 1.2: Items and Inventory ----------
----- 1.2.1 -----
-- Algebraic data type Order
data Order =
    -- Order type with the order's ID (Int), the order's date (String), items purchased ([Item])
    Order Int String [Int]

----- 1.2.2 -----
-- Creating a custom show for Order
instance Show Order where 
    show (Order id date orderList) =
        "\n" ++ (show id) ++ " (" ++ date ++ ") \n" ++ "Purchased: " ++ (show orderList) ++ "\n"

----- 1.2.3 -----
-- A type synomyn Sales for a list of Orders
type Sales = [Order]

-- Test Code: Please Ignore --
order101 = Order 101 "01/01/2019" [3,7]
order104 = Order 104 "10/01/2019" [9,10,11]
order105 = Order 105 "12/02/2019" [5]
order109 = Order 109 "25/02/2019" [9,10,11,14]

sales :: Sales
sales = [order101, order104, order105, order109]

-------------------------------------------------------------- Question 2 --------------------------------------------------------------

-- Description: Displays an improved version of the Inventory and Sales type synonyms.
-- Parameters: Type variable accepting any list
-- Returns: None -- Throws: None

displayList :: Show a => [a] -> IO ()
displayList x = putStrLn (foldl (++) "" (map show x))

-------------------------------------------------------------- Question 3 --------------------------------------------------------------
---------- Question 3.1: Total Cost of An Order ----------

-- Description: Returns the total cost of the Items in that Order.
-- Parameters: ord (The order given of type Order), inv (The inventory of the order)
-- Returns: Total Cost of the order -- Throws: None 

calculateTotal :: Order -> Inventory -> Float
calculateTotal ord inv = sum (map getPrice itemsBought)             -- Get the items bought, then get the item information, finally sum the prices
    where 
        orNums = (\(Order _ _ c)->c) ord                        
        itemsBought = filter (flip elem orNums . getID) inv

---------- Question 3.2: Total Cost of An Order ----------

-- Given Helper Function
roundCurrency :: Float -> Float
roundCurrency c = (fromIntegral (round (c * 100))) / 100

-- Description: Returns a float with the total amount of PayPal fees owing for all orders in sales.
-- Fees are noted from the website as: 2.9% of the transaction amount plus $0.30 CAD
-- Parameters: sal (The sales of the merchant), inv (The inventory of the order)
-- Returns: Total Cost of the order -- Throws: None 

payPalFees :: Sales -> Inventory -> Float
payPalFees sal inv = roundCurrency (sum (map (\x->0.3 + x*0.029) getAllSales))    -- Convert the orders into sales, then find the fees, finally sum
    where
        getAllSales = map (flip calculateTotal inv) sales               

