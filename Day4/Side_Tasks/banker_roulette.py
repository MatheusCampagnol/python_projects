import random as rm

randomint = 0

randomstr = ""

friends = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

#First function to pull an random name from the list of friends using random(rm).choice() function.
def main():
   
   randomstr = rm.choice(friends)
   print(str(f"{randomstr} is going to buy the meal today!"))

#Second function to pull a random name using the random number set from 0 to 4 and printing it out.
def main_2():
    randomint = rm.randint(0, 4)
    print(str(f"{friends[randomint]} is going to buy the meal today!"))


if __name__ == "__main__":
    main()
