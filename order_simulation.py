# Pizza order and billing

# to add:
# 1. display prices and toppings list
# 2. add percentage tip or dollar tip
# 3. ask for address if delivery (check address is in area)
# 4. add 'Not on menu' display menu item
# 5. account for toppings split by 'and'
# 6. add update phone, delivery/pickup times, prices, toppings list

from datetime import datetime, timedelta

current_date_time = datetime.now()
delivery_time = 45
pickup_time = 20
store_phone_number = 555-555-5555
tax_rate = 0.0825
small_topping_price = 2
med_large_topping_price = 3
extra_cheese = 1
pizza_toppings = ['cheese']
pizza_ordered = {'order_date_time' : current_date_time, 'delivery' : False, 'pizza_size' : '', 'toppings' : pizza_toppings, 'extra_cheese' : False, 'sub_total' : 0, 'tax' : 0, 'tip' : 0, "total_bill" : 0}

toppings_menu = ['Pepperoni', 'Mushroom', 'Sausage', 'Onion', 'Black Olives', 'Green Pepper', 'Extra Cheese']


def prompt_for_delivery():
  print(f"Current delivery time is {delivery_time} minutes.\nPickup time is currently {pickup_time} minutes.\n")
  isdelivery = str.title(input('Is this order for delivery or pickup?\n'))
  if isdelivery == 'Delivery':
    isdelivery = True
  elif isdelivery == 'Pickup':
    isdelivery = False
  else:
    print('\nPlease enter either "Delivery" or "Pickup".')
    isdelivery = prompt_for_delivery()
  
  return isdelivery


def prompt_for_size():
  size = str.title(input("\nWhat size pizza do you want? S, M, or L \n"))

  if size == 'S' or size == 'Small':
    size = 'Small'
  elif size == 'M' or size == 'medium':
    size = 'Medium'
  elif size == 'L' or size == 'large':
    size = 'Large'
  else:
    print('The size requested is not clear. Please enter:\n"S" for small,\n "M" for medium, or\n "L" for large')
    prompt_for_size()
  
  return size


def display_menu():
  print('\nThe topping choices are:\n')
  [print(item) for item in toppings_menu]


def prompt_for_toppings(topping = 'None'):

  while(str.title(topping) not in ['Done', '', ' ']):
    print('\nEnter:')
    print('Pizza topping to add (one at a time) or:')
    print('"Menu" to see topping choices.')
    print('"None" for just a cheese pizza.') 
    print('"Done" when complete.\n')

    topping = str.title(input('What topping do you want on your pizza?\n'))
    # No toppings wanted. Complete order. 
    if topping == 'None':
      topping = 'Done'
    elif topping == 'Menu':
      display_menu()
      topping = str.title(input('\nWhat topping do you want on your pizza?\n'))

    # check and clean topping data
    if (' ' in topping) and (topping not in toppings_menu):
      topping = topping.replace(' ', ', ')
    if ',' in topping:
      [pizza_toppings.append(item.strip()) for item in topping.split(',') if item.strip() in toppings_menu]
    elif topping in toppings_menu:
      pizza_toppings.append(topping)
    
    if topping in toppings_menu:
      print(f"{topping} added.")
    elif (topping not in ['Done','Menu','None' '', ' ']): 
      print(f"\n{topping} not currently available. See menu for toppings.")
      display_menu()

  # "Done" and 'None' will pass through leaving toppings as ['cheese'] only

  return pizza_toppings


def get_total_bill():
  final_bill = 0

  if 'Extra Cheese' in pizza_ordered['toppings']:
    pizza_ordered['extra_cheese'] = True
    pizza_ordered['toppings'].remove('Extra Cheese')
  if pizza_ordered['pizza_size'] == 'Small':
    final_bill += 15
    final_bill += (len(pizza_ordered['toppings']) - 1) * small_topping_price
  if pizza_ordered['pizza_size'] == 'Medium':
    final_bill += 20
    final_bill += (len(pizza_ordered['toppings']) - 1) * med_large_topping_price
  if pizza_ordered['pizza_size'] == 'Large':
    final_bill += 25
    final_bill += (len(pizza_ordered['toppings']) - 1) * med_large_topping_price

  if pizza_ordered['extra_cheese']:
    final_bill += 1

  pizza_ordered['sub_total'] = final_bill
  pizza_ordered['tax'] = round(final_bill * tax_rate, 2)

  total_bill = '{:.2f}'.format(pizza_ordered['sub_total'] +                                        pizza_ordered['tax'])
  print(f"\nYour current total with tax is ${total_bill}")

  pizza_ordered['tip'] = round(float(input("\tWould you like to add a tip?\n\tEnter dollar amount to tip or 0 for no tip.\n$ ")), 2)
  
  total_bill = pizza_ordered['sub_total'] + \
               pizza_ordered['tax'] + \
               pizza_ordered['tip']

  return total_bill


def order_summary_confirmation():
  toppings_list = ''

  if len(pizza_ordered['toppings'][1:]):
    toppings_list = ' with ' + ', '.join(pizza_ordered['toppings'][1:])

  total_bill = '{:.2f}'.format(pizza_ordered['total_bill'])
  tax = '{:.2f}'.format(pizza_ordered['tax'])
  tip = '{:.2f}'.format(pizza_ordered['tip'])

  if pizza_ordered['extra_cheese']:
    toppings_list += ' with Extra Cheese'

  confirmation_statement = f"\nYour total for a {pizza_ordered['pizza_size']} cheese pizza{toppings_list} is ${total_bill}.\nThis total includes ${tax} tax and ${tip} tip.\n"

  print(confirmation_statement)
  submit_order = input("Would you like to submit this order? Yes or No\n")
  
  if str.title(submit_order) == 'Yes':
    return True
  elif str.title(submit_order) == 'No':
    return False
  else:
    print(f"An error has occurred. Please retry to place order or contact the store at {store_phone_number}")
    return False


def exit_prompt(submit_order):

  if pizza_ordered['delivery']:
    wait_time = delivery_time
  else: wait_time = pickup_time

  if submit_order:
    order_type = 'be ready'
    if pizza_ordered['delivery']:
      order_type = 'arrive'

    order_submitted = datetime.now()
    print(f"\nYour order has been submitted and should {order_type} at {(order_submitted + timedelta(minutes=wait_time)).strftime('%H:%M')}")
  else:
    print('\nYour order has been canceled. You may start a new order or exit.')

# main
print("Welcome to Python Pizza Deliveries!")
pizza_ordered['delivery'] = prompt_for_delivery()
pizza_ordered['pizza_size'] = prompt_for_size()
pizza_ordered['toppings'] = prompt_for_toppings()
pizza_ordered['total_bill'] = get_total_bill()

submit_order = order_summary_confirmation()
exit_prompt(submit_order)

# mimic order ticket sent or queued:
print('\n\no\Order recieved: ')
print(pizza_ordered)

