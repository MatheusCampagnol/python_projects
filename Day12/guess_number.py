from rich import print
from rich.progress import track
import ascii_art as aa
import time








def generate_status_bar():
    for _ in track(range(1000), description="Generating number..."):
        time.sleep(0.001)
    print("[bold green]Number generated![/bold green]")
        

def difficulty_option(prompt):
    if prompt == "easy":
        return 10
    elif prompt == "hard":
        return 5
    else:
        print("[bold red]Invalid input. Please type only 'easy' or 'hard': [/bold red]")
        return difficulty_option(input("Choose a difficulty. Type 'easy' or 'hard'. ").lower())


def print_ascii():
    print(aa.guess_art)
    print("Welcome to the Number Guessing Game!")
    print("Generating number from 1 to 100.")

def main(): 
    difficulty = ""

    print_ascii()
    generate_status_bar()
    difficulty = difficulty_option(input("Choose a difficulty. Type 'easy' or 'hard': ").lower())


if __name__ == "__main__":
    main()
    