def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}
wanna_continue=True
first_num=float(input("enter the first number "))
while wanna_continue:
    op=input("enter the operation you want")
    sec_num=float(input("enter the second number"))
    result=operations[op](first_num,sec_num)
    print(f"result is : {result}")
    choice=input("press y if you want to continue opeataions with the curent result , press n for exiting the calculator")
    if choice=="y":
        first_num=result
    else:
        wanna_continue=False
