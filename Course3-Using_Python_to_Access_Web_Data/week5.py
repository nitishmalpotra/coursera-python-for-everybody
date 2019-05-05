'''
Extracting Data from XML

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_228096.xml (Sum ends with 71)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
'''

from urllib.request import urlopen
import xml.etree.ElementTree as ET

# Read in XML from the URL
url = input('Enter location: ')
print ('Retrieving', url)
uh = urlopen(url)
data = uh.read()

# Convert the XML to a tree
tree = ET.fromstring(data)

# Print how many characters in the XML
print ('Retrieved',len(data),'characters')

# Get all of the count values
counts = tree.findall('.//count')

# Total all of the counts
total = 0
for item in counts:
    total += int(item.text)

print (total)
