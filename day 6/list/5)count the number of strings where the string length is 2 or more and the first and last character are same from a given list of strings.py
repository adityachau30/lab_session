#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
#  Sample List : ['abc', 'xyz', 'aba', '1221'] 
# Expected Result : 2 
list = ['abc', 'xyz', 'aba', '1221']

for first in list:
    start=(first[0])
    #print(start)

for last in list:
    end = last[-1]
    #print(end)


if first 