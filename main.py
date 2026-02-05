import turtle
from random import randint

FONT = ('Arial', 24, 'bold')
TURTLE_COLOR = "green"
SCORE = 0
BACKGROUND_COLOR = "light blue"
TIME = 10

game_board = turtle.Screen()
game_board.bgcolor(BACKGROUND_COLOR)
game_board.title("Turtle Smack")
turtle_instance = turtle.Turtle()
turtle_instance.color(TURTLE_COLOR)
turtle_instance.speed("fastest")
turtle_instance.shape("turtle")
turtle_instance.shapesize(2)
turtle_instance.penup()
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 250)
x = 500
y = 400

def turtle_jump():
    turtle_instance.hideturtle()
    turtle_instance.goto((randint(int(-x/2), int(x/2))), (randint(int(-y/2), int(y/2))))
    turtle_instance.color(TURTLE_COLOR)
    game_board.ontimer(turtle_instance.showturtle, randint(700, 1500))

def jump_time(seconds = TIME):
    if seconds > 0:
        game_board.ontimer(turtle_jump, randint(1000, 2000))
        game_board.ontimer(lambda: jump_time(seconds - 1), 1000)

def click_on_turtle(x, y):
    if turtle_instance.distance(x, y) < 25:
        turtle_instance.color("red")
        global SCORE
        SCORE = SCORE + 1

def timer(seconds = TIME):
    if seconds >= 0:
        pen.clear()
        game_board.ontimer(lambda: timer(seconds - 1), 1000)
        pen.write(f"Time Left: {seconds}\nScore: {SCORE}", False, "center", FONT)
    else:
        game_board.bgcolor("red")
        game_board.onclick(None)
        game_board.listen()
        game_board.onkeypress(turtle.bye, "space")
        for i in range(50):
            turtle_instance.hideturtle()
            turtle_instance.showturtle()
        pen.clear()
        pen.goto(0, 0)
        turtle_instance.goto(pen.xcor() - 170, pen.ycor() - 10)
        turtle_instance.pendown()
        turtle_instance.speed(3)
        turtle_instance.forward(340)
        turtle_instance.left(90)
        turtle_instance.forward(130)
        turtle_instance.left(90)
        turtle_instance.forward(340)
        turtle_instance.left(90)
        turtle_instance.forward(130)
        turtle_instance.left(90)
        pen.write(f"GAME OVER \nSCORE: {SCORE}\nPress 'Space' To Exit", False, "center", FONT)

game_board.onclick(click_on_turtle)
timer()
jump_time()
turtle.mainloop()
