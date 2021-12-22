#  Write a Python function to find the Max of three numbers.

num1 = int(input("Enter any Number:"))
num2 = int(input("Enter any Number:"))
num3 = int(input("Enter any Number:"))


def max(num1,num2,num3):
    

     if num1>num2 and num1>num3:
        print(f"The greatest number is  {num1}")


     elif num2>num1 and num2>num3:
        print(f"The greatest number is  {num2}")


     elif num3>num1 and num3>num2:
        print(f"The greatest number is  {num3}")
     else:
        print("Error")
max(num1,num2,num3)