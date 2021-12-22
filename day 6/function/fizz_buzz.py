# Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “Fizz”. 
# If it is divisible by 5, it should return “Buzz”. 
# If it is divisible by both 3 and 5, it should return “FizzBuzz”. 
# Otherwise, it should return the same number.

num = int(input("Enter any Number:"))

def fizz_buzz(num1):
    if num1%3 == 0 and num1%5 == 0 :
        print("FizzBuzz")


    elif num1%5 == 0:
        print("Buzz")

    elif num1%3 == 0:
        print("Fizz")
    else:
        print(num1)

fizz_buzz(num)