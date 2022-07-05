print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill?"))
tip_percent = int(input("How much tip would you like give?"))
split_people = int(input("How many people to split the bill?"))

total = total_bill + (total_bill * (tip_percent/100))
each_person_pay = round((total /5),2)
each_person_pay = "{:.2f}".format(each_person_pay)
print(f"Each person should pay: {each_person_pay}")

# Learn Python Day 1  and Day 2

