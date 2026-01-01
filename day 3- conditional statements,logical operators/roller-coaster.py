height=int(input("enter your height in cm\n"))
bill=0


age=int(input("enter your age\n"))
if height>120:
    print("you are allowed on the roller-coaster ride")
    if age>=18:
        print("the ticket cost is 12$")
        bill+=12
    elif age>=12:
        print("the ticket cost is 7$")
        bill+=7
    elif 55 >= age >= 45:
        print("everything is going to be on us")
    else:
        print("the ticket cost is 5$")
        bill+=5
    want_photos = bool(input("cost of photos is 3$ if you want photos type anything , if you dont, press enter "))
    if want_photos:
        print("photo cost is 3$")
        bill+=3

    print(f"your total bill sums up to {bill}$")

else:
    print("you are not allowed on the roller-coaster ride")