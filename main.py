from art import logo
from game_data import data
import random

data_len = len(data)

num = random.randint(0, data_len)

the_game = (data[num])

for i in the_game:
    print(i)

