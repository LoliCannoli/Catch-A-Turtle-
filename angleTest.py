import math

x1,y1 = 0,10
x2, y2 = 10, 20

slope = (y2 -y1)/(x2 - x1)

x = math.degrees(math.atan(1))
print(x)

import turtle

window = turtle.Screen()

testingTurtle = turtle.Turtle()
testingTurtle.shape('classic')

testingTurtle.setheading(0)

window.mainloop()
