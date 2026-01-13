import random
data = {
    1: ("Instagram", 690),
    2: ("Cristiano Ronaldo", 670),
    3: ("Lionel Messi", 510),
    4: ("Selena Gomez", 415),
    5: ("Kylie Jenner", 391),
    6: ("Dwayne Johnson", 390),
    7: ("Ariana Grande", 372),
    8: ("Kim Kardashian", 354),
    9: ("Beyoncé", 308),
    10: ("Khloé Kardashian", 300)
}
score=0
random_first=random.randint(1,10)
random_second=random.randint(1,10)
while True:
    print(f"score = {score}")
    
    while random_first==random_second:
        random_second=random.randint(1,10)
    ans=input(f"Who has more followers? {data[random_first][0]} or {data[random_second][0]}\n type a for first option and b for second ")
    ans=ans.lower()
    check_ans=0
    if data[random_first][1] > data[random_second][1]:
        check_ans="a"
    else:
        check_ans="b"
    if ans==check_ans:
        print("correct ans")
        score+=1
        print(f"current score = {score}")
    else:
        print("wrong ans")
        print(f"game over final score= {score}")
        break
    random_first=random_second
    random_second=random.randint(1,10)
    
