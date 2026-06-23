
from random import choice

from menu import MENU, resources

def check_transaction(money_received, drink_choice):
    drink_cost = MENU[drink_choice]["cost"]
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def process_coins(quarter, dime, nickel, penny):
    total = (quarter * 0.25) + (dime * 0.10) + (nickel * 0.05) + (penny * 0.01)
    return total    
    

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")

def check_resources(drink_type):
    ingredients = MENU[drink_type]["ingredients"]
    for ingredient, amount in ingredients.items():
        if resources[ingredient] < amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

def deduct_resources(drink_type):
    ingredients = MENU[drink_type]["ingredients"]
    for ingredient, amount in ingredients.items():
        resources[ingredient] -= amount
    print(f"☕ {drink_type.capitalize()} is done!")

def process_cappuccino():
    deduct_resources("cappuccino")

def process_espresso():
    deduct_resources("espresso")

def process_latte():
    deduct_resources("latte")

def check_action(prompt):
    try:
        if prompt == "espresso": return "espresso"    
        elif prompt == "latte": return "latte"
        elif prompt == "cappuccino": return "cappuccino"
        elif prompt == "off": return "off"
        elif prompt == "report": return "report"
        else:
            raise ValueError("Option not yet implemented or available. Try again.")            
    except ValueError as e: 
        print(f"Error: {e}")
        return check_action(prompt = input(
            "What would you like? (espresso/latte/cappuccino): "
        ).lower())   


def main():

    while True:

        choice = check_action(prompt = input(
            "What would you like? (espresso/latte/cappuccino): "
        ).lower())

        if choice == "off":
            break

        if choice == "report":
            print_report()
            continue
        
        while not check_resources(choice):
            choice = check_action(prompt = input(
                "What would you like? (espresso/latte/cappuccino): "
            ).lower())
        
        isMoneyEnough = check_transaction(process_coins(
            quarter = int(input("How many quarters?: ")),
            dime = int(input("How many dimes?: ")),
            nickel = int(input("How many nickels?: ")),
            penny = int(input("How many pennies?: "))
        ), choice)
        
        if not isMoneyEnough:
            continue
        
        if choice == "espresso":
            process_espresso()
        elif choice == "latte":
            process_latte() 
        elif choice == "cappuccino":
            process_cappuccino()

if __name__ == "__main__":
    main()