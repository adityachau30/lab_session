import pdb

bike1 = "yamaha"
bike1_price = 25000

bike2 = "honda"
bike2_price = 50000

set_track.pdp()
name = input("enter your name")
choose = int(input("press 1 for yamaha and 2 for honda:"))
print(f"hello {name}")

if choose ==1:
    print(f"{bike1}will cost you {bike1_price}")
elif choose ==2:
    print(f"{bike2_price}will cost you {bike2+2000}")
else:
    print("press only 1 or 2")