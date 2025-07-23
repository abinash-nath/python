x = int(input("please enter your age:"))

if x<6:
    print("you are a child")
    if x<0:
        print("invalid age")
elif x>=6 and x<=25:
    print("you are at right age to start education")
else:
    print("you shold have started education long long back")