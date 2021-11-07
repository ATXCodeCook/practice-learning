# BMI Calculator

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

def BMI_Calculator(height, weight):
  return round((float(weight)/(float(height)**2)))

BMI = BMI_Calculator(height, weight)
print(f" Your BMI is {BMI}.")








