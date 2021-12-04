# asking user to input their time
sec=int(input("enter the second"))

#converting sec into min  1min = 60 sec
min = int(sec/60)

#converting sec into hrs  1 hrs = 60*60 sec
hrs = int(sec/3600)

#converting sec into day  1 day = 60*60*24
day = int(sec/86400)

print (day, hrs , min)