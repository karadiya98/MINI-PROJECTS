import turtle
import random
import time

delay = 0.1
score = 0
highscore = 0

# body of snake 
bodies = []

# screen setup
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("grey")
s.setup(width=600, height=600)

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("silver")
head.fillcolor("blue")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.goto(0, 200)
food.ht()
food.st()

# score board
sr = turtle.Turtle()
sr.speed(0)
sr.shape("square")
sr.fillcolor("black")
sr.penup()
sr.goto(-250, -250)
sr.ht()
sr.write("Score: 0 | Highscore: 0")

# movement functions
def moveup():
    if head.direction != "down":
        head.direction = "up"

def movedown():
    if head.direction != "up":
        head.direction = "down"   

def moveright():
    if head.direction != "left":
        head.direction = "right"

def moveleft():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)   

# handling keyboard input
s.listen()
s.onkey(moveup, "Up")
s.onkey(movedown, "Down")
s.onkey(moveleft, "Left")
s.onkey(moveright, "Right")

# ---------------- main method ------------------------------ 
while True:
    s.update()  # updating the screen

    # collision with screen borders (wraparound effect)
    if head.xcor() < -290:
        head.setx(290)
    if head.xcor() > 290:
        head.setx(-290)
    if head.ycor() < -290:
        head.sety(290)
    if head.ycor() > 290:
        head.sety(-290)            

    # collision with food
    if head.distance(food) < 20:
        # move food to a random place
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # increase length of the snake
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        body.fillcolor("black")
        bodies.append(body)

        # update score
        score += 10
        if score > highscore:
            highscore = score
        sr.clear()
        sr.write("Score: {} | Highscore: {}".format(score, highscore))

    # moving the snake body
    for index in range(len(bodies) - 1, 0, -1):
        x = bodies[index - 1].xcor()
        y = bodies[index - 1].ycor()
        bodies[index].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()    

    # collision with the snake's body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # hide all the snake's body parts
            for body in bodies:
                body.hideturtle()
            bodies.clear()

            score = 0
            delay = 0.1

            # update score board
            sr.clear()
            sr.write("Score: {} | Highscore: {}".format(score, highscore))

    time.sleep(delay)

# No need to call s.mainloop() here because it's handled by s.update()
