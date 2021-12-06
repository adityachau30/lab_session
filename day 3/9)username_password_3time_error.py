un = str(input("enter username"))
ps = input("enter password")
for i in range(3):
    if int(ps) == 123:
        print("You have login successfully")
        break
else:
        print("Try again")
        ps=input("wrong,Please try again")
        for i in range(3):
            if int(ps) == 123:
                print("You have login successfully")
                break
        else:
            print("Try again")
            ps = input("wrong, Please try again")
            for i in range(3):
                if int(a) == 123:
                    print("You have login successfully")
                    break
            else:
                print("sorry, your account is blocked")