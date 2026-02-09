import turtle
from random import randint

FONT = ('Arial', 16, 'bold')
TURTLE_COLOR = "green"
BACKGROUND_COLOR = "light blue"
TIME = 30
SCREEN_HEIGHT = 700
SCREEN_WIDTH = 700

score = 0
game_over = False
game_board = turtle.Screen()
game_board.title("Turtle Smack")
turtle_instance = turtle.Turtle()
turtle_instance.color(TURTLE_COLOR)
turtle_instance.penup()
turtle_instance.speed("fastest")
turtle_instance.shape("turtle")
turtle_instance.shapesize(2)
game_over_turtle = turtle.Turtle()
game_over_turtle.hideturtle()
game_over_turtle.penup()
t = turtle.Turtle()
t.hideturtle()
t.penup()
s = turtle.Turtle()
s.hideturtle()
s.penup()


def start_game():
    global game_over, score
    game_over = False
    score = 0
    game_over_turtle.clear()
    turtle_instance.clear()
    t.clear()
    s.clear()
    game_board.bgcolor(BACKGROUND_COLOR)
    game_board.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    game_board.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
    timer()
    turtle_jump()
    game_board.onclick(click_on_turtle)

def timer():
    t.goto(0, SCREEN_HEIGHT/2 * 0.8)
    s.goto(0, SCREEN_HEIGHT / 2 * 0.7)
    def countdown(sec = TIME):
        if sec >= 0:
            t.clear()
            s.clear()
            t.write(f"Time Left: {sec}", False, "center", font = FONT)
            s.write(f"Score: {score}", False, "center", font=FONT)
            game_board.ontimer(lambda: countdown(sec - 1), 1000)
        else:
            t.hideturtle()
            t.clear()
            s.hideturtle()
            global game_over
            game_over = True
    countdown()

def turtle_jump():
    if not game_over:
        turtle_instance.hideturtle()
        turtle_instance.goto(randint(int(-SCREEN_WIDTH*0.7/2), int(SCREEN_WIDTH*0.7/2)),
                             randint(int(-SCREEN_HEIGHT*0.7/2), int(SCREEN_HEIGHT*0.7/2)))
        turtle_instance.color(TURTLE_COLOR)
        turtle_instance.showturtle()
        game_board.ontimer(turtle_jump, randint(400, 2000))
    else:
        turtle_instance.hideturtle()
        game_over_screen()

def click_on_turtle(x, y):
    if turtle_instance.distance(x, y) < 25:
        turtle_instance.color("red")
        global score
        score = score + 1
        turtle_instance.hideturtle()
        turtle_instance.goto(SCREEN_WIDTH, SCREEN_HEIGHT)

def game_over_screen():
    if game_over:
        game_board.bgcolor("red")
        turtle_instance.hideturtle()
        game_over_turtle.clear()
        game_over_turtle.goto(0, 0)
        game_over_turtle.write("GAME OVER", align="center", font=FONT)
        game_over_turtle.goto(0, -20)
        game_over_turtle.write("press 'space' to exit", align="center", font=FONT)
        game_over_turtle.goto(0, -40)
        game_over_turtle.write("press 'N' to new game", align="center", font=FONT)
        game_board.onclick(None)
        game_board.listen()
        game_board.onkeypress(exit_game, "space")
        game_board.onkeypress(new_game, "n")

def exit_game():
    if game_over:
        turtle.bye()

def new_game():
    if game_over:
        start_game()


start_game()
turtle.mainloop()