#Test scoreboard notice

import leaderboard
import turtle
import random
import math

playerName = input('What is your name')

Colours = ['Pink', 'lightblue', 'white']
colour = random.choice(Colours)
shape = 'circle'
size = 4

timer = 5
timerFinished = False
counter_interval = 1000

font = ('Courier New', 20, 'bold')

score = 10
pointsToAdd = 1

runner = turtle.Turtle()
runner.fillcolor(colour)
runner.shape(shape)
runner.shapesize(size)
runner.speed(8)
runner.penup()
runner.onclick(lambda x, y: addPoints())

def getNewCords():
    newX = random.randint(-400, 400)
    newY = random.randint(-300, 300)
    return newX, newY

def moveToNewLocation():
    global timerFinished

    if not timerFinished:
        runner.showturtle()
        newX, newY = getNewCords()
        runner.goto(newX, newY)
    else:
        return


scoreWritter = turtle.Turtle()
scoreWritter.hideturtle()
scoreWritter.penup()
scoreWritter.goto(-80, 250)

def addPoints():
    global score, pointsToAdd

    if runner.isvisible():
        turtle.hideturtle()
        score += pointsToAdd

        scoreWritter.clear()
        scoreWritter.write('Score: ' + str(score) , font = font)
        moveToNewLocation()

def findHeading(x1, y1, x2, y2):
    #I had to restudy geometry for this T~T
    y = y2 -y1
    x = x2 - x1

    degrees = math.degrees(math.atan2(y,x))
    print('Degress: ' + str(degrees))
    return degrees - 90

def findDistance(x1, y1, x2, y2):
    unroot = ((x2 - x1)**2) + ((y2 - y1)**2)
    distance = math.sqrt(unroot)
    print('Distance:' + str(distance))
    return distance / 2

def moveInArc():
    currentX, currentY = runner.xcor(), runner.ycor()

    newX, newY = getNewCords()

    runner.showturtle()
    runner.setheading(findHeading(currentX, currentY, newX, newY))
    runner.circle(findDistance(currentX, currentY, newX, newY), 180)
    runner.hideturtle()

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

window = turtle.Screen()
window.bgcolor('gray')
window.ontimer(countdown, counter_interval)

while not timerFinished:
    moveInArc()
    moveToNewLocation()

leaderboardTurtle = turtle.Turtle()
leaderboardTurtle.hideturtle()
leaderboardTurtle.penup()
leaderboardTurtle.goto(leaderboardTurtle.xcor() - 75, leaderboardTurtle.ycor())

if(timerFinished):
    runner.hideturtle()
    leaderboard.addItemToLeaderboard(playerName, score)
    topThreeList = leaderboard.getTopX(3)
    for player in ltopThreeList:
        leaderboardTurtle.write(player, font = font)
        leaderboardTurtle.goto(leaderboardTurtle.xcor(), leaderboardTurtle.ycor() - 30)

    if (playerName + ' - ' + str(score) in topThreeList):
        print('You made the leaderboard')


window.mainloop()
