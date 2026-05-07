#Importing the necessary libraries:

import random_module as rm
import asciii_art  as aa


#variables:
user_input = 0
computer_choice = 0

#main functions:
#This function will ask the user to input their choice of rock, paper or scissors and return it.    
def get_user_choice():
    global user_input
    try:
        user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
        if user_input < 0 or user_input > 2:
            raise ValueError("Invalid input. Please enter 0, 1, or 2.")
        return user_input
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)

#This function will take the value from get_user_choice() and print the corresponding ASCII art for the user's choice.
def show_user_choice(user_input):
    if user_input == 0:
        print("You choose rock! "
              f"{aa.rock}")
    elif user_input == 1:
        print("You choose paper! "
              f"{aa.paper}")
    elif user_input == 2:
        print("You choose scissors! "
              f"{aa.scissors}")

#get_computer_choice() - This function will use the random module to generate a random choice for the computer and return it.
def get_computer_choice():
    global computer_choice
    rm.generate_random_number()
    computer_choice = rm.randomint

    if computer_choice == 0:
        print("Computer choose rock! "
              f"{aa.rock}")
    elif computer_choice == 1:
        print("Computer choose paper! "
              f"{aa.paper}")
    elif computer_choice == 2:
        print("Computer choose scissors! "
              f"{aa.scissors}")


#determine_winner() - This function compares the values of user's and computer's choices and determines the wi
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:        
        print("Computer wins!")

#main() - This funcition calls get_user_choice() and get_computer_choice().
def main():
    get_user_choice()
    show_user_choice(user_input)
    get_computer_choice()
    determine_winner(user_input, computer_choice)
    

if __name__ == "__main__":
    main()