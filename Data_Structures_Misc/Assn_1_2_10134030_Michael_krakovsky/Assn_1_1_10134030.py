# Name: Michael Krakovsky (Student ID: 10134030)
# Date: Jan 16, 2018
# Description: Complete the requirements set forth in Assignment 1.1. (i.e. Create the bag object)
# Version: 1.0

import random

class Bag():
    def __init__(self):
        self.bagItems = []          # Create an empty list that stores data items

    def add(self, item):
        self.bagItems.append(item)          # Append the item to the list

    def remove(self, item):
        try:
            self.bagItems.remove(item)
            return True          # Returns true if item was removed else return false
        except (ValueError):
            return False
    
    def contains(self, item):
        if item in self.bagItems:           # Brute search to see whether the bag contains the item
            return True
        else:
            return False
    
    def numItems(self):
        return len(self.bagItems)           # Return the number of items within the bag

    def grab(self):
        return random.choice(self.bagItems)     # Returns a random item

    def __str__(self):
        return " ".join(str(x) + ' ||' for x in self.bagItems)             # Convert the bag into a string and return (|| separates the contents)


def main():
    # Test Code
    myBag = Bag()
    # Test the add method 
    myBag.add(30)
    myBag.add("A string")
    myBag.add('c')
    myBag.add([4, 3, 4, 5])
    myBag.add(34.3434)

    # Test the __str__ method
    print(myBag.__str__())        # Did the bag add everything properly and can it print?
    
    # Test the remove method
    myBag.remove(23424)
    print(myBag.__str__())    # Nothing should happen
    myBag.remove("A string")
    print(myBag.__str__())    # Should be removed
    print(type(myBag.__str__()))            # Ensure the type is a string 

    # Test the contains method
    print(myBag.contains([4, 3, 4, 5]))     # Print True if Correct
    print(myBag.contains([4, 3, 4, 3]))     # Print False if Correct

    # Test the numItems method
    print(myBag.numItems())             # Should print 4 

    # Test the grab method
    print(myBag.grab())             # Prints a random item from the bag
    print(myBag.grab())

if __name__ == '__main__':
    main()