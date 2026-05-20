bidding_list = {}

def calculate_winner():
#Percorre o dicionário e retorna a chave (nome) que possui o maior valor (bid).    
    winner = max(bidding_list, key=bidding_list.get)
#Usa a chave do vencedor para acessar o valor do lance dentro do dicionário.
    winning_bid = bidding_list[winner]
#Imprime o resultado.
    print(f"The winner is {winner} with a bid of ${winning_bid}")


def process_bid():
    person_name = get_name()
    bid_amount = get_bid()

    bidding_list[person_name] = bid_amount

#Gets input for go again indicator:
def get_go_again_indicator():
    go_again_indicator = ""
    go_again_indicator = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()

    try:
        if go_again_indicator not in ['yes', 'no']:
            raise ValueError("Invalid input. Please type only yes or no.")
    except ValueError as e:
        print(f"Error: {e}")
        return get_go_again_indicator()

    return go_again_indicator

#Gets bid input:
def get_bid():
    try:
        bid_ammount = int(input("What is your bid?: $"))
        if bid_ammount <= 0:
            raise ValueError("Invalid input. Please enter a number greater than zero.")
    except ValueError as e:
        print(f"Error: {e}")
        return get_bid()
    
    return bid_ammount

#Gets input for name:
def get_name():
    try:
        person_name = input("What's your name?: ")
        if not person_name.isalpha():
            raise ValueError("You must type a letters only name")
        if person_name in bidding_list:
            raise ValueError("This name has already been used. Please choose another name.")    
    except ValueError as e:
        print(f"Error: {e}")
        return get_name()    
    return person_name

def main():
    while True:
        process_bid()
        if get_go_again_indicator() == "no":
            calculate_winner()
            break

if __name__ == "__main__":
    main()