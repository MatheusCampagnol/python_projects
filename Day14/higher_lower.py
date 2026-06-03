import game_data as game_data
import ascii_art as aa
import os




def define_correct_comparison(answer, idx, idx1):
    a = game_data.data[idx]
    b = game_data.data[idx1]

    if a['follower_count'] > b['follower_count'] and answer == 'a':
        return False
    elif b['follower_count'] > a['follower_count'] and answer == 'b':
        return False
    else:
        return True

def comparison_current(index): 
    a = game_data.data[index]
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.")

def comparison_next(index):
    b = game_data.data[index]
    print(f"Compare B: {b['name']}, {b['description']}, from {b['country']}.")

def print_versus_ascii_art():
    print(aa.versus)

def print_logo_ascii_art():
    print(aa.logo)

def main():

    game_over = False
    index = 0
    idx = index
    idx1 = index + 1
    score = 0

    while game_over == False:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_logo_ascii_art()

        if score == 0:
            pass
        else:
            print(f"You're right! Current score: {score}")


        comparison_current(idx)
        print_versus_ascii_art()
        comparison_next(idx1)
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_correct = define_correct_comparison(answer, idx, idx1)

        if is_correct == False:
            if answer == 'b':
                idx = idx1
            idx1 += 1
            score += 1
        else: 
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True

if __name__ == "__main__":
    main()
