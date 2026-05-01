hello = "Hello, World!"
number = input("Please enter a number: ")

def hello_world():
    return hello

def main():
    
    if number.isfloat():
        print(f"You entered a float: {number}")
    elif number.isdigit():
        print(f"You entered an integer: {number}")
    else:
        print(f"You entered a string: {number}")

        
if __name__ == "__main__":
    main()