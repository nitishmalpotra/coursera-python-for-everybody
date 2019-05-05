'''
Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
'''

string = "X-DSPAM-Confidence:    0.8475";

colpos = string.find(':')
number = string[colpos+1:]
confidence = float(number)
print(confidence)
