first_person_name = ""
second_person_name = ""

true = ["t","r","u","e"]
love = ["l","o","v","e"]

def get_second_person_name(true_counter, love_counter):
    second_person_name = input("Please type the first person's name: ").lower()
    for i in range(len(second_person_name)):
        if second_person_name[i] in true:
            true_counter += 1            
        if second_person_name[i] in love:
            love_counter += 1    
    return true_counter, love_counter

def get_first_person_name():
    true_counter = 0
    love_counter = 0
    first_person_name = input("Please type the first person's name: ").lower()
    for i in range(len(first_person_name)):
        if first_person_name[i] in true:
            true_counter += 1            
        if first_person_name[i] in love:
            love_counter += 1   
    return true_counter, love_counter        
    

def main():
    true_counter, love_counter = get_first_person_name()
    true_counter, love_counter = get_second_person_name(true_counter,love_counter)
    print(f"Your Love Score is: {true_counter}{love_counter}")


if __name__ == "__main__":
    main()
