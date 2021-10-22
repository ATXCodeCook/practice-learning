# Check if input is even or odd.
# Loop until input is integer.
while True:
  try:
    number = input("Which integer number do you want to check? \n")
    number = int(number)
    break
  except ValueError:
    print(f"\n{number} is not an integer (number that is not a decimal or fraction).\n")

def is_even(number):
  '''
  Takes in an integer and returns a statement as to whether the number is even or odd.

  Parameter: number (int)
  Return: statement of even or odd (str)
  Output: None
  '''
  num_parity = 'odd'

  if number % 2 == 0:
    num_parity = 'even'
    
  return f"\n{number} is an {num_parity} number."

print(is_even(number))