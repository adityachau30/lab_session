# asking uster to input time in minute
num = int(input("enter the time"))

# converting min into hour ex. 130/60 = 2.10 hour
hour = int(num/60)

# converting min into min ex 130/60 = 2.10 (10 min) is reminder
min = (num%60)


print(f"the hours is {hour}")
print(f"the minute is {min}")


