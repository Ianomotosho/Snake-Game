# Simple Snake Game in Python 3.11 for Beginners
#By UkKingOfCodingAndGaming
# Real name - Ian

import turtle
import time
import random

delay = 0.1

#Score
score = 0
high_score = 0


# set up screen
w = turtle.Screen()
w.title("snake game by @Ian Oluwadurotimi Fajobi-omotosho")
w.bgcolor("green")
w.setup(width=800, height=700)
w.tracer(0)

#snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup()
head.goto(0,0)
head_direction = "stop"

segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align= "center",  font=("Courier", 24, "normal"))         


#functions
def move():
    if head_direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head_direction == "down":
          y = head.ycor()
          head.sety(y - 20)

    if head_direction == "left":
          x = head.xcor()
          head.setx(x - 20)

    if head_direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def go_up():
  if head_direction != "down":
    head.direction = "up"

def go_down():
  if head_direction !=  "up":
    head.direction = "down"

def go_left():
    if head_direction !=  "right":
      head.direction = "left"

def go_right():
    if head_direction !=  "left":
      head.direction = "right"


#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)





#keyboard
w.listen() 
w.onkeypress(go_up, "w")
w.onkeypress(go_down, "s")
w.onkeypress(go_left, "a")
w.onkeypress(go_right, "d")
#main game loop
while True:
    w.update()
    # check for a collision
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #hide  the segments
        for segment in segments:
              segment.goto(1000, 1000)

        # clear the segment list
        segments.clear()

        #Reset the score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center"),








    #check for a collision with the food
    if head.distance(food) < 20:
         # move the food to a random spot 
         x = random.randint(-290, 290)
         y = random.randint(-290, 290)
         food.goto(x,y)

         #add a segment
         new_segment = turtle.Turtle()
         new_segment.speed(0)
         new_segment.shape("square")
         new_segment.color("grey")
         new_segment.penup()
         segments.append(new_segment)
         
         # Shorten the delay
         delay  -= 0.001


         #increase the score
         score += 100

         if score > high_score:
              high_score = score
              pen.clear()
         pen.write("Score: {}  High Score: {}".format(score, high_score), align="center"),
         font=("Courier", 24,  "normal")         


         

         # move the end segments first in reverse order
         for index in range(len(segments)-1, 0, -1):
              x = segments[index-1].xcor()
              y = segments[index-1].ycor()
              segments[index].goto(x,y)

        # Move segment 0  to where the head is
         if len(segments)  > 0:
             x = head.xcor()  
             y = head.ycor() 
             segments[0].goto(x,y)

         move()

         # check for head collision with the body segments
         for segment in segments:
              if segment.distance(head) < 20:
                    time.sleep(1)
                    head.goto(0,0)
                    head.direction = "stop"
                  #hide  the segments
                    for segment in segments:
                     segment.goto(1000, 1000)

                     # clear the segment list
                    segments.clear()


                      #reset the delay
                    delay = 0.1
                      
          

                    time.sleep(delay)
                    w.mainloop() 