# import package and making objects
import turtle

import numpy as np
# Not sure if I need to import robot if an object is passed to a function

import random 
sc=turtle.Screen()
trtl=turtle.Turtle()
 
# method to draw y-axis lines
def drawy(val):
     
    # line
    
    trtl.forward(600)
     
    # set position
    trtl.up()
    #trtl.setpos(val,300)
    trtl.down()
     
    # another line
    trtl.backward(600)
     
    # set position again
    trtl.up()
    trtl.setpos(-300 + val, -300)
    trtl.down()
     
# method to draw y-axis lines
def drawx(val):
     
    # line
    trtl.forward(600)
     
    # set position
    trtl.up()
    #trtl.setpos(-135, val)
    trtl.down()
     
    # another line
    trtl.backward(600)
     
    # set position again
    trtl.up()
    trtl.setpos(-300, -300 + val)
    trtl.down()
     
def moveRobots(bot, currentLocation, nextLocation):
    
    bot.penup()
    if(currentLocation == (0,0)):
        bot.goto(-285, 285)
    else:
        bot.pendown()
        #bot.goto(-285  + currentLocation[1] * 30, 285 - currentLocation[0] * 30)
    
    # Don't move if path not found 
    if currentLocation[1] != -1:
        bot.pendown()
        bot.goto(-285 + nextLocation[1] * 30, 285 - nextLocation[0] * 30)
        bot.penup()

    # Bot with no path turns red
    else:
        bot.penup()
        bot.color('red')
        bot.goto(-315, 285)



def createObstical(x, y):
    obstical = turtle.Turtle()
    obstical.penup()
    obstical.color('red')
    obstical.shape('circle')
    obstical.speed(10)

    obstical.goto(-285 + (30 * y), 285 - (30 * x))

     
 
# Tun this function and pass it robot(s)
def runAnimation(robots, grid):
    # set screen
    sc.setup(800, 800)   
    
    # set turtle features
    trtl.speed(100)
    trtl.left(90) 
    trtl.color('black')
    

    # y lines
    for i in range(21):
        if(i == 0):
            trtl.up()
            trtl.setpos(-300,-300)
        drawy(30*(i+1))
    
    # set position for x lines
    trtl.right(90)
    trtl.up()
    trtl.setpos(-300,-300)
    trtl.down()
    
    # x lines
    for i in range(21):
        drawx(30*(i+1))
    
    # hide the turtle
    trtl.hideturtle()

    # Find which path is longest
    longestRobotPath = 0
    bots = []

    # Add the obsticals to show how turty has to go around obsticals 
    for i in range(20):
        for j in range(20):
            if grid[i][j] == 1:
                createObstical(i, j)

    # Need to add colors: Green for one bag, red for 2 bags?

    for i in range(len(robots)):
        bots.append(turtle.Turtle())
        bots[i].color('black')
        bots[i].shape('turtle')
        bots[i].speed(10)

    for i in robots:
        if len(i.path) > longestRobotPath:
            longestRobotPath = len(i.path)
    

    for i in range(longestRobotPath):
        for j in range(len(robots)):
            # check if robot 0 exits
            if len(robots[j].path) == 0:
                moveRobots(bots[j], (0, -1), (0, 0))

            else:
                # check 
                if (i < len(robots[j].path)) and (robots[j].path[i] is not None or robots[j].path[i] is not [0,0]) and len(robots[j].path) != 0:

                    # initialize the location of the 'robot' when i = 0
                    if i == 0:
                        moveRobots(bots[j], currentLocation = robots[j].path[i], nextLocation = robots[j].path[i])
                    
                    # when we are at the last index of the path we don't need to move the turtle again, so curPath = nextPath
                    elif i is len(robots[j].path) - 1:
                        moveRobots(bots[j], currentLocation = robots[j].path[i], nextLocation = robots[j].path[i])
                        bots[j].color('lightgreen')

                    #Once first delivery is made turn turtle orange 
                    elif robots[j].delivery[0][0] == robots[j].path[i][0] and robots[j].delivery[0][1] == robots[j].path[i][1]:
                        moveRobots(bots[j], currentLocation = robots[j].path[i], nextLocation = robots[j].path[i])
                        bots[j].color('orange')


                    #  in every other case besides the first and the last index, move to the next location in the path array
                    else:
                        moveRobots(bots[j], currentLocation = robots[j].path[i], nextLocation = robots[j].path[i + 1])

    sc.exitonclick()

