# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

#local variables
index = 0
ind = 0



url = raw_input('Enter - ')
count = int(raw_input('Enter count: '))
position = int(raw_input('Enter position: '))

#print out url enter by the user
print url

for i in range(count):
    for j in range(position):
        if j == position-1:
            #1 Input the url into the urllib.urlopen to get the list of all the html page
            #reading url enter by the user from keyboard
            html = urllib.urlopen(url).read()
    
            #2 pass it to Beautiful soap to tidy up the html page
            #passing url to be parsed by soap
            soup = BeautifulSoup(html)
    
            #3 retrieve anchor tags only
            # Retrieve all of the anchor tags
            tags = soup('a')
        
            #4 from the anchor tags remove the href and get only http address
            url = tags[position -1].get('href', None)
            print url
    
            #5 move three positions down starting from its current position
                # 5-1 Repeat steps 1-4 until however number of counts enter by the user
            
            
            #6 repeat step 1 - 5 for however number of counts passed by the user
         
 
