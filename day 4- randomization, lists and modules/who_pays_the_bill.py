import random
friends=["alice","bob","charlie","david","emanuel"]
index=random.randint(0,4)
person_paying_the_bill=friends[index]
print(f"the person paying the bill of all of us is {person_paying_the_bill}")
print(f"or it is {random.choice(friends)}")
