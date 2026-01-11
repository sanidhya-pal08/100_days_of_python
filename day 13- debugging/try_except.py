try:
    age=int(input("enter your age pls "))
except ValueError:
    print("numerical values only pls")
    age=int(input("enter your age pls "))
if age>18:
    print(f"You can drive at your age of {age}")