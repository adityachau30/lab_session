#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements 

num =[1,2,3,4,5,6,7,8]

for i in num:
    if i!=num[0] and i!=num[4] and i!=[5]:
        print(i)
