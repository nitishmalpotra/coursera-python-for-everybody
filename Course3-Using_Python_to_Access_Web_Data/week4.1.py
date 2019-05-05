'''
Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_228094.html (Sum ends with 56)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
'''


from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

html = urlopen('http://py4e-data.dr-chuck.net/comments_228094.html')

soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('td')

total = 0
for tag in tags:
    # Look at the parts of a tag
    line = str(tag)
    x = re.findall('[0-9]+',line)
    if len(x) > 0:
        for item in x:
            total += int(item)

print(total)
