#This module uses the random library to generate a number between 1 and 3.
import random

#Variable declaration for module.
randomint = 0

def generate_random_number():
    global randomint
    randomint = random.randint(1, 3)
    return randomint
