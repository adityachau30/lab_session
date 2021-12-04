# asking user to enter weight in kg
mass = int(input("enter your mass in kg"))

#asking user to input their height in meter
height = int(input("enter your height in meter"))

# bmi = mass/height²
bmi = (mass/(height*height))

# \u00b2 = ²(square)
print("the bmi of body is {} kg/m\u00b2".format(bmi))