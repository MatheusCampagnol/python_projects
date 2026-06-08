import random
import os

import game_data
import ascii_art as aa


def is_correct_answer(answer, a_index, b_index):
    a = game_data.data[a_index]
    b = game_data.data[b_index]

    if a["follower_count"] > b["follower_count"]:
        return answer == "a"

    return answer == "b"


def print_comparison(label, index):
    person = game_data.data[index]

    print(
        f"Compare {label}: "
        f"{person['name']}, "
        f"{person['description']}, "
        f"from {person['country']}."
    )


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_random_index(exclude=None):
    while True:
        index = random.randint(0, len(game_data.data) - 1)

        if index != exclude:
            return index


def main():
    score = 0
    game_over = False

    # Primeiro competidor
    a_index = get_random_index()

    while not game_over:
        clear_screen()

        print(aa.logo)

        if score > 0:
            print(f"You're right! Current score: {score}\n")

        # Segundo competidor
        b_index = get_random_index(exclude=a_index)

        print_comparison("A", a_index)
        print(aa.versus)
        print_comparison("B", b_index)

        answer = input(
            "Who has more followers? Type 'A' or 'B': "
        ).lower()

        if is_correct_answer(answer, a_index, b_index):
            score += 1

            # O B vira o novo A
            a_index = b_index

        else:
            clear_screen()
            print(aa.logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True


if __name__ == "__main__":
    main()