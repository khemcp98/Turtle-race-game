import random
from turtle import Turtle, Screen

is_game_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []
for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)

user_bet = screen.textinput(title="make a bet", prompt="Which turtle will win the race? Enter color")
if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            color_turtle = turtle.pencolor()
            is_game_on = False
            if user_bet == color_turtle:
                print(f"You've won winning turtle is {color_turtle}")
            else:
                print(f"You've lost winning turtle is {color_turtle}")
        turtle.forward(random.randint(0, 10))


screen.exitonclick()
