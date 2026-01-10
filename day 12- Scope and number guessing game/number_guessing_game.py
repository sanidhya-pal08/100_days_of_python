import random

def selecting_difficulty():
    while True:
        difficulty=input("type easy for easy difficulty and hard for hard difficulty ")
        if difficulty.lower()=="easy":
                lives=10
                break
        elif difficulty.lower()=="hard":
                lives=5
                break
        else:
                print("enter a valid input")
    return lives

def guessing_number():
    target=random.randint(1,100)
    attempts=selecting_difficulty()
    print(f"guess a number between 1 and 100 you have currently {attempts} attempts left")

    while attempts>0:  
        guess=int(input("guess a number "))

        if guess>target:
            print("Too High")

        elif guess<target:
            print("Too Low")

        else:
            print(f"{guess} is the correct answer You won the game")
            return

        attempts-=1
        print(f"you have currently {attempts} attempts left")

    print("You lost , you ran out of attempts")
    return
            

guessing_number()



    




