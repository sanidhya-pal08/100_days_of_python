import random
#noodle logic
# computer_choice=random.randint(0,2)
# choice=int(input("what do you choose? enter 0 for rock, 1 for paper, 2 for scissor"))
# if choice<0 or choice>2:
#     print("please enter a valid input")
# else:
#     if choice == computer_choice:
#         print("computer choose the same thing draw")
#     else:
#         if choice == 0:
#             if computer_choice == 1:
#                 print("computer choose paper , You Lost")
#             else:
#                 print("computer choose scissor , You Won")
#         elif choice == 1:
#             if computer_choice == 0:
#                 print("computer choose rock , You Won")
#             else:
#                 print("computer choose scissor , You Lost")
#         else:
#             if computer_choice == 0:
#                 print("computer choose rock , You Lost")
#             else:
#                 print("computer choose paper , You Won")
#


#cleaner version below
choices=["rock","paper","scissors"]
computer_choice=random.randint(0,2)
user_choice=int(input("enter 0 for rock,1 for paper,2 for scissors"))

if user_choice<0 or user_choice>2:
    print("please enter a valid choice between 0 to 2")
else:
    print(f"you chose {choices[user_choice]}")
    print(f"computer chose {choices[computer_choice]}")
    if computer_choice==user_choice:
        print(f"Draw because computer choice was also {choices[computer_choice]}")
    elif (user_choice==0 and computer_choice==2) or (user_choice==1 and computer_choice==0) or (user_choice==2 and computer_choice==1):
        print("you won!!")
    else:
        print("you lost")
    #anohter modification below for last elif and else
    # elif (user_choice - computer_choice) % 3 == 1:
    #     print("You win")
    # else:
    #     print("You lose")