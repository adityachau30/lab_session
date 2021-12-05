a = int(input("enter a number"))
b = int(input("enter b number"))
c = int(input("enter c number"))

if a<b and c>a:
    print("a is smallest")
elif b<a and b<c:
    print("b is smallest")
else:
    print("c is smallest")