import random
result=random.randint(0,1)
ans=int(input("enter 0 for heads and 1 for tails\n"))
if result==0:
    if ans==0:
        print("You Won")
    elif ans==1:
        print("You Lost ")
    else:
        print("enter 0 or 1 nothing else")
    print("It's Heads!!")
else:
    if ans==1:
        print("You Won")
    elif ans==0:
        print("You Lost ")
    else:
        print("enter 0 or 1 nothing else")
    print("It's Tails!!")