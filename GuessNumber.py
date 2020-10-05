import random

guess_number = random.randint(1,3)
guess_count = 0
number = 0
while guess_number != number and guess_count < 3:
    try:
        number = int(input("Guess: "))
        guess_count = guess_count + 1
        if number < guess_number:
            print("Too low. Guess number is " + str(guess_count))
        elif number > guess_number:
            print("Too high. Guess number is " + str(guess_count))
        else:
            print('Correct! You guessed it on try #' + str(guess_count))
    except ValueError:
        print("You did not enter a number.")
if guess_count == 3:
    print("Out of Guesses! Guess Number was " + str(guess_number))