# Approximate Days, Weeks and Months Until you reach a certain age.
import datetime as dt

# 🚨 Don't change the code below 👇
current_age = input("What is your current age?\n")
age_to_reach = input("What age do you want to get days, weeks and months left until that age?\n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

current_age = int(current_age)
age_to_reach = int(age_to_reach)
this_month = dt.datetime.now().month

months_left = int((age_to_reach - current_age) * 12 - this_month)
days_left = int(months_left /12 * 365.25)
weeks_left = int(days_left / 7)

print(f"\nYou have approximately {days_left} days, {weeks_left} weeks, and {months_left} months left until you are {age_to_reach} years old.")







