# Compatibility Score Generator

print("Welcome to the Love Calculator!")
def prompt_for_names():
  name1 = input("What is your name? \n")
  name2 = input("What is their name? \n")
  return (name1, name2)
  
def compatibility_score_generator(name1, name2):
  combinded_names = (name1 + name2).lower()
  tens_digit_score = 0
  ones_digit_score = 0
  
  for character in list('true'):
    tens_digit_score += combinded_names.count(character)

  for character in list('love'):
    ones_digit_score += combinded_names.count(character)

  score = tens_digit_score * 10 + ones_digit_score

  if score <10 or score > 90:
    output = f"Your score is {score}, you go together like coke and mentos."
  elif score >= 40 and score <= 50:
    output = f"Your score is {score}, you are alright together."
  else:
    output = f"Your score is {score}"

  return output

name1, name2 = prompt_for_names()
results = compatibility_score_generator(name1, name2)
print(results)

# #tests
# print('\nTests:')
# print(compatibility_score_generator('aaa', 'bbb'))
# print(compatibility_score_generator('bbtruetruetruedd', 'aalovelovedd'))
# print(compatibility_score_generator('aatrueaa', 'aalovlaa'))
# print(compatibility_score_generator('aatraa', 'aaloaa'))
# print(compatibility_score_generator('bbtruetrss', 'bblovess'))