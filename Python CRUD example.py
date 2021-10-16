# add new user

import random
import string
import numpy as np
from datetime import date

# pre-initialized/database
users_dict = dict()
next_account_id = 1000
account_id_lookup = {}

print(next_account_id)

# Add/Create user
def add_new_user():
  '''
  Accepts user input for name, age and gender. Assigns next Account ID and adds user to the user_dict dictionary. The name:account_id is stored in a lookup table/dictionary for faster name searches. The assumption that memory and storage are not constrained. Other methods for fast lookup may be needed if memory or storage is a constraint. 

  Note: Missing name will be assigned "Anonomous", Missing age will be assigned 999 (missing flag value) and missing gender will be assigned as numpy nan.

  It is assummed a database or data structure will be previously created and stored to hold the user dictionary, next_account_id (may be implemented as set/list if needed) and lookup table.   
  '''
  global next_account_id
  duplicate_user_name_flag = True

  user_name = input("What would you like your user name to be? ")
  # Check for duplicate user_name
  while ((user_name in account_id_lookup.keys()) or (user_name in [None, ''])):
    print('User name \'' + user_name + '\' is unavailable. Please use another user name.')
    user_name = input("What would you like your user name to be? ")

  age = input("What is your age? ")
  signup_date = date.today()
  gender = input("What is your gender? ")

  if age == '':
    age = 999
  if gender == '':
    gender = np.nan
  account_id = next_account_id
  users_dict[account_id] = {'user_name' : user_name, 'age' : int(age), 'gender' : gender, 'age_changed_date' : signup_date, 'member_since': signup_date}
  account_id_lookup[user_name] = account_id

  next_account_id +=1

  print('\nNew user \'' + user_name + '\' added with Account ID ' + str(account_id) + '.')


# get user info by name or id
def get_user_info(user_name = '', account_id = 0):
  '''
  Get user information by name or id. Prints information with approximated age based on today's year minus signup date's year added to age.
  
  Return: None (prints information)

  Parameters: user_name (string)
              account_id (int)
  '''

  # print user name and id to search for (reference only)
  if user_name is not None and account_id is not None:
    print("\nTest name and id are: " + user_name + ', ' + str(account_id))

  if user_name and account_id == 0:
    try:
      account_id = account_id_lookup[user_name]
    except KeyError:
      print("\nNo user name \'" + user_name +"\' found.")
      return

    if account_id:
      print('\n\nUser Found')
      print('\naccount_id: ' + str(account_id))
      
      # update user's aproximate age based on signup year
      this_year = date.today().year
      age_changed_date = users_dict[account_id]['age_changed_date'].year
      user_signup_age = users_dict[account_id]['age']
      user_age = user_signup_age + (this_year - age_changed_date)
      users_dict[account_id]['age'] = user_age
      
      for k, v in users_dict[account_id].items():
        print(str(k) +': ' + str(v))
      print('\n')

  elif account_id and (account_id != 0):
    try:
      if users_dict[account_id]:
        print('\n\nUser Found')
        print('account_id: ' + str(account_id))
    except KeyError:
      print("\nNo account ID '" + str(account_id) + "' found.")
      return
    for k, v in users_dict[account_id].items():
      print(str(k) +': ' + str(v))
    print('\n')
  
  else: 
    print("\nAn unknown error occured. Please check that a valid user name or Account ID was entered.")



# Update user info by account id
def update_user_by_id(account_id):
  print('What field do you want to update?')
  print('Enter the number next to the field you would like to update:')
  print('1 - user_name')
  print('2 - age  Note: Age may only be changed one time.')
  print('3 - gender')
  print('Q - Exit without making changes')

  update_field = str(input('Enter number (1, 2 or 3) or "Q" to exit: '))

  if update_field == '1':
      user_name = input("What would you like your user name to be? ")
      # Check for duplicate user_name
      while ((user_name in account_id_lookup.keys()) or (user_name in [None, ''])):
        print('User name \'' + user_name + '\' is unavailable. Please use another user name or enter "Q" to Exit.')
        user_name = input("What would you like your user name to be? ")

      if user_name !='Q':
        users_dict[account_id]['user_name'] = user_name
        return
  
  elif update_field == '2':
    age = 0
    while (age < 1 or age >150):
      age = int(input("What is your current age? "))

    # Only allow one age change policy
    # Will allow multiple changes on signup day
    age_changed_previously = users_dict[account_id]['age_changed_date'] != users_dict[account_id]['member_since']

    if age_changed_previously:
      print('The age of the acount holder can only be changed once. Please contact support if you need additional help.')
      return

    users_dict[account_id]['age'] = age
    users_dict[account_id]['age_changed_date'] = date.today()



  elif update_field == '3':
      gender = ''

      while (gender == ''):
        gender = input('What is your gender? ')
      
      users_dict[account_id]['gender'] = gender

  else:
      print('No changes made. Returning...')



# delete user by id
def remove_user_by_id(account_id, confirmation = True):
  try:  del users_dict[account_id]
  except KeyError:
    print('Account ID ' + str(account_id) + ' not found.')
    return
  if confirmation:
    print('User with ID \'' + str(account_id) + '\' has been removed.')


## Test: get info
def get_info_test():
  test_name1 = ''
  test_name2 = ''
  test_id1 = 0
  test_id2 = 0
  blank_id = None
  blank_name = None
  test_users_to_remove = []

  global next_account_id

  for i in range(0, 21):
    user_name = ''.join(random.choice(string.ascii_letters) for _ in range(7))
    age = random.randint(1, 100)
    signup_date = date.today()
    gender = ''.join(random.choice(string.ascii_letters) for _ in range(4))

    account_id = next_account_id
    test_users_to_remove.append(account_id)
    users_dict[account_id] = {'user_name' : user_name, 'age' : int(age), 'gender' : gender, 'age_changed_date' : signup_date, 'signup_date' : signup_date}

    account_id_lookup[user_name] = account_id

    next_account_id +=1

    if i == 3:
      test_name1 = user_name
      test_id1 = account_id
    
    if i == 12:
      test_name2 = user_name
      test_id2 = account_id
    

  # get_users_list()
  print("\nBegin user's name and user's ID tests.")
  get_user_info(user_name = test_name1)
  get_user_info(account_id = test_id1)
  get_user_info(user_name = test_name2)
  get_user_info(account_id = test_id2)
  print("\nCatch missing values tests:")
  print('\nNo value entered for next two lines.')
  get_user_info(user_name = blank_name)
  get_user_info(account_id = blank_id)
  get_user_info(user_name = 'Not_in_list')
  get_user_info(account_id = 99)
  print("\n\nEnd of tests. Removing test_users from user_dict.")

  # Remove test users from users_dict
  num_test_users = len(users_dict)
  for account_id in test_users_to_remove:
    remove_user_by_id(account_id, confirmation=False)
  print('\nNumber of test users to remove: ' + str(len(test_users_to_remove)))
  num_test_users_removed = num_test_users - len(users_dict)
  print('\nNumber of test users removed is: ' + str(num_test_users_removed))
  if len(test_users_to_remove) != num_test_users_removed:
    print(num_test_users)
    print(num_test_users_removed)

    print('Some test users were not removed. Please verifiy the following Account IDs have been removed.\n')
    print(test_users_to_remove)

## End Test


get_info_test()

# add_new_user()
# add_new_user()
# get_user_info(user_name = '')
# remove_user_by_id()

