from art import logo, vs
from game_data import data
import random
#from replit import clear

def get_random_account():
    """Randomly picks a dictionary from the list of dictionary"""
    return random.choice(data)

def account(info):
    """Takes the account data and returns the printable format"""
    name = info['name']
    desc = info['description']
    country = info['country']
    return (f"{name}, a {desc} from {country}.")

def check_answer(guess, a_followers_count, b_followers_count):
    """Takes the user's guess and follower counts and returns if they got it right"""
    if a_followers_count > b_followers_count:
        return guess == "a"
    else:
        return guess == "b"

def game():
    score = 0
    end_of_game = False
    account_b = get_random_account()
    while not end_of_game:
        print(logo)
        account_a = account_b
        account_b = get_random_account()
        
        if account_a == account_b:
            account_b = get_random_account()
        print(f"Compare A: {account(account_a)}")
        print(vs)
        print(f"Against B: {account(account_b)}")
        answer = input("Who has more followers? Type 'A' or 'B':").lower()
        
        a_followers_count = account_a['follower_count']
        b_followers_count = account_b['follower_count']
        
        is_correct = check_answer(answer, a_followers_count, b_followers_count)
        #clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            end_of_game = True
            print(f"Sorry, that's wrong. Final score: {score}")
        
game()
