import turtle
import random
import time
import math

Colors = ['Pink', 'lightblue', 'white']
Shapes = ['circle', 'turtle', 'classic']

color = random.choice(Colors)
shape = random.choice(Shapes)
size = 2
score = 0
timer = 50000000
timerFinished = False
counter_interval = 1000

font = ('Courier New', 20, 'bold')

counter = turtle.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-80, 350)

def countdown():
    global timer, timerFinished
    counter.clear()

    if timer <= 0:
        counter.write('Times Up', font = font)
        timerFinished = True
    else:
        counter.write("Timer: " + str(timer), font = font)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)

scoreWritter = turtle.Turtle()
scoreWritter.hideturtle()
scoreWritter.penup()
scoreWritter.goto(-80, 250)

def updateScore(points):
    global score
    score += points
    scoreWritter.clear()
    scoreWritter.write('Score: ' + str(score) , font = font)

def spotClicked():
    global timerFinished
    if not timerFinished:
        changePosition()
        updateScore(1)
    else:
        return

runner = turtle.Turtle()
runner.fillcolor(color)
runner.shape(shape)
runner.shapesize(size)
runner.penup()
runner.speed(10)
runner.onclick(lambda x, y: spotClicked())

def findHeading(curX, curY, newX, newY):
    #I had to restudy geometry for this T~T
    y = newY -curY
    x = newX - curX

    degrees = math.degrees(math.atan2(y,x))
    print('Degress: ' + str(degrees))
    return degrees - 90

def findDistance(x1, y1, x2, y2):
    unroot = ((x2 - x1)**2) + ((y2 - y1)**2)
    distance = math.sqrt(unroot)
    print('Distance:' + str(distance))
    return distance / 2

pointPloter = turtle.Turtle()
pointPloter.hideturtle()
pointPloter.shape('circle')
pointPloter.penup()

def changePosition():
    currentX, currentY = runner.xcor(), runner.ycor()

    newX = random.randint(-400, 400)
    newY = random.randint(-300, 300)

    pointPloter.goto(newX, newY)
    pointPloter.stamp()

    print('New cords: ' + str(newX) + ', ' + str(newY))

    runner.showturtle()
    runner.setheading(findHeading(currentX, currentY, newX, newY))
    runner.circle(findDistance(currentX, currentY, newX, newY), 180)
    runner.hideturtle()

window = turtle.Screen()
window.ontimer(countdown, counter_interval)
window.bgcolor('gray')
window.mainloop()
