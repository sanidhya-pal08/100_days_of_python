print("welcome to the treasure island ")
first_answer=input("do you wanna go left or right\n").lower()
if first_answer=="left":
    second_answer=input("you are in front of a lake do you wanna swim across or do you wanna wait for a boat\n").lower()
    if second_answer=="wait":
        third_answer=input("you are at the island with the help of the boat now you have three doors blue,red and yellow which one do you wanna enter?\n").lower()
        if third_answer=="red":
            print("it was a room full of snakes and they ate you game over")
        elif third_answer=="yellow":
            print("you won you found the treasure!!!!!!!")
        elif third_answer=="blue":
            print("you fell into a trap game over")
        else:
            print("not sure if an option like this even exists. Game Over")
    else:
        print("crocodile ate you game over")
else:
    print("lion ate you game over")