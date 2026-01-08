def calculator():
    wanna_continue=True
    first_num=float(input("enter the first number"))
    while wanna_continue:
        operation=input("enter which of these four operations do you want +, -, *, /")
        second_num=float(input("enter the second number"))
        if operation=="+":
            print(f"your first number was {first_num} and your second number was {second_num} and the operation was {operation} the result is :")
            result=first_num+second_num
            print(result)

        elif operation=="-":
            print(f"your first number was {first_num} and your second number was {second_num} and the operation was {operation} the result is :")
            result=first_num-second_num
            print(result)
        elif operation=="*":
            print(f"your first number was {first_num} and your second number was {second_num} and the operation was {operation} the result is :")
            result=first_num*second_num
            print(result)
        elif operation=="/":
            print(f"your first number was {first_num} and your second number was {second_num} and the operation was {operation} the result is :")
            result=first_num/second_num
            print(result)
        choice=input("type y if you want to continue calculating with the result and n if you wanna exit")
        if choice=="y":
            first_num=result
        else:
            wanna_continue=False

