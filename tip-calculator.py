#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

greeting = "Welcome to the tipe calculator.\n"

print(greeting)
total_bill = float(input("What was the total bill?\n"))

tip_percent = int(input("What percentage tip would you like to give? 10, 15, 20 or any other amount\n"))

split_number = int(input("How many people would you like to split the bill with? Enter 1 for no split of bill\n"))

tip_amount = round(total_bill * (tip_percent/100), 2)
bill_with_tip = round(((total_bill + tip_amount) / split_number), 3)

print(f"The tip amount is: ${tip_amount:.2f}")

if split_number == 1:
  print(f"The total bill with tip is ${bill_with_tip:.2f}")
else:
  print(f"Each person should pay: ${bill_with_tip:.2f}")