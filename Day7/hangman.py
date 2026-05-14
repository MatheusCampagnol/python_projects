import random
import stages_ascii as sa

word_list = ["apple", "banana", "window", "garden", "river", "mountain",
            "pencil", "school", "teacher", "friend", "family", "computer",
            "keyboard", "picture", "bottle", "orange", "purple", "yellow",
            "animal", "flower", "summer", "winter", "morning", "evening",
            "library", "hospital", "airport", "station", "market", "coffee",
            "chicken", "sandwich", "blanket", "backpack", "holiday", "journey",
            "village", "country", "captain", "pirate", "forest", "bridge",
            "island", "camera", "guitar", "pocket", "mirror", "button",
            "rocket", "planet"]

chosen_word = ""
lives = 6
letters_used = []

def is_letter_already_used(user_input,letters_used):
    if user_input in letters_used:
        print(f"You already tried the letter '{user_input}'.")
        return True
    return False

def print_straw_man(lives):
    print(sa.stages[lives])

def check_if_user_won(blanks):
    if "".join(blanks) == chosen_word:
        print(f"**********************************You won, nice job!**********************************")
        return True
            

#Stage variables for our hangman.

stage6 = """
  +---+
  |   |
      |
      |
      |
      |
=========
"""

stage5 = """
  +---+
  |   |
  O   |
      |
      |
      |
=========
"""

stage4 = """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
"""

stage3 = """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
"""

stage2 = """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
"""

stage1 = """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
"""

stage0 = """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
stages = [stage0, stage1, stage2, stage3, stage4, stage5, stage6]

letters_used = []

def is_letter_already_used(user_input,letters_used):
    if user_input in letters_used:
        print(f"You already tried the letter '{user_input}'.")
        return True
    return False

def print_straw_man(lives):
    print(stages[lives])

def check_if_user_won(blanks):
    if "".join(blanks) == chosen_word:
        print(f"**********************************You won, nice job!**********************************")
        return True
            

#Every guess is checked after the input.
def guess_letter():
    global lives
    while lives > 0:
        user_input = get_user_input()

        if is_letter_already_used(user_input, letters_used):
            continue

        letters_used.append(user_input)

        if user_input in chosen_word:
            print(f"Good job! The letter '{user_input}' is in the word.")
#Gets the range of chosen_word and for every occurence of user_input, replaces the blank in the list with the letter user selected.
            for i in range(len(chosen_word)):
                if chosen_word[i] == user_input:
                    blanks[i] = user_input  
            print_straw_man(lives)                     
            print(" ".join(blanks)) 
            print("______________________________________________________________________________________________________________________")
            check_if_user_won(blanks)
        else:
            print(f"Sorry, the letter '{user_input}' is not in the word.")
            lives -= 1

            if lives == 0:
                print_straw_man(lives)
                print(" ".join(blanks))
                print(f"**********************************You lose!!!!!**********************************")
                break

            print_straw_man(lives)
            print(" ".join(blanks))
        


#Gets user input. Any inputs lenghts > 1 will be discarded.
def get_user_input():
    while True:
        user_input = input("Please enter a letter: ").lower()
        if len(user_input) != 1:
            print("Invalid input. Please enter a single letter.")
            continue               
        return user_input

#Generates blanks in the code.
def generate_blanks(chosen_word):
    global blanks
    blanks = []
    for _ in range(len(chosen_word)):
        blanks.append("_")  
    return blanks


#Selects a random word from list word_list and returns it.
def select_random_word(word_list):
    return random.choice(word_list)

#1. Sets chosen_word from a list.
#2. Then generates the blanks with the lenght of the word.
#3. Calls guess_letter which then calls the user input.
def main():
    global chosen_word
    chosen_word = select_random_word(word_list)
    generate_blanks(chosen_word)
#Joins the blank appends into one string.               
    print_straw_man(lives)
    print(" ".join(blanks)) 
    guess_letter()

if __name__ == "__main__":
    main()