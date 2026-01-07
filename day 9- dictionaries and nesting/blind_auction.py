
wanna_bid=True
bidders={}
def check_winner(dictionary):
    high_score=0
    name=""
    for i in dictionary:
        if high_score<dictionary[i]:
            high_score=dictionary[i]
            name=i
    print(f"{name} won the auction and bid of {name} was {high_score}")


while wanna_bid==True:
    name=input("enter your name ")
    bid=int(input("hello enter your bid "))
    bidders[name]=bid
    choice=input("are there more bidders? answer in yes/no ").lower()
    if choice=="no":
        wanna_bid=False
    elif choice=="yes":
        print("\n"*100)
        
check_winner(bidders)
