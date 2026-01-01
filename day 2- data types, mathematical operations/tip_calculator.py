bill=float(input("what was the total bill?\n"))
tip_percent=int(input("what percentage tip would you like to give? 10,12 or 15?\n"))
number_of_people=int(input("how many people would split the bill?\n"))
total_amount=bill+(bill*(tip_percent/100))
amount_per_person=total_amount/number_of_people
print(f"the amount to be paid per person is ${round(amount_per_person,2)} ")
