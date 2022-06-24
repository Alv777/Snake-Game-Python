#                             THE MIGHTY SNAKE  by Alvkraft                       #
#                                                                                 #
# WARNING: THIS IS THE ENTIRE CODE OF THE GAME, BE AWARE OF MODIFY SOMETHING,     #
# YOU CAN BREAK THE GAME. IF YOU HAVE EXPERIENCE WITH PYTHON GO ON AND MODIFY MY  #
# GAME AT YOUR PLEASURE. IF YOU ARE GOING TO USE THE CODE CONTACT ME VIA EMAIL    #
# business.alvkraft@gmail.com, ENJOY THE GAME AS I ENJOYED CREATING IT.           #

import turtle
import time
import random

posponer = 0.1

# Scoreboard 📋
score = 0
high_score = 0

# Screen Configuration 📺
wn = turtle.Screen()

wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0)

# Snake Head 🐍

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("GreenYellow")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Food 🍎

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

# Segments / Snake's Body 🐍
segments = []

# Text
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0,260)
text.write("Score: 0       High Score:0", align = "center", font =("Courier", 24, "normal"))

# Functions 📋
def up():
	head.direction = "up"
def down():
	head.direction = "down"
def left():
	head.direction = "left"
def right():
	head.direction = "right"

def mov():
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

# Keyboard ⌨

## Wasd Keys ##
wn.listen()
wn.onkeypress(up, "w")
wn.onkeypress(down, "s")
wn.onkeypress(left, "a")
wn.onkeypress(right, "d")
## Arrow Keys ##
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")

# Time / Updates ⌛
while True:
	wn.update()

	# Border Screen Collision
	if head.xcor() > 280 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
		time.sleep(1)
		head.direction = "stop"
		head.goto(0,0)
		[a.hideturtle() for a in segments]
		segments.clear()

		## Hide Segments
		for segment in segments:
			segments.goto(1000,1000)

		## Reset Scoreboard
		score = 0
		text.clear()
		text.write("Score: {}     High Score: {}".format(score, high_score),
				align = "center", font =("Courier", 24, "normal"))

    # Food Collisions 🍎
	if head.distance(food) < 20:
		x = random.randint(-280, 280)
		y = random.randint(-280, 280)
		food.goto(x,y)

		#from playsound import playsound
			#playsound

		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("square")
		new_segment.color("Green")
		new_segment.penup()
		segments.append(new_segment)

		# Scoreboard Point System
		score += 10

		if score > high_score:
			high_score = score

		text.clear()
		text.write("Score: {}     High Score: {}".format(score, high_score),
				align = "center", font =("Courier", 24, "normal"))

	# Move Snake's Body
	totalSeg = len(segments)
	for index in range(totalSeg -1, 0, -1):
		x = segments[index - 1].xcor()
		y = segments[index - 1].ycor()
		segments[index].goto(x,y)

	if totalSeg > 0:
		x = head.xcor()
		y = head.ycor()
		segments[0].goto(x,y)


	mov()

	#Body Collisions
	for segment in segments:
		if segment.distance(head) < 20:
			time.sleep(1)
			head.goto(0,0)
			head.direction = "stop"

			# Hide Segments
			for segment in segments:
				segment.goto(1000,1000)

			segments.clear()

	time.sleep(posponer)

turtle.exitonclick()