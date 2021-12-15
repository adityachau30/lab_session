a = input("enter any letter or any number")
i = len(a)
k = i+1
w = ""
for j in range(1,k):
    l = i-j
    w = w + a[l]
print(w)
