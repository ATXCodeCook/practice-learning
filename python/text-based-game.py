print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print('Enter "quit" at anytime to exit the game.') 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

def get_character_action(mission_prompt_counter):
  return (input())

def game_control(mission_prompt_counter = 0):

  while (mission_prompt_counter < 4):
    character_action = game_progress(mission_prompt_counter)
    if character_action.lower() in ['left', 'wait', 'yellow']:
      mission_prompt_counter += 1
    elif character_action.lower() in ['right', 'swim', 'red']:
      mission_prompt_counter = game_end(mission_prompt_counter)
    elif character_action.lower() == 'blue':
      mission_prompt_counter = game_end(mission_prompt_counter + 1)
    elif mission_prompt_counter == 2: # and no correct door color above
      _ = game_end(mission_prompt_counter + 2)
      mission_prompt_counter = 999
    elif character_action.lower() in ['end', 'quit']:
      mission_prompt_counter = 999
    else:
      print('\nUnrecoginzed action')
      print(mission_prompt_counter)

def game_progress(mission_prompt_counter):
  mission_prompts_list = ['You\'re at a crossroad. Where do you want to go? Type "left" or "right"',
  'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.',
  "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?",
  "You found the treasure! You Win!"]

  print('\n' + mission_prompts_list[mission_prompt_counter])
  if mission_prompt_counter != 3:
    character_action  = get_character_action(mission_prompt_counter)
    return(character_action)
  else:
    return('end')

def game_end(mission_prompt_counter):
  game_end_prompts_list = ["You fell into a hole. Game Over.",
  "You get attacked by an angry trout. Game Over.",
  "It's a room full of fire. Game Over.",
  "You enter a room of beasts. Game Over.",
  "You are delirious chose a door that doesn't exist. Game Over." ]

  print(game_end_prompts_list[mission_prompt_counter])
  # game end code
  return(999)

game_control()