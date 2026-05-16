#Imports:
import Cyphers_Ascii as ca

alphabet = list("abcdefghijklmnopqrstuvwxyz") * 2 #*2 foi sugestão do Google após eu pesquisar por estouro de índice.

def process_message():
    encrypted_letter = []
    encode_or_decode = get_encode_or_decode()
    message = get_message()
    shift_number = get_shift_number()

    if encode_or_decode == 'encode': 
        for i in message:
            if not i.isalpha():
                encrypted_letter.append(i)
                continue
            else:
                position = (alphabet.index(i) + shift_number) % 26
                encrypted_letter.append(alphabet[position])
    elif encode_or_decode == 'decode':
        for i in message:
            if not i.isalpha():
                encrypted_letter.append(i)
                continue
            else:
                position = (alphabet.index(i) - shift_number) % 26
                encrypted_letter.append(alphabet[position])
            
    print(f"Here's your message: {''.join(encrypted_letter)}")
    
#Gets input for encode or decode:
def get_encode_or_decode():    
    try:
        encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()  
        if encode_or_decode not in ['encode', 'decode']:
            raise ValueError("You must choose either 'encode' or 'decode'.")
    except ValueError as e:
        print(f"Error: {e}")    
        return get_encode_or_decode()
    
    return encode_or_decode

#Gets input for message:
def get_message():
    try:
        message = input("Type your message: ").lower()
        if not message.strip():
            raise ValueError("You must type a message before encoding or decoding.")
    except ValueError as e:
        print(f"Error: {e}")
        return get_message()    
    return message

#Gets input for shift number:
def get_shift_number():
    try:
        shift_number = int(input("Type the shift number: "))
        if shift_number <= 0:
            raise ValueError("Invalid input. Please enter a number greater than zero.")
    except ValueError as e:
        print(f"Error: {e}")
        return get_shift_number()
    
    return shift_number

#Gets input for go again indicator:
def get_go_again_indicator():
    go_again_indicator = ""
    go_again_indicator = input("Type 'yes' if you want to go again. Otherwise type 'no': ")

    try:
        if go_again_indicator not in ['yes', 'no']:
            raise ValueError("Invalid input. Please type only yes or no.")
    except ValueError as e:
        print(f"Error: {e}")
        return get_go_again_indicator()

    return go_again_indicator

#Prints the art for the Cypher:
def print_ciphers_art():
    print(ca.caesar_cipher_logo)

def main():
    print_ciphers_art()
    while True:
        process_message()
        if get_go_again_indicator() == "no":
            break

if __name__ == "__main__":
    main()