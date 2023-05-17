import art
from game_data import data
import random

#the_game = (data[random.randint(0, len(data))])

#name = the_game['name']
#no_of_followers = the_game['follower_count']
#desc = the_game['description']
#country = the_game['country']

#print(f"{name}, a {desc} from {country}.")
def get_random_account():
    return random.choice(data)

the_game = random.choice(data)
def account():
    name = the_game['name']
    desc = the_game['description']
    country = the_game['country']
    return (f"{name}, a {desc} from {country}.")

account_a = account()
print(f"Compare A: {account_a}")
account_b = get_random_account()
print(f"Against B: {account_b}")
print(account_a["follower_count"]) 
    #print(