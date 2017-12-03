# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
currentval = 0
newval = 0
count = 0
for tag in tags:
    # Look at the parts of a tag
    #print 'TAG:',tag
    #print 'URL:',tag.get('href', None)
    #print 'Contents:',tag.contents[0]
    content = tag.contents[0]
    currentval = int(content)
    newval = newval + currentval
    count = count + 1

print 'Count ',count
print 'Sum ',newval
    #print 'Attrs:',tag.attrs
