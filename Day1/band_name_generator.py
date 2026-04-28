#Cidade:
def city_name():
    city = input("Which city did you grow up in? \n")
    if city.isalpha():
        print(f"City name accepted: {city}")
    else:
        print("Please enter a valid city name consisting of letters only.")    

#PET:
def pet_name():
    pet = input("What is the name of your pet? \n")
    if pet.isalpha():
        print(f"Pet name accepted: {pet}")
    else:
        print("Please enter a valid pet name consisting of letters only.")    


#Main Function:
def main():

    city_name()
    pet_name()  
 
#Defines Main
if __name__ == "__main__":
    main()


