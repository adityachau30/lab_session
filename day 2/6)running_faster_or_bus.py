dis = 4
time = (4/25)*60
tt = time*20
timeA = (1/7)*60
timeB= (2/15)*60
timeC = (1/7)*60
totaltime = timeA+timeB+timeC
print("the total time to reach university by bus is : " , tt)
print("the total time to reach university by walkikng : " , totaltime)
if totaltime>tt:
    print("walking is faster to reach university")
else:
    print("going by bus if faster")