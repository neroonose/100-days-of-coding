from art import logo
from game_data import data
import random

the_game = (data[random.randint(0, len(data))])

name = the_game['name']
no_of_followers = the_game['follower_count']
desc = the_game['description']
country = the_game['country']

print(f"{name}, a {desc} from {country}.")

