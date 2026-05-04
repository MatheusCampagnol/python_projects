#Define Variables:

is_left_right = False
direction = ""
is_swim_wait = False
wait_swim = ""
is_door_yellow = False
door_color = ""

#Prints treasure ASCII art:
def treasure_art():
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
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************''')

def check_left_right(direction):

    if direction.lower() == "left":
        return True
    else:
        return False
    

def check_swim_wait(wait_swim):
    if wait_swim.lower() == "wait":
        return True
    else:
        return False

def check_door_color(door_color):
    if door_color.lower() == "yellow":
        print("You win!")
        return True
    elif door_color.lower() == "red":
        print("Burned by fire. Game Over.")
        return False
    elif door_color.lower() == "blue":
        print("Eaten by beasts. Game Over.")
        return False
    else:
        print("Invalid door!")
        return False
 

#Core code:
def find_treasure():
    global is_left_right, direction, is_swim_wait, wait_swim, is_door_yellow, door_color

    direction = input("Welcome to Treasure Island."
          "Your mission is to find the treasure."
          "You're at a cross road. Where do you want to go?"
          "Type 'left' or 'right': ")
    
    is_left_right = check_left_right(direction)

    if is_left_right:
       wait_swim = input("You've come to a lake. There's an island in the middle of the lake."
                         "Type 'wait' to wait for a boat. Type 'swim' to swim across. ")
       is_swim_wait = check_swim_wait(wait_swim)
       if is_swim_wait:
            door_color = input("You arrive at the island unharmed. There is a house with 3 doors."
                               "One red, one yellow and one blue. Which color do you choose? ")
            is_door_yellow = check_door_color(door_color)
       else:
           print("Attacked by trout. Game Over.")
    else:
        print("Fall into a hole. Game Over.")

def main():

    treasure_art()
    find_treasure()


if __name__ == "__main__":
    main()