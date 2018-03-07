"""A number-guessing game."""
from random import randint


def guessing_game():
# pick random number
    repeat = "Y"
    scores = []

    #Greet player and get the player name rawinput
    print("Hello!")
    name = raw_input("What is your name? ")

    while repeat == "Y":
        start = int(raw_input("Choose a starting number: "))
        end = int(raw_input("Choose an ending number: "))
        
        number = randint(1, 100)
    # Get the player to chose a number between 1 and 100 rawinput
        print("%s, I'm thinking of a number between 1 and 100, guess my number! You only get three guesses!") % name
        # print try to guess my number!
        digit = 0
        guess = 0
        while digit < 15 and guess != number:
            try:
                guess = int(raw_input("What is your guess? "))
                if guess < 1 or guess > 100:
                    print("Follow the instructions!!")
                elif guess < number:
                    print("Your guess is too low, try again!")
                elif guess > number:
                    print("Your guess is too high, try again!")
            except ValueError:
                print("Follow the instructions!!")
            digit += 1

        if guess == number:
            scores.append(digit)
            lowest_score = min(scores)

            print("Congrats %s! You found my number in %d tries! \nYour best score is %d") % (name, digit, lowest_score)
        else:
            print("Too many tries!")           
        repeat = raw_input("Do you want to play again? Y or N: ")

guessing_game()

#two rawinput for the start and end number at line 15 
#change line 24 to var start and end

#bigger the range the harder the game is >> 100 vs 50, the larger range is 2X, 
#divide larger range by smaller 5(2) for 50 and 5(1) for 100
#measuring range: end - start + 1 = range 
