import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def blackjack():
    wanna_continue=True
    while True:
            choice=input("enter y if you wanna play blackjack and enter n if you dont want to play blackjack ")
            if choice=="y":
                wanna_continue=True
                break
            elif choice=="n":
                wanna_continue=False
                break
            else:
                print("please respond with a valid input")
        
    while wanna_continue:
        user_cards=[]
        dealer_cards=[]
        user_cards.append(random.choice(cards))
        user_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
        print(f"you have the cards of {user_cards} \nthe dealer has the first card of {dealer_cards[0]}")
        while True :
            card_choice=input("do you want an extra card enter y for yes and n for no ")
            if card_choice=="y":
                user_cards.append(random.choice(cards))
                print(f"you have the cards of {user_cards} \nyour current score is {sum(user_cards)}")
                user_score=sum(user_cards)
                if user_score>21:
                    break
                elif user_score==21:
                    break
            elif card_choice=="n":
                break
            else:
                print("enter a valid response")
        user_score=sum(user_cards)
        dealer_score=sum(dealer_cards)
        while dealer_score<17:
            print("dealer decided to draw a card")
            dealer_cards.append(random.choice(cards))
            dealer_score=sum(dealer_cards)
        user_diff=21-user_score
        dealer_diff=21-dealer_score
        print(f"Your current score is {user_score} and dealer score is {dealer_score}")
        if (user_score>21 and dealer_score>21) or (user_score==dealer_score):
            print("The game is Draw")
        
        elif (dealer_score==21):
            print("You lost the dealer won by blackjack")
        
            
        elif (user_score==21):
            print("You won by blackjack")
        
            
        elif(user_score>21):
            print("You lost , your score went greater than 21")
        
            
        elif(dealer_score>21):
            print("You won , the dealer score went above 21")
            
            
        elif(user_diff<dealer_diff):
            print("You won your score was closer to 21 than the dealer score")
            
            
        elif(user_diff>dealer_diff):
            print("You lost dealer's score was closer to 21 than your score")
        while True:
            choice=input("enter y if you wanna play blackjack and enter n if you dont want to play blackjack ")
            if choice=="y":
                wanna_continue=True
                break
            elif choice=="n":
                wanna_continue=False
                break
            else:
                print("please respond with a valid input")

           
        

blackjack()


