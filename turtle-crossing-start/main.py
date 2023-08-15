import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = ScoreBoard()


screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # create new cars
    car_manager.new_car()
    car_manager.move_cars()

    # check for collision and make game over
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

    # increase player's score and increase game level
    if player.end_point():
        car_manager.level_up()
        score_board.increase_score()        
        player.starting_postion()

screen.exitonclick()
