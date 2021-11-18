# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
def BMI_calculator(height, weight):
  '''
  Takes user input for height and weight, calculates your BMI, return statement based on BMI value.

  Parameters: height (float)
              weight (float)

  Return: BMI statement (sum)
  Output: None
  '''

  BMI = round((weight/(height**2)), 1)

  BMI_value_str = f"\nYour BMI is {BMI}. You "

  if BMI < 18.5:
    statement = BMI_value_str + "are considered underweight."
  elif BMI < 25:
    statement = BMI_value_str + "are considered normal weight."
  elif BMI < 30:
    statement = BMI_value_str + "are considered slightly overweight."
  elif BMI < 35:
    statement = BMI_value_str + "are considered obese."
  else:
    statement = BMI_value_str + "are considered clinically obese."

  return statement

print(BMI_calculator(height, weight))

