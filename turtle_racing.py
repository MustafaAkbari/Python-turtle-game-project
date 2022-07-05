from turtle import Turtle, Screen
import random
is_race_on = False
window = Screen()
window.bgcolor("Black")
window.title("Turtle Racing")
window.setup(width=500, height=400)
user_choice = window.textinput(title="Make your choice!", prompt="Which turtle will win tha race? Enter a color: ")
colors = ["red", "blue", "green", "yellow", "orange", "purple", "white"]
all_turtles = []
end_line = Turtle()
end_line.penup()
end_line.speed("fastest")
end_line.hideturtle()
end_line.goto(x=235, y=-240)
end_line.pendown()
end_line.pencolor("white")
end_line.setheading(90)
end_line.forward(500)
end_line.showturtle()

y_core = -200
x_core = -240
for turtle_index in range(7):
    y_core += 50
    musti = Turtle("turtle")
    musti.penup()
    musti.color(colors[turtle_index])
    musti.goto(x=x_core, y=y_core)
    all_turtles.append(musti)
if user_choice:
    is_race_on = True
while is_race_on:
    for turtles in all_turtles:
        if turtles.xcor() > 230:
            winning_color = turtles.pencolor()
            if winning_color == user_choice:
                print(f"You've won!, the {winning_color} turtle is winner!")
            else:
                print(f"You've lose!, the {winning_color} turtle is winner!")
            is_race_on = False
        rand_space = random.randint(1, 10)
        turtles.forward(rand_space)
window.mainloop()
