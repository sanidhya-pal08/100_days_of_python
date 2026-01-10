def is_prime(num):
    if num<=1 or num==4:
        return False
    if num==2 or num==3:
        return True
    end_point=(num//2)+1
    print(end_point)
    for i in range(2,end_point):
        print(num%i)
        if num%i==0:
            return False
    return True
prime_or_not=is_prime(7)
if prime_or_not:
    print("prime")
else:
    print("composite")
