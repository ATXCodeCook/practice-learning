# Is a year a leap year
while True:
  try:
    year = int(input("Which year do you want to check? \n"))
    break
  except ValueError:
    print("Year must be a whole number. Please enter a whole number year.\n")

def is_leap_year(year):
  if (year % 4) == 0:
    if (not (year % 100) == 0) or ((year % 400) == 0):
      return True
    else: return False

def output_is_leap_year(year):
  if is_leap_year(year):
    print(f"{year} is a leap year.")
  else:
    # \033[4m   \033[0m underlines the word not
    print(f"{year} is \033[4mnot\033[0m a leap year")

output_is_leap_year(year)