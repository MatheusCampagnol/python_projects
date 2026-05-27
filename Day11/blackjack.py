import ascii_art as aa
import random
from rich import print

card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Both draw_one_card and draw_card work hand-in-hand to add new cards for the player.
def draw_one_card():
    return random.choice(card_deck)

def draw_card(cards):
    
    cards.append(draw_one_card())

def winner_check(computers_sum, players_sum):
    """Checks the winner of the game if certain conditions are met.

    Args:
        computers_sum (int): Sum of all computer's cards.
        players_sum (int): Sum of all player's cards.

    Returns:
        Bool: Returns False if the criteria is met (if any player has a blackjack, hit 21 or have gone bust). Returns true if none of the criteria is met.
    """
    if computers_sum == 21 and players_sum == 21:
        print(f"[red]It's a[/red] [bold red]Draw![/bold red] [red]Both you and the computer have got a blackjack![/red]")
        return False
    elif computers_sum == 21:
        print(f"You [bold red]lose![/bold red] Computer has got a blackjack.")
        return False
    elif players_sum == 21:
        print(f"You [bold green]win![/bold green] With your hand you've got a blackjack.")
        return False
    elif players_sum > 21:
        print(f"You [bold red]busted![/bold red]")
        return False
    elif computers_sum > 21:
        print(f"[bold green]Computer busted! You win![/bold green]")
        return False

    return True

    
def add_up_scores(computers_cards, players_cards):
    """Collects player's and computer's cards and sum them.

    Args:
        computers_cards (int, list): random collection of numbers from card_deck.
        players_cards (int, list): random collection of numbers from card_deck.

    Returns:
        int: the sum of computer's cards and player's cards.
    """
    computer_total = sum(computers_cards)
    while computer_total > 21:
        if 11 in computers_cards:
            computer_total -= 10
#Covers a condition where multiple Aces can occur.            
            computers_cards.remove(11)
        else:
            break

    players_total = sum(players_cards)
    while players_total > 21:
        if 11 in players_cards:
            players_total -= 10
#Covers a condition where multiple Aces can occur.            
            players_cards.remove(11)
        else:
            break    
        
    return computer_total, players_total

#Draws two cards for the player.
def draw_player_cards():
    return random.sample(card_deck, 2)

#Draws two cards for the computer.
def draw_computer_cards():
    return random.sample(card_deck, 2)

def print_ascii_art():
    print(aa.BLACKJACK_ASCII)

def prints(computers_cards, players_cards, computer_sum, player_sum):
    """Prints players cards and its respective sums.

    Args:
        computers_cards (int, list): A list that contains all computer's cards.
        players_cards (int, list): A list that contains all player's cards.
        computer_sum (int): Sum of all computer's cards.
        player_sum (int): Sum of all player's cards.
    """
    print(f"Computers cards: {computers_cards}")
    print(f"Players cards: {players_cards}")
    print(f"Computers sum: {computer_sum}")
    print(f"Players sum: {player_sum}")
    
def main(): 
    print_ascii_art()

    computers_cards = draw_computer_cards()
    players_cards = draw_player_cards()

    game_running = True

    while game_running:
        computer_sum, player_sum = add_up_scores(computers_cards=computers_cards, players_cards=players_cards)

        prints(computers_cards, players_cards, computer_sum, player_sum)
        
        game_running = winner_check(computer_sum,player_sum)

        if not game_running:
            break

        choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()        

        if choice == "y":
            draw_card(players_cards)
        else:
            print("You chose to stand.")
            computer_sum, player_sum = add_up_scores(computers_cards, players_cards)
            while computer_sum < 17:
                draw_card(computers_cards)
                computer_sum, player_sum = add_up_scores(computers_cards, players_cards)
            prints(computers_cards, players_cards, computer_sum, player_sum)
            game_running = winner_check(computer_sum, player_sum)

            if game_running:
                if computer_sum > player_sum:
                    print("[red]Computer[/red] [bold red]wins![/bold red]")
                elif player_sum > computer_sum:
                    print("[bold green]You win![/bold green]")
                else:
                    print("[yellow]It's a draw![/yellow]")
            break



if __name__ == "__main__":
    main()