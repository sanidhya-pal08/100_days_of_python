def is_leap_year(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    else:
        return False

    # Write your code here
    # Don't change the function name.
print(is_leap_year(2028))