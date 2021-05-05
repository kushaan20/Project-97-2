import random
number = random.randint(1, 9)
chances = 0
while chances < 5:
    guess = int(input("Enter number :"))
    chances = chances + 1
    if guess == number:
        print("Congratulations! You Won! The number is indeed ", number, "!")
        break 
    if not guess == number:
        print("Guess a different number than ", guess)
    if not chances < 5:
        print("You Lost! The number is: ", number)

