#TODO: Fazer uma função que faça a lista blanks virar uma string. Após isso, comparar com a palavra pré-selecionada.
#TODO: Implementar a rotina de vitória. Após adivinhar todas as letras da palavra, o usuário ganha.
import random

word_list = ["apple", "banana", "window", "garden", "river", "mountain",
            "pencil", "school", "teacher", "friend", "family", "computer",
            "keyboard", "picture", "bottle", "orange", "purple", "yellow",
            "animal", "flower", "summer", "winter", "morning", "evening",
            "library", "hospital", "airport", "station", "market", "coffee",
            "chicken", "sandwich", "blanket", "backpack", "holiday", "journey",
            "village", "country", "captain", "pirate", "forest", "bridge",
            "island", "camera", "guitar", "pocket", "mirror", "button",
            "rocket", "planet"]

chosen_word = []
lives = 6

#Every guess is checked after the input.
def guess_letter():
    while True and lives > 0:
        user_input = get_user_input()
        if user_input in chosen_word:
            print(f"Good job! The letter '{user_input}' is in the word.")
        elif lives == 0:
            print(f"You lose.")
            break
        else:
            print(f"Sorry, the letter '{user_input}' is not in the word.")
            lives -= 1
            print(lives)
        


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
    print(" ".join(blanks)) 
    guess_letter()

if __name__ == "__main__":
    main()