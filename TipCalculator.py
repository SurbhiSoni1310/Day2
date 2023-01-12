print("Welcome to tip calculator")
bill = float(input("What is the total bill? $"))
percent = int(input("What percentage tip would you like to give? 10, 12, 0r 15?"))
people = int(input("How many people to split the bill? "))
pay = ((percent/100)*bill)/people + bill/people
# print("Each person should pay: $"+str(round(pay, 2)))
final_amount = "{:.2f}".format(pay)
print("Each person should pay: $"+final_amount)

