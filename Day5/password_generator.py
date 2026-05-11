#Libraries:
import random

#Variables:
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',
]

numbers = [
    '0', '1', '2', '3', '4',
    '5', '6', '7', '8', '9'
]

symbols = [
    '!', '@', '#', '$', '%', '&',
    '(', ')', '*', '+', '-', '_',
    '=', '?', '/', '\\', '|', '[',
    ']', '{', '}', '<', '>', '.',
    ',', ':', ';'
]

letter_qty = 0
symbol_qty = 0
number_qty = 0
password = ''

def generate_password(letter_qty, symbol_qty, number_qty):
#Abre uma lista.
    pre_gen_password = []
#_ ignora a variável de loop, e o range é definido pela quantidade de letras, símbolos e números.    
    for _ in range(letter_qty):
        pre_gen_password += random.choice(letters)

    for _ in range(symbol_qty):
        pre_gen_password += random.choice(symbols)

    for _ in range(number_qty):
        pre_gen_password += random.choice(numbers)
#Embaralha a lista de caracteres.
    random.shuffle(pre_gen_password)  

#Pega o limite da pre_gen_password e usa ela como limite no for.
    for i in range(len(pre_gen_password)):
#Se o caractere for uma letra, ela passa na condição.
        if pre_gen_password[i].isalpha():
#E sendo verdadeira, é convertida para maiúscula.        
            if random.choice([True, False]):
                pre_gen_password[i] = pre_gen_password[i].upper()

#Junta tudo numa string simples.    
    password = ''.join(pre_gen_password)
#Mostra a senha gerada para o usuário.
    print(f"Your generated password is: {password}")
    

def main():
    global letter_qty, symbol_qty, number_qty
    while True:
        try:
            letter_qty = int(
                input("How many LETTERS would you like in your password? "))

            if letter_qty <= 0:
                print("Letter quantity must be greater than 0.")
                continue

            symbol_qty = int(
                input("How many SYMBOLS would you like in your password? "))

            if symbol_qty <= 0:
                print("Symbol quantity must be greater than 0.")
                continue

            number_qty = int(
                input("How many NUMBERS would you like in your password? "))

            if number_qty <= 0:
                print("Number quantity must be greater than 0.")
                continue

            break

        except ValueError:
            print("Error: Please type numbers only.")
            continue


if __name__ == "__main__":
    print("Welcome to the PyPassword Generator!")
    main()
    generate_password(letter_qty, symbol_qty, number_qty)