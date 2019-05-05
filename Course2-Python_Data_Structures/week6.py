'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dictionary_hours = dict()

for line in handle:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        colpos = words[5].find(':')
        hour = words[5][:colpos]
        dictionary_hours[hour] = dictionary_hours.get(hour,0) + 1

lst = list()
for key, val in dictionary_hours.items():
    lst.append((key,val))

lst.sort()

for key, val in lst:
    print(key,val)
