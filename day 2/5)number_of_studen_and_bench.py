a = int(input("enter the number of student in class a : "))
b = int(input("enter the nu,ber of student in class b : "))
c = int(input("enter the number of student in class c : "))

# 1 bench = 2 studnet
ab = int(a/2)
aab = int(a%ab)
a_bench = ab+aab

bb = int(b/2)
bbb = int(b%bb)
b_bench = bb+bbb

cb = int(c/2)
cbb = int(c%cb)
c_bench = cb+cbb

total_bench = a_bench + b_bench + c_bench

print(f"Total number of bench required is {total_bench}")