math = int(input("enter your math marks"))
science = int(input("enter your science marks"))
social = int(input("enter your social marks"))
computer = int(input("enter your computer marks"))


total_marks = math+science+social+computer
total_per = (total_marks/400)*100

if total_per>=70:
    print("you got distinction")
elif total_per>=60 and total_per<=70:
    print("you got first devision")
elif total_per>=40:
    print("you got second devision")
else :
    print("you are fail")
