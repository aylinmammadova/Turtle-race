from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race? Enter a color:").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False

turtle_list = []
for turtle_index in range(6):
    t = Turtle(shape="turtle")
    t.color(colors[turtle_index])
    t.penup()
    t.goto(x=-230, y=-100 + turtle_index * 40)
    turtle_list.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 220: # 250 subtract at least half of turtle size but i made a little mor
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
