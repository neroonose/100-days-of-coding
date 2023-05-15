#from art import logo
import random
#Number Guessing Game Objectives:

# Include an ASCII art logo.
#print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")
mode = input("choose a difficulty. Type 'hard' or 'easy':")

if mode == "easy":
    num_guesses = 10
elif mode == "hard":
    num_guesses = 5
else:
    print("invalid game level")

# Allow the player to submit a guess for a number between 1 and 100
def game():
    the_guess = random.randint(1, 100)
    print(f"computer guessed {the_guess}")
    end_of_game = False

    remaining_guesses = num_guesses
        
    while not end_of_game:
        print(f"You have {remaining_guesses} remaining.")
        user = int(input("pick a number between 1 and 100:"))
        if user > the_guess:
            remaining_guesses -= 1
            #int(input("Guess Again!:"))
            print( "Too high")
        elif user < the_guess:
            remaining_guesses -= 1
            #int(input("Guess Again!:"))
            print( "Too low")
        elif user == the_guess:
            print(f"You got it! the answer was {the_guess}")
            end_of_game = True
        
        if remaining_guesses == 0:
            end_of_game = True
            print("You lost")
            
        
game()

play_again = input("Do you want to play again? Type 'Y' or 'N':")            
if play_again == "Y":
    game()
elif play_again == "N":
    return