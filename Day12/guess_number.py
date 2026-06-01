from rich import print
from rich.progress import track
import random 
import ascii_art as aa
import time

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def get_number(prompt):
    while True:      
        value = input(prompt).strip()
#Retorna sempre um int.
        try:
            return int(value)
        except ValueError:
            print("[bold red]Invalid number.[/bold red]")

    
def generate_random_number():
    return random.randint(1, 100)


def show_loading_bar():
    for _ in track(range(1000), description="Generating number..."):
        time.sleep(0.001)
    print("[bold green]Number generated![/bold green]")
        

def choose_difficulty(prompt):
    if prompt == "easy":
        return EASY_ATTEMPTS
    elif prompt == "hard":
        return HARD_ATTEMPTS 
    else:
        print("[bold red]Invalid input. Please type only 'easy' or 'hard': [/bold red]")
        return choose_difficulty(input("Choose a difficulty. Type 'easy' or 'hard'. ").lower())


def print_ascii():
    print(aa.guess_art)
    print("Welcome to the Number Guessing Game!")
    print("Generating number from 1 to 100.")

def main(): 

    print_ascii()
    show_loading_bar()
    random_number = generate_random_number()
#    print(f"Psst, your number is: {random_number}")
    chances_left = choose_difficulty(input("Choose a difficulty. Type 'easy' or 'hard': ").lower())
    
    while chances_left > 0:    
        number = get_number("Make your guess: ")
        
        if number < random_number:
            chances_left -= 1
            if chances_left > 0:
                print(f"Too low. Chances left: {chances_left}")

        elif number > random_number:
            chances_left -=1
            if chances_left > 0:
                print(f"Too high. Chances left: {chances_left}")

        else:
            print(f"[bold blue]That's it! The correct number has been guessed![/bold blue] Number was {random_number}!")
            break
    
        if chances_left == 0:
            print("[bold red]You ran out of chances![/bold red]")


if __name__ == "__main__":
    main()
    
