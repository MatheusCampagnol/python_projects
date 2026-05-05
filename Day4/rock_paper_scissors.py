#Importing the necessary libraries:

import random_module as rm
import asciii_art  as aa

#main functions:
#get_user_choice() - This function will ask the user to input their choice of rock, paper or scissors and return it.    
def get_user_choice():
    exit(1)

#get_computer_choice() - This function will use the random module to generate a random choice for the computer and return it.
def get_computer_choice():
    rm.generate_random_number()

#determine_winner() - This function compares the values of user's and computer's choices and determines the winner.
def determine_winner(user_choice, computer_choice):
    exit(1)

#main() - This funcition calls get_user_choice() and get_computer_choice().
def main():

    rm.generate_random_number()
    print(str(f"This is your number. {rm.randomint}"))
    print("This is rock: ")
    print(aa.rock)

if __name__ == "__main__":
    main()