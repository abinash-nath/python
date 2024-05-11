# break -- comes out of loop altogether
#continue -- skips the current iteration and moves to next
# pass -- Acts as a placeholder and does nothing

#Program that will be on infite loop till name is given
# while True:
#     name =input("Enter a name:")
#     if name != "":
#         print("the name entered is: ",name)
#         break

####################################

#Phone number formatting
# phone = "934-287-3425"
# for i in phone:
#     if i == "-":
#         continue
#     print(i,end="")

####################################

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)
        