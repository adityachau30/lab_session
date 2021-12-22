# Write a Python program to reverse a string. 


int = input("Enter input a word ")

def reverse(int1):
    w = ""
    for j in range(1,len(int1)+1):
        l = len(int1)-j
        w = w + int1[l]
    return w

rev = reverse(int)
print(f"The Reverse string of {int} is: {rev}")