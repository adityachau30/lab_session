year =int(input("enter year"))

a = year%4
b = year%100
c = year%400

if (b==0 and a!=0 ):
    print("its not leap year")
else:
    print("its leap year")