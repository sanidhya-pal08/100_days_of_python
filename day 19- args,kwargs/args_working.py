def add(*args):
    total_sum=0
    for arg in args:
        print(arg,end=" hi lol\n ")
        total_sum+=arg
    return total_sum
print(add(22,465,245,57)) 