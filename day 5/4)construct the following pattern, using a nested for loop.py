for i in range(5):
    for j in range(i+1):
        print('*',end='*')
    print()
while i <= 7 :
    j = 7
    while j >= i:
        print("*", end = "*")
        j -= 1
    print()
    i += 1