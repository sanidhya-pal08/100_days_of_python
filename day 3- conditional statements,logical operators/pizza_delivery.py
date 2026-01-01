print("welcome to the pizza delivery")
bill=0
size=input("enter the size of the pizza S M or L")
pepperoni=input("do you want pepperoni? Y for yes and N for no")
extra_cheese=input("do you want cheese? Y for yes and N for no")
if size=="S":
    bill+=15
elif size=="M":
    bill+=20
elif size=="L":
    bill+=25
else:
    print("please enter either S M or L")
if pepperoni=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3
if extra_cheese=="Y":
    bill+=1
print(f"the total bill is {bill}$")