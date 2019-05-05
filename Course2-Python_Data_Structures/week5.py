'''
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)

dictionary_addresses = dict()

for line in handle:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        dictionary_addresses[words[1]] = dictionary_addresses.get(words[1],0) + 1

maximum = 0

for address in dictionary_addresses:
    if dictionary_addresses[address] > maximum:
        maximum = dictionary_addresses[address]
        maximum_address = address

print(maximum_address, maximum)
