import random
#setup____________________________________________________________________________________________________________________________
word_list=["apple","laptop","pen","table","weight"]
goal=random.choice(word_list)
leng=len(goal)
current=[]
current=["_"]*leng
lives=6
goal_reached=False


#functions_______________________________________________________________________________________________________________________
def printing_current_value():
    password="".join(current)
    print(password)


def check_goal_status():
    for i in range(0,leng):
        if current[i]!=goal[i]:
            
            return False
    return True   

#game_start________________________________________________________________________________________________________________

printing_current_value()
print("you got 6 lives right now play carefully")

while lives>0 and not goal_reached:
    word_guessed=False
    word=input("enter a letter")
    for i in range(0,leng):
        if word==goal[i]:
            word_guessed=True
            current[i]=word
    if word_guessed:

        print(f"that was the right word your current situation looks like ")
     
    else:
        lives-=1
        print(f'oops that was the wrong guess your current word  looks like ')
    printing_current_value()
    print(f"lives left - {lives}/6")
    if lives==0:
        print("you lost all of your lives game over!")
    goal_reached=check_goal_status()
    if goal_reached:
        print('you won every word matched!!!!')
    








