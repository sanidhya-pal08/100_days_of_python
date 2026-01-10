#Write a program to input eight numbers from the user and display all the unique numbers (once). 
s=set()
for i in range(0,8):
    element=int(input(f"enter your element number {i+1}- "))
    s.add(element)
print(s)